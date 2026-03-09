import torch
from rocket import Rocket
from policy import ActorCritic
import os
import glob

# Decide which device we want to run on
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

if __name__ == '__main__':

    task = 'landing'  # Make sure this matches our training task!
    max_steps = 800
    
    # Find all saved brains in the checkpoint folder
    ckpt_dir = glob.glob(os.path.join(task+'_ckpt', '*.pt'))
    
    env = Rocket(task=task, max_steps=max_steps)
    net = ActorCritic(input_dim=env.state_dims, output_dim=env.action_dims).to(device)
    
    # Load the most recent brain if it exists
    if len(ckpt_dir) > 0:
        checkpoint = torch.load(ckpt_dir[-1],weights_only=False)  # load the most recent checkpoint
        net.load_state_dict(checkpoint['model_G_state_dict'])
        print("Successfully loaded the trained brain!")
    else:
        print("No saved brain found. It will fly randomly.")

    state = env.reset()
    
    # The final exam loop
    for step_id in range(max_steps):
        
        # deterministic=True forces the AI to use its best knowledge, no random exploring
        action, log_prob, value = net.get_action(state, deterministic=True)
        state, reward, done, _ = env.step(action)
        
        # Open the visual window every single frame
        env.render(window_name='Test Flight')
        
        # Stop the test if it hits the ground
        if env.already_crash or env.already_landing:
            break