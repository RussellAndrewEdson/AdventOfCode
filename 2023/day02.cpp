/**
 * C++ code for the 2023 Advent of Code, Day 2.
 *
 * Code author: Russell A. Edson
 * Date last modified: 02/12/2023
 */
#include <iostream>
#include <string>
#include <fstream>
#include <regex>

// Helper function: get number of coloured cubes in handful
int numCubes(const std::string& handful, const std::string& colour) {
    std::regex colourRegex("(\\d+) " + colour);
    std::smatch match;
    int number = 0;
    if (std::regex_search(handful, match, colourRegex)) {
        number = std::stoi(match[1]);
    }
    return number;
}

int main(int argc, char* argv[]) {
    std::string line, currentChar, handful;
    unsigned int strIndex;
    int red, maxRed, green, maxGreen, blue, maxBlue, gameIdSum, powerSum;
    bool gamePossible;
    std::ifstream file("day02.txt");
    std::regex idRegex("Game (\\d+):");
    std::smatch match;
    std::vector<int> gameIds, part1PossibleGames;
    int currentGameId;
    std::vector<std::vector<std::string>> handfuls;
    std::vector<std::string> currentHandfuls;

    if (file.is_open()) {
        while (std::getline(file, line)) {
            if (std::regex_search(line, match, idRegex)) {
                currentGameId = std::stoi(match[1]);
                gameIds.push_back(currentGameId);
            }

            currentHandfuls.clear();
            // Skip to after Game ...:
            strIndex = 0;
            currentChar = line[strIndex];
            while (currentChar != ":" && strIndex < line.size()) { 
                currentChar = line[strIndex];
                strIndex++;
            }
            strIndex++;

            handful = "";
            while (strIndex < line.size()) {
                currentChar = line[strIndex];
                if (currentChar == ";") {
                    if (handful != "") {
                        currentHandfuls.push_back(handful);
                        handful = "";
                    }
                } else {
                    handful += currentChar;
                }
                strIndex++;
            }
            if (handful != "") {
                currentHandfuls.push_back(handful);
            }
            handfuls.push_back(currentHandfuls);
        }
    }

    // Part 1
    gameIdSum = 0;
    maxRed = 12;
    maxGreen = 13;
    maxBlue = 14;
    for (unsigned int i = 0; i < gameIds.size(); i++) {
        gamePossible = true;
        currentHandfuls = handfuls[i];
        for (unsigned int j = 0; j < currentHandfuls.size(); j++) {
            red = numCubes(currentHandfuls[j], "red");
            green = numCubes(currentHandfuls[j], "green");
            blue = numCubes(currentHandfuls[j], "blue");

            if (red > maxRed || green > maxGreen || blue > maxBlue) {
                gamePossible = false;
            }
        }

        if (gamePossible) {
            part1PossibleGames.push_back(gameIds[i]);
        }
    }
    for (unsigned int i = 0; i < part1PossibleGames.size(); i++) {
        gameIdSum += part1PossibleGames[i];
    }
    std::cout << "Part 1: " << gameIdSum << std::endl;

    // Part 2
    powerSum = 0;
    for (unsigned int i = 0; i < gameIds.size(); i++) {
        currentHandfuls = handfuls[i];
        maxRed = 0;
        maxGreen = 0;
        maxBlue = 0;
        for (unsigned int j = 0; j < currentHandfuls.size(); j++) {
            red = numCubes(currentHandfuls[j], "red");
            green = numCubes(currentHandfuls[j], "green");
            blue = numCubes(currentHandfuls[j], "blue");

            if (red > maxRed) { maxRed = red; }
            if (green > maxGreen) { maxGreen = green; }
            if (blue > maxBlue) { maxBlue = blue; }
        }
        powerSum += maxRed * maxGreen * maxBlue;
    }

    std::cout << "Part 2: " << powerSum << std::endl;
    return 0;
}
