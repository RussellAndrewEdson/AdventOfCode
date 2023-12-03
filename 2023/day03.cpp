/**
 * C++ code for the 2023 Advent of Code, Day 3.
 *
 * Code author: Russell A. Edson
 * Date last modified: 03/12/2023
 */
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

// Helper function: a symbol is anything that isn't a number or a dot.
bool isSymbol(char character) {
    return !(std::isdigit(character) || character == '.');
}

// Helper function: true if the given places are for a part number.
bool isPartNumber(std::vector<std::string> schematic, int row, 
        std::vector<int> places) {
    bool isPartNumber = false;
    int labelStart, labelEnd;
    for (int i = row - 1; i <= row + 1; i++) {
        if (i >= 0 && i < static_cast<int>(schematic.size())) {
            labelStart = places.at(0);
            labelEnd = places.back();
            for (int j = labelStart - 1; j <= labelEnd + 1; j++) {
                if (j >= 0 && j < static_cast<int>(schematic[i].size())) {
                    if (isSymbol(schematic[i][j])) {
                        isPartNumber = true;
                    }
                }
            }
        }
    }
    return isPartNumber;
}

int main(int argc, char* argv[]) {
    std::vector<std::string> schematic;
    std::vector<int> serialNumbers, gearNumbers, labelPlaces;
    std::vector<bool> isPartNumbers;
    std::string line, labelBuffer;
    char currentChar;
    int part1Sum, part2Sum;
    bool adjacent;
    std::ifstream file("day03.txt");

    if (file.is_open()) {
        while (std::getline(file, line)) {
            schematic.push_back(line);
        }
    }

    // Part 1
    for (unsigned int i = 0; i < schematic.size(); i++) {
        labelBuffer = "";
        labelPlaces.clear();
        for (unsigned int j = 0; j < schematic[i].size(); j++) {
            currentChar = schematic[i][j];
            if (std::isdigit(currentChar)) {
                labelBuffer.append(std::string(1, currentChar));
                labelPlaces.push_back(j);
            } else {
                if (labelBuffer.size() > 0) {
                    serialNumbers.push_back(std::stoi(labelBuffer));
                    isPartNumbers.push_back(
                        isPartNumber(schematic, i, labelPlaces)
                    );
                }
                labelBuffer = "";
                labelPlaces.clear();
            }

            // At end of line: check for a completed serial number
            if (j + 1 == schematic[i].size() && labelBuffer.size() > 0) {
                if (labelBuffer.size() > 0) {
                    serialNumbers.push_back(std::stoi(labelBuffer));
                    isPartNumbers.push_back(
                        isPartNumber(schematic, i, labelPlaces)
                    );
                }
                labelBuffer = "";
                labelPlaces.clear();
            }
        }
    }

    part1Sum = 0;
    for (unsigned int i = 0; i < serialNumbers.size(); i++) {
        if (isPartNumbers[i]) {
            part1Sum += serialNumbers[i];
        }
    }
    std::cout << "Part 1: " << part1Sum << std::endl;

    // Part 2
    part2Sum = 0;
    for (unsigned int i = 0; i < schematic.size(); i++) {
        for (unsigned int j = 0; j < schematic[i].size(); j++) {
            currentChar = schematic[i][j];
            if (currentChar == '*') {
                gearNumbers.clear();
                
                for (int ii = static_cast<int>(i) - 1; 
                        ii <= static_cast<int>(i) + 1; ii++) {
                    if (ii >= 0 && ii < static_cast<int>(schematic.size())) {
                        labelBuffer = "";
                        labelPlaces.clear();
                        for (int jj = 0; 
                                jj < static_cast<int>(schematic[ii].size()); 
                                jj++) {
                            currentChar = schematic[ii][jj];
                            if (std::isdigit(currentChar)) {
                                labelBuffer.append(std::string(1, currentChar));
                                labelPlaces.push_back(jj);
                            } else {
                                if (labelBuffer.size() > 0) {
                                    adjacent = false;
                                    for (int place : labelPlaces) {
                                        if (place == static_cast<int>(j) - 1 || 
                                                place == static_cast<int>(j) || 
                                                place == static_cast<int>(j) 
                                                + 1) {
                                            adjacent = true;
                                        }
                                    }
                                    if (adjacent) {
                                        gearNumbers.push_back(
                                            std::stoi(labelBuffer)
                                        );
                                    }
                                }
                                labelBuffer = "";
                                labelPlaces.clear();
                            }

                            // At end of line, check for a completed number
                            if (jj + 1 == static_cast<int>(schematic[ii].size()) 
                                    && labelBuffer.size() > 0) {
                                if (labelBuffer.size() > 0) {
                                    adjacent = false;
                                    for (int place : labelPlaces) {
                                        if (place == static_cast<int>(j) - 1 || 
                                                place == static_cast<int>(j) || 
                                                place == static_cast<int>(j) 
                                                + 1) {
                                            adjacent = true;
                                        }
                                    }
                                    if (adjacent) {
                                        gearNumbers.push_back(
                                            std::stoi(labelBuffer)
                                        );
                                    }
                                }
                                labelBuffer = "";
                                labelPlaces.clear();
                            }
                        }
                    }
                }

                // Multiply gear numbers if exactly two
                if (gearNumbers.size() == 2) {
                    part2Sum += gearNumbers[0] * gearNumbers[1];
                }
            }
        }
    }
    std::cout << "Part 2: " << part2Sum << std::endl;

    return 0;
}
