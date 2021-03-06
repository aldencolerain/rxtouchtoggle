import nox

@nox.session
def test(session):
    session.install('pytest')
    session.install('pytest-mock')
    session.run('pytest', *session.posargs)


@nox.session
def lint(session):
    session.install('pylint')
    session.run('pylint', 'rxtouchtoggle')
