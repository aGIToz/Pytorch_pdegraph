def info():
    about = """
    This subpackage implements operators on graphs to run a manually defined PDE on graph, Calculus on graphs.

    Ref:
    https://en.wikipedia.org/wiki/Calculus_on_finite_weighted_graphs
    """
    print(about)

__all__ = [
        'GradInfNorm',
        'GradMinusInfNorm',
        'GradMinusNorm',
        'GradNorm',
        'GradPlusInfNorm',
        'GradPlusNorm',
        'MeanCurv',
        'LapIso',
        'LapAniso',
        'info',

]
