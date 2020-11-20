from .adapters.gym_adapter import GymAdapter

ADAPTERS = {
    'gym': GymAdapter,
}
try:
    from .adapters.robosuite_adapter import RobosuiteAdapter

    ADAPTERS['robosuite'] = RobosuiteAdapter
except ModuleNotFoundError as e:
    if 'robosuite' not in e.msg:
        raise

    print("Warning: robosuite package not found. Run `pip install robosuite`"
          " to use robosuite environments.")

UNIVERSES = set(ADAPTERS.keys())


def get_environment(universe, domain, task, environment_params):
    return ADAPTERS[universe](domain, task, **environment_params)


def get_environment_from_params(environment_params):
    universe = environment_params['universe']
    task = environment_params['task']
    domain = environment_params['domain']
    environment_kwargs = environment_params.get('kwargs', {}).copy()

    return get_environment(universe, domain, task, environment_kwargs)
