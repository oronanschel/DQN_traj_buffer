import subprocess, sys

def run_watch():
  a = '/home/oron/Workspace/DQN_theano_time_average/models/2016-10-08_10-18-45/last_model.pkl'
  command = ['python', 'train_q.py', '--steps-per-epoch', '0',
  '--test-length', '100000', '--nn-file', a, '--display-screen']

  p1 = subprocess.Popen(command)
  p1.wait()
    
if __name__ == "__main__":
  run_watch()
