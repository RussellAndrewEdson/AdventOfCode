/**
 * C++ code for the 2023 Advent of Code, Day 01.
 * 
 * Code author: Russell A. Edson
 * Date last modified: 01/12/2023
 */
#include <iostream>
#include <string>
#include <fstream>
#include <regex>

// Extract the numerical digits from a given string
std::string extractDigits(const std::string& str) {
    std::string digits = "";
    std::regex regex("(\\d)");
    std::sregex_iterator iter(str.begin(), str.end(), regex);
    std::sregex_iterator end;

    while (iter != end) {
        for (unsigned i = 0; i < iter->size(); i++) {
            digits += (*iter)[i];
        }
        iter++;
    }
    return digits;
}

// Convert a given spelled digit
std::string convertSpelledDigit(const std::string& digit) {
    if (digit == "one")   { return "1"; }
    if (digit == "two")   { return "2"; }
    if (digit == "three") { return "3"; }
    if (digit == "four")  { return "4"; }
    if (digit == "five")  { return "5"; }
    if (digit == "six")   { return "6"; }
    if (digit == "seven") { return "7"; }
    if (digit == "eight") { return "8"; }
    if (digit == "nine")  { return "9"; }
    return digit;
}

// Extract numerical and spelled words from a given string
std::string extractNumAndSpelledDigits(const std::string& str) {
    std::string digits = "";
    std::regex regex("(?=(\\d|one|two|three|four|five|six|seven|eight|nine))");
    std::sregex_iterator iter(str.begin(), str.end(), regex);
    std::sregex_iterator end;

    while (iter != end) {
        for (unsigned i = 0; i < iter->size(); i++) {
            digits += convertSpelledDigit((*iter)[i]);
        }
        iter++;
    }
    return digits;
}


int main() {
    std::string line, digits;
    int value, part1Total = 0, part2Total = 0;

    std::ifstream file("day01.txt");
    if (file.is_open()) {
        while (std::getline(file, line)) {
            // Part 1
            digits = extractDigits(line);
            value = std::stoi(std::string(1, digits.at(0)) + digits.back());
            part1Total += value;

            // Part 2
            digits = extractNumAndSpelledDigits(line);
            value = std::stoi(std::string(1, digits.at(0)) + digits.back());
            part2Total += value;
        }
    }

    std::cout << "Part 1: " << part1Total << std::endl;
    std::cout << "Part 2: " << part2Total << std::endl;
    return 0;
}
