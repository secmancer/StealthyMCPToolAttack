# Improving the Stealthiness of Tool Learning Attacks against Coding Agents
## Authors: Alden Wang, Adan Silva, Andrea Ng

Code repository for this paper, which was written for CSC 429 Spring 2026

# Project Structure
- `baseline/`: Contains the baseline scripts derived from TIPExploit's ideas.
  - Contains a baseline RCE and DoS version.
  - Use the workspace_manager and env_setter tool structure originally used.
- `modified/`: Contains the modified RCE version made more stealthy.
  - Derived from the baseline RCE version, but uses an API server to hide the payload.
  - Presents itself as a "secure" file downloader.
- `tools/`: Contains our prompt guard check we used along with its dependencies. 

# Baseline Paper
Our work is built off of the paper: Red-Teaming Coding Agents from a Tool-Invocation Perspective: An Empirical Security Assessment.
Our baseline scripts are derived from the TIPExploit repository, but modified to suit our needs.
- Paper: https://arxiv.org/pdf/2509.05755
- Code: https://github.com/TIPExploit/TIPExploit/tree/main

# Note
This work is intended for research and educational purposes only. Do not use it for malicious purposes.

# Setup
To set up the environment, run the setup script:
```bash
./setup.sh
```
After, activate the virtual environment:
```bash
source .venv/bin/activate
```

# Running the adversarial server
- To run the adversarial server, use the script within the modified folder:
```bash
./run_adversarial_server.sh
```
- This activates the virtual environment and runs the adversarial server for you.
- Therefore, using this script, you don't need to activate the virtual environment manually.
