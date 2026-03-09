# Starship RL Landing: Modernized A2C Simulation

This project is a modernized and improved version of the open-source rocket recycling simulation created by **Zhengxia Zou**. I utilized this repository as a practical learning tool to study Advantage Actor-Critic (A2C) reinforcement learning architectures and environment design.

The original, highly recommended repository can be found here: [jiupinjia/rocket-recycling](https://github.com/jiupinjia/rocket-recycling)

<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/0354880a-c8f3-4f8d-876b-b19e87882e69" />


## 🏆 Attribution & Citation
Full credit for the foundational 2D physics engine, base environment (`rocket.py`), and the original neural network architecture goes to Zhengxia Zou. 

```bibtex
@misc{zou2021rocket,
  author = {Zhengxia Zou},
  title = {Rocket-recycling with Reinforcement Learning},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jiupinjia/rocket-recycling}}
}
```
## 🛠️ Modifications & Modernization
While the core physics engine remains intact, I implemented several quality-of-life updates and technical fixes to stabilize the learning algorithm and ensure compatibility with modern software libraries:

* **NumPy 2.0 Compatibility:** Updated the legacy matrix multiplication logic (`np.mat`) in the utility functions to use `np.asmatrix`, preventing crash errors on modern NumPy installations.
* **PyTorch 2.6 Security Bypass:** Added the `weights_only=False` flag to the `torch.load` pipeline to allow legacy custom checkpoint dictionaries (which include episode IDs and reward histories) to load without triggering new PyTorch security blocks.
* **Algorithm Stabilization:** Diagnosed a Catastrophic Forgetting loop causing policy collapse during late-stage training. Implemented a Gradient Clipping speed limit (`torch.nn.utils.clip_grad_norm_`) to stabilize the neural network's learning curve.
* **Task Optimization:** Re-engineered the training loop to default to the complex Starship "bellyflop" landing maneuver rather than the basic hovering task.

## 🔗 Connection to My B.Tech Honours Project
Studying this repository heavily inspired my own personal Reinforcement Learning project. Specifically, I adapted this author's incredibly clean checkpointing file structure and reward graphing implementation for my own work. 

You can check out my independent B.Tech Honours Mini-Project here: 
👉 [MathewJobey/S8-Honours-Reinforcement_Learning-Mini_Project](https://github.com/MathewJobey/S8-Honours-Reinforcement_Learning-Mini_Project)

## 📄 License
Under the ShareAlike clause of the original repository, this modified project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0).
