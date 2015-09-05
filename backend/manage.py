import sys
import os
dirname = os.path.dirname
sys.path.insert(0, dirname(dirname(os.path.abspath(__file__))))

from backend import manager
if __name__ == '__main__':
    manager.run()
