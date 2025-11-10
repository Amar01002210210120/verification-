#include <iostream>
#include <random>    // RNG
#include <vector>    // for std::vector, simple

int main() {
    // Parameters
    const double initial_price = 100.0; // const so the values don't change, double for 64 bit double-percision (VERY IMPORTANT IN FINANCE unlike long double or float)
    const double up_return = 0.01;    // +1%
    const double down_return = -0.01; // -1%
    const int days = 10;              // length of each path
    const int num_paths = 1000;       // number of simulations

    // Random number setup
    std::random_device rd;           // seed source
    std::mt19937 rng(rd());          // Mersenne Twister engine
    std::bernoulli_distribution coin_flip(0.55); // Gave the stock a little updrift, now we see slight uptick instead of base 50/50, it is stocks after all 

    int count_above_initial = 0;

    for (int path = 0; path < num_paths; ++path) {
        double price = initial_price;

        for (int d = 0; d < days; ++d) {
            bool up = coin_flip(rng); // true or false 

            if (up) {
                price *= (1.0 + up_return);
            } else {
                price *= (1.0 + down_return);
            }
        }

        if (price > initial_price) {
            ++count_above_initial;
        }
    }

    double probability = static_cast<double>(count_above_initial) / num_paths;

    std::cout << "Initial price: " << initial_price << "\n";
    std::cout << "Number of paths: " << num_paths << "\n";
    std::cout << "Days per path: " << days << "\n";
    std::cout << "Paths ending above initial: " << count_above_initial << "\n";
    std::cout << "Estimated probability(final > initial): " << probability << "\n";

    return 0;
}

// Simple introduction for monte carlo. Possibly look into implementing markov chains into project
