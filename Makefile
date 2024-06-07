voronoi:
	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function euler \
		--distribution-function random
	
	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function manhattan \
		--distribution-function random
	
	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function chebyshev \
		--distribution-function random

	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function euler \
		--distribution-function min-distance \
		--min-distance 5.0

	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function manhattan \
		--distribution-function min-distance \
		--min-distance 5.0

	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function chebyshev \
		--distribution-function min-distance \
		--min-distance 5.0
	
	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function euler \
		--distribution-function fuzzy-grid \
		--fuzz-radius 5.0

	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function manhattan \
		--distribution-function fuzzy-grid \
		--fuzz-radius 5.0

	poetry run adventure voronoi 50 50 10 \
		--seed 1337 \
		--distance-function chebyshev \
		--distribution-function fuzzy-grid \
		--fuzz-radius 5.0