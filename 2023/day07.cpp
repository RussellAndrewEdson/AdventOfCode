/**
 * C++ code for the 2023 Advent of Code, Day 7.
 *
 * Code author: Russell A. Edson
 * Date last modified: 07/12/2023
 */
#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <tuple>

enum HandType {
    FIVE_OF_A_KIND = 0x00700000,
    FOUR_OF_A_KIND = 0x00600000,
    FULL_HOUSE = 0x00500000,
    THREE_OF_A_KIND = 0x00400000,
    TWO_PAIR = 0x00300000,
    ONE_PAIR = 0x00200000,
    HIGH_CARD = 0x00100000
};

const char handValues[13] = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 
    'Q', 'K', 'A'};
const unsigned int handValuesCount = 13;

// Helper function: returns the hand-type modifier for hex
HandType getHandType(std::vector<char> hand, bool jokerIsWildcard) {
    std::map<char, int> cardCounts;
    std::vector<int> counts;
    int jokerCount = 0;
    HandType type = HIGH_CARD;

    for (char card : hand) {
        if (jokerIsWildcard && card == 'J') {
            jokerCount++;
        } else {
            cardCounts[card]++;
        }
    }
    for (auto const& [card, count] : cardCounts) {
        counts.push_back(count);
    }
    std::sort(counts.rbegin(), counts.rend());

    // Check for pathological all-joker case
    if (jokerIsWildcard && jokerCount == 5) {
        counts.push_back(5);
    } else if (jokerIsWildcard) {
        counts[0] += jokerCount;
    }

    if (counts[0] == 5) {
        type = FIVE_OF_A_KIND;
    } else if (counts[0] == 4) {
        type = FOUR_OF_A_KIND;
    } else if (counts[0] == 3 && counts[1] == 2) {
        type = FULL_HOUSE;
    } else if (counts[0] == 3) {
        type = THREE_OF_A_KIND;
    } else if (counts[0] == 2 && counts[1] == 2) {
        type = TWO_PAIR;
    } else if (counts[0] == 2) {
        type = ONE_PAIR;
    }

    return type;
}

// Helper function: return hex representation of 'strength' of hand
int getHandStrength(std::vector<char> hand, bool jokerIsWildcard) {
    int strength = 0x00000000, charIndex;
    for (unsigned int i = 0; i < hand.size(); i++) {
        strength <<= 4;
        charIndex = -1;
        for (unsigned int j = 0; j < handValuesCount; j++) {
            if (hand[i] == handValues[j]) {
                charIndex = j;
                break;
            }
        }

        // Jokers are the weakest if they are treated as wildcards
        if (jokerIsWildcard && hand[i] == 'J') {
            charIndex = -2;
        }
        
        strength |= charIndex + 2;
    }

    strength |= getHandType(hand, jokerIsWildcard);
    return strength;
}

int main(int argc, char* argv[]) {
    std::string line, handChars, bid;
    std::ifstream file("day07.txt");
    std::vector<std::tuple<std::vector<char>, int, int>> hands;
    std::tuple<std::vector<char>, int, int> hand;
    std::vector<char> cards;
    std::stringstream sstream;
    char card;
    int part1Winnings, part2Winnings;

    if (file.is_open()) {
        while (std::getline(file, line)) {
            sstream.str(line);
            sstream >> handChars >> bid;
            cards.clear();
            for (unsigned int i = 0; i < handChars.length(); i++) {
                card = handChars[i];
                cards.push_back(card);
            }
            std::get<0>(hand) = cards;
            std::get<1>(hand) = getHandStrength(cards, false);
            std::get<2>(hand) = std::stoi(bid);
            hands.push_back(hand);
            sstream.clear();
        }
        std::sort(hands.begin(), hands.end(), 
            [](auto const& left, auto const& right) {
                return std::get<1>(left) < std::get<1>(right);
        });

        // Part 1
        part1Winnings = 0;
        for (unsigned int i = 0; i < hands.size(); i++) {
            part1Winnings += (i + 1) * std::get<2>(hands[i]);
        }
        std::cout << "Part 1: " << part1Winnings << std::endl;

        // Part 2
        part2Winnings = 0;
        for (unsigned int i = 0; i < hands.size(); i++) {
            std::get<1>(hands[i]) = getHandStrength(
                std::get<0>(hands[i]), true
            );
        }
        std::sort(hands.begin(), hands.end(), 
            [](auto const& left, auto const& right) {
                return std::get<1>(left) < std::get<1>(right);
        });
        for (unsigned int i = 0; i < hands.size(); i++) {
            part2Winnings += (i + 1) * std::get<2>(hands[i]);
        }
        std::cout << "Part 2: " << part2Winnings << std::endl;
    }

    return 0;
}
