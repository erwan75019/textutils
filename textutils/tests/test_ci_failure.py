# Test volontairement incorrect pour vérifier que la CI détecte les erreurs

# def test_ci_intentional_failure():
# assert 1 == 2, "Intentional CI failure"

# Test corrigé pour vérifier que la CI repasse au vert


def test_ci_intentional_failure():
    assert 1 == 1, "CI test should pass"
