/**
 * C++ code for the 2023 Advent of Code, Day 4.
 *
 * Code author: Russell A. Edson
 * Date last modified: 04/12/2023
 */
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <regex>
#include <sstream>

class Card {
    public:
        int cardNumber;
        std::vector<int> winningNumbers, scratchedNumbers;
        Card(int, std::vector<int>, std::vector<int>);
};

Card::Card(int number, std::vector<int> winning, std::vector<int> scratched) {
    cardNumber = number;
    winningNumbers = winning;
    scratchedNumbers = scratched;
}

int main(int argc, char* argv[]) {
    std::vector<Card> cards;
    int cardNumber, value, points, matches, part1Points, part2Total;
    bool winner;
    std::vector<int> winningNumbers, scratchedNumbers, cardCopies;
    std::string line, cardPart, winningPart, scratchedPart;
    std::ifstream file("day04.txt");
    std::regex cardRegex("Card[ ]*(\\d+):");
    std::regex winningRegex(":(.*)(?=\\|)");
    std::regex scratchedRegex("\\|(.*)$");
    std::smatch match;

    if (file.is_open()) {
        while (std::getline(file, line)) {
            cardNumber = 0;
            winningNumbers.clear();
            scratchedNumbers.clear();

            if (std::regex_search(line, match, cardRegex)) {
                cardPart = match[1];
                cardNumber = std::stoi(cardPart);
            }
            if (std::regex_search(line, match, winningRegex)) {
                winningPart = match[1];
                std::stringstream sstream(winningPart);
                while (sstream >> value) {
                    winningNumbers.push_back(value);
                }
            }
            if (std::regex_search(line, match, scratchedRegex)) {
                scratchedPart = match[1];
                std::stringstream sstream(scratchedPart);
                while (sstream >> value) {
                    scratchedNumbers.push_back(value);
                }
            }
            cards.push_back(Card(cardNumber, winningNumbers, scratchedNumbers));
        }
    }

    // Part 1
    part1Points = 0;
    for (Card card : cards) {
        points = 0;
        for (int scratchedNumber : card.scratchedNumbers) {
            winner = false;
            for (int winningNumber : card.winningNumbers) {
                if (scratchedNumber == winningNumber) {
                    winner = true;
                }
            }
            if (winner) {
                if (points == 0) {
                    points = 1;
                } else {
                    points *= 2;
                }
            }
        }
        part1Points += points;
    }
    std::cout << "Part 1: " << part1Points << std::endl;

    // Part 2
    part2Total = 0;
    cardCopies.clear();
    for (Card card : cards) {
        cardCopies.push_back(1);
    }
    for (unsigned int i = 0; i < cardCopies.size(); i++) {
        Card card = cards[i];
        matches = 0;
        for (int scratchedNumber : card.scratchedNumbers) {
            winner = false;
            for (int winningNumber : card.winningNumbers) {
                if (scratchedNumber == winningNumber) {
                    winner = true;
                }
            }
            if (winner) {
                matches += 1;
            }
        }

        for (int j = 1; j <= matches; j++) {
            cardCopies[i + j] += cardCopies[i];
        }
    }
    for (unsigned int i = 0; i < cardCopies.size(); i++) {
        part2Total += cardCopies[i];
    }
    std::cout << "Part 2: " << part2Total << std::endl;

    return 0;
}


