#include <iostream>
#include <tuple>
#include <string>
#include <fstream>
#include <regex>
#include <vector>
#include <iterator> 
#include <stack>  

#define COMM std::tuple<std::string,int,int>
#define COMVEC std::vector<COMM>

// const std::regex re("(a-z){3} (\\d)+");
const std::regex re("^[a-z]{3} [\\+|\\-][\\d]+$");
const std::regex operation("^[a-z]{3}");
const std::regex number("[\\+|\\-][\\d]+$");

COMM smake_tuple(const std::string s1, const int s2)
{
    COMM tup = std::make_tuple(s1, s2, 0);
    return tup;
}

COMVEC read_c(std::string f)
{
    std::smatch sm;
    std::smatch sub1;
    std::smatch sub2;
    std::ifstream file(f);

    COMVEC commands;

    // std::ifstream file("input.txt");
    int len = 0;
    // Read all lines of the source file
    for (std::string line{}; std::getline(file, line);)
    {
        if(std::regex_match(line, sm, re))
        {
            const std::string str = sm[0];
            if(std::regex_search(str.begin(), str.end(), sub1, operation)) ;
            if(std::regex_search(str.begin(), str.end(), sub2, number)) ;
            COMM tup = smake_tuple(sub1[0], std::stod(sub2[0]));
            commands.push_back(tup);
        }
        len++;
    }

    return commands;
}

int part1(COMVEC& com, bool pp, char b, std::string f)
{
    int pc = 1;
    int acc = 0;
    int counter = 10;
    while(true)
    {
        for (auto i : com)
        {
            std::cout << std::get<0>(i) << std::get<1>(i) << std::get<2>(i) << std::endl;
        }
        std::cout << "-----------------------------" << std::endl;
        if (pp)
            std::cout << "pc: " << pc << std::endl;
        COMM vec = com[pc-1];
        if (pp)
            std::cout << std::get<0>(vec) << " +" << std::get<1>(vec) << " cnt:" << std::get<2>(vec) << std::endl;

        std::string command = std::get<0>(vec);
        if (command == "nop")
        {
            COMM& tup = com[pc-1];
            std::get<2>(tup) += 1; // already visited this command
            if (std::get<2>(tup) >= 2)
                break; // escape condition
            pc++;
            if (pc > com.size())
                return acc;
        }
        else if (command == "acc")
        {
            COMM& tup = com[pc-1];
            std::get<2>(tup) += 1; // already visited this command
            if (std::get<2>(tup) >= 2)
                break; // escape condition
            pc++;
            acc += std::get<1>(vec);
            if (pc > com.size())
                return acc;
        }
        else if (command == "jmp")
        {
            COMM& tup = com[pc-1];
            std::get<2>(tup) += 1; // already visited this command
            if (std::get<2>(tup) >= 2)
                break; // escape condition
            pc += std::get<1>(vec);
            if (pc > com.size())
                return acc;

        }
        if (pp) {
            std::cout << std::get<0>(com[pc]) << " --- " << std::get<1>(com[pc]) << std::endl;
            std::cout << std::get<0>(vec) << " +" << std::get<1>(vec) << " cnt:" << std::get<2>(vec) << std::endl;
            std::cout << "-----------------------" << std::endl;
        }
        if (b == 'b')
            if (counter-- == 0)
                break;
    }
    return acc;
}

int change_jmp(std::stack<int> &jmp_stack)
{
    int max_pc = -1;
    while(!jmp_stack.empty())
    {
        int pc = jmp_stack.top();
        jmp_stack.pop();
        if (pc > max_pc)
            max_pc = pc;
    }
    return max_pc;
}

int replay(int change, std::string f, bool pp, char b)
{
    COMVEC vec = read_c(f);
    COMM& tup = vec[change];
    std::cout << std::get<0>(tup) << std::endl;
    std::get<0>(tup) = "nop"; // already visited this command
    std::cout << std::get<0>(tup) << std::endl;
    return (part1(vec, pp, b, f));
}

int part2(COMVEC &com, bool pp, char b, std::string f)
{
    int pc = 1;
    int acc = 0;
    int counter = 10;
    std::stack<int> jmp_stack;
    while(true)
    {
        if (pp)
            std::cout << "pc: " << pc << std::endl;
        COMM vec = com[pc-1];
        if (pp)
            std::cout << std::get<0>(vec) << " +" << std::get<1>(vec) << " cnt:" << std::get<2>(vec) << std::endl;

        std::string command = std::get<0>(vec);
        if (command == "nop")
        {
            COMM& tup = com[pc-1];
            std::get<2>(tup) += 1; // already visited this command
            if (std::get<2>(tup) >= 2)
            {
                int chng = change_jmp(jmp_stack); // escape condition
                return replay(chng, f, pp, b);
            }
            pc++;
        }
        else if (command == "acc")
        {
            COMM& tup = com[pc-1];
            std::get<2>(tup) += 1; // already visited this command
            if (std::get<2>(tup) >= 2)
            {
                int chng = change_jmp(jmp_stack); // escape condition
                return replay(chng, f, pp, b);
            }
            pc++;
            acc += std::get<1>(vec);
        }
        else if (command == "jmp")
        {
            COMM& tup = com[pc-1];
            jmp_stack.push(pc-1);
            std::get<2>(tup) += 1; // already visited this command
            if (std::get<2>(tup) >= 2)
            {
                int chng = change_jmp(jmp_stack); // escape condition
                return replay(chng, f, pp, b);
            }

            pc += std::get<1>(vec);
        }
        if (pp) {
            std::cout << std::get<0>(com[pc]) << " --- " << std::get<1>(com[pc]) << std::endl;
            std::cout << std::get<0>(vec) << " +" << std::get<1>(vec) << " cnt:" << std::get<2>(vec) << std::endl;
            std::cout << "-----------------------" << std::endl;
        }
        if (b == 'b')
            if (counter-- == 0)
                break;
    }
    return acc;
}

int main(int argc, char** argv)
{
    COMVEC commands = read_c(argv[1]);

    bool pp = false;
    if (argc >= 3)
        if (*argv[2] == '1')
           pp = true;

    char b = 'a';
    if (argc >= 4)
        b = *argv[3];
    
    // int i = part1(commands, pp, b, argv[1]);
    // std::cout << "Part 1: " << i << std::endl;

    int i = part2(commands, pp, b, argv[1]);
    std::cout << "Part 2: " << i << std::endl;
    return 0;
}