"""
Note that this file cannot be modified.
If you would like to add your own unit tests, please put these in a separate file.
"""

import pytest

from src.animal_farm import AnimalFarm

M, N = 1000, 1000
_animal_farm = AnimalFarm([
    [
        i*N + j for j in range(N)
    ] for i in range(M)
])

@pytest.fixture
def animal_farm_setup():
    return _animal_farm

def get_count(i, j, k):
    return (j+1) * k * i * (i+1) // 2 + (i+1) * j * (j+1) // 2

@pytest.mark.timeout(5)
def test_count_all_regions(animal_farm_setup):
    m, n = animal_farm_setup.dimension()
    for i in range(m):
        for j in range(n):
            assert animal_farm_setup.count(
                (0, 0), (i, j),
            ) == get_count(i, j, n)

@pytest.mark.timeout(5)
def test_count_single_cell(animal_farm_setup):
    assert animal_farm_setup.count((1,1), (1,1)) == N+1

@pytest.mark.timeout(5)
def test_update(animal_farm_setup):
    m, n = animal_farm_setup.dimension()

    old = animal_farm_setup.count((m//2,n//2), (m//2,n//2))
    new = old+1
    animal_farm_setup.update((m//2,n//2), new)

    # Queries that don't include the updated cell should stay the same.
    assert animal_farm_setup.count((0,0), (m//2-1,n//2-1)) == get_count(m//2-1, n//2-1, n)

    # Queries that do include the updated cell should change.
    assert animal_farm_setup.count((0,0), (m-1,n-1)) == get_count(m-1, n-1, n)+1
