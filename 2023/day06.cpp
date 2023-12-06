/**
 * C++ code for the 2023 Advent of Code, Day 6.
 * 
 * Code author: Russell A. Edson
 * Date last modified: 06/12/2023
 */
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <numeric>
#include <cmath>

int main(int argc, char* argv[]) {
    std::string line, token, concatenation;
    std::ifstream file("day06.txt");
    std::vector<int> times, bestDistances, raceWins;
    std::stringstream sstream;
    int distance, bestDistance, time, winCount, part1Solution;
    long int part2BestDistance, part2Time, discriminant, leftRoot, 
        rightRoot, fudge, part2Solution;
    double sqrtDiscriminant;

    if (file.is_open()) {
        // First line is times
        std::getline(file, line);
        sstream.str(line);
        sstream >> token;  // ignore "Time:"
        while (sstream >> token) {
            times.push_back(std::stoi(token));
        }
        sstream.clear();

        // Second line is distances
        std::getline(file, line);
        sstream.str(line);
        sstream >> token; // ignore "Distance:"
        while (sstream >> token) {
            bestDistances.push_back(std::stoi(token));
        }
        sstream.clear();

        // Part 1
        for (unsigned int i = 0; i < times.size(); i++) {
            time = times[i];
            bestDistance = bestDistances[i];
            winCount = 0;

            for (int holdTime = 0; holdTime <= time; holdTime++) {
                distance = holdTime * (time - holdTime);

                if (distance > bestDistance) {
                    winCount++;
                }
            }
            raceWins.push_back(winCount);
        }
        part1Solution = std::accumulate(raceWins.begin(), raceWins.end(), 
            1, std::multiplies<>());
        std::cout << "Part 1: " << part1Solution << std::endl;

        // Part 2
        concatenation = "";
        for (int time : times) {
            concatenation += std::to_string(time);
        }
        part2Time = std::stol(concatenation);
        concatenation = "";
        for (int bestDistance : bestDistances) {
            concatenation += std::to_string(bestDistance);
        }
        part2BestDistance = std::stol(concatenation);

        // Mathematically, winning times only occur between the roots
        // of the equation holdTime*(time - holdTime) - bestDistance = 0
        // (since we are doing float<->int conversions on huge numbers, 
        // we add a fudge factor here to make sure we get the right 
        // integer roots that we want).
        fudge = 10;
        discriminant = part2Time * part2Time - 4 * part2BestDistance;
        sqrtDiscriminant = 0.5 * std::sqrt(discriminant);
        leftRoot = (part2Time / 2) - std::floor(sqrtDiscriminant) - fudge;
        while (leftRoot * (part2Time - leftRoot) - part2BestDistance < 0) {
            leftRoot++;
        }
        rightRoot = (part2Time / 2) + std::floor(sqrtDiscriminant) + fudge;
        while (rightRoot * (part2Time - rightRoot) - part2BestDistance < 0) {
            rightRoot--;
        }
        part2Solution = rightRoot - leftRoot + 1;
        std::cout << "Part 2: " << part2Solution << std::endl;
    }
    return 0;
}
