#include <fstream>
#include <iostream>
#include <string>

using namespace std;

struct stack {
	char value; // { [ } ] 등의 값을 받아들임
	stack* next; // 다음을 가리키는 포인터

};

struct Top {
	int count; // 
	struct stack* head; // 맨위를 head로 지정, head를 통해서만 stack에 접근 할 수 있음!
};

char pop(Top* top) {

	if (top->head->value == NULL) // value 값이 존재하지 않을 때
	{
		cout << "error" << '\n';
		return '\0'; // null 문자를 리턴함
	}

	char result = top->head->value;
	stack* temp = top->head;
	top->head = top->head->next;
	delete temp;

	top->count--;

	return result;
}


void push(char exp, Top* top) {

	stack* newStack = new stack();
	newStack->value = exp;

	newStack->next = top->head;
	top->head = newStack;
	
	top->count++;
}

bool MatchingParentheses(string ari_exp) {
	Top* top = new Top();
	top->count = 0;
	top->head = NULL; // 새로운 비교용 

	for (char ch : ari_exp)
	{
		if (ch == '[' or ch == '{' or ch == '(')
		{
			push(ch, top);
		}
		else if (ch == ']' or ch == '}' or ch == ')')
		{
			if (top->count == 0 or !top->head) {
				return false; // 비어있거나, 매칭하지 않음.
			}

			char pop_value = pop(top);

			if ((pop_value == '{' and ch == '}') or
				(pop_value == '[' and ch == ']') or
				(pop_value == '(' and ch == ')'))
			{
				
			}
			else
			{
				return false;
			}
		}
	}

	if (top->count != 0)
	{
		return false;
	}
	else
	{
		return true;
	}
	
}

int main()
{
    int number;
	string n;
    cin >> number;
    for (int i = 0; i<number; i++)
    {
        cin >> n;

	    if (MatchingParentheses(n) == true)
	    {
		    cout << "YES" <<'\n';
	    }
	    else
	    {
		    cout << "NO" <<'\n';
	    }
    }
	
}
