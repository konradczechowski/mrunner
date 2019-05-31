from munch import Munch

from mrunner.experiment import Experiment
import sys, os

sys.path.append(os.path.join(os.getcwd(), 'some_utils'))

def create_experiment_for_spec(parameters):
   # @HM: here you include mpi command
   # script = "mpi command here"
   script = 'mpirun python experiment_basic.py'
   # this will be also displayed in jobs on prometheus
   name = 'your initials, experiment name'
   project_name = "sandbox"
   python_path = '.:some_utils:some/other/utils/path'
   paths_to_dump = ''  # e.g. 'plgrid tensor2tensor', do we need it?
   tags = 'test_user other_tag'.split(' ')
   return Experiment(project=project_name, name=name, script=script,
                     parameters=parameters, python_path=python_path,
                     paths_to_dump=paths_to_dump, tags=tags,
                     time='0-0:10'
                     # ,ntasks=2
                     )



def spec():
  params = Munch(param1=10, param2=12, wd=10)
  experiments = [create_experiment_for_spec(params)]
  return experiments