#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* convert(char *s, int num_rows);
void assertEquals(char *expected, char *actually);

char *temp;

int main() {
	
	char* c = convert("PAYPALISHIRING", 3); // len is 14
	printf("\n[Debug] c: {%s}", c);
	//assertEquals("PAHNAPLSIIGYIR", c);
	free(c);
	
	/*
	char* c2 = convert("ABC", 3);
	assertEquals("ABC", c2);
	
	char* c3 = convert("ABCDEF", 3);
	assertEquals("AEBDFC", c3);
	* */
	
	//char* c4 = convert("ABCDEF", 3);
	//printf("\n--%s--", c4);
}

char* convert(char *s, int numRows){
	
	int i, len = (int)strlen(s), index = 0;
	
	if (len == numRows) return s; // if its same size, return
	
	int top_bottom_interval;
	
	if (numRows % 2 == 0){
		top_bottom_interval = numRows + 2;
	} else {
		top_bottom_interval = numRows + 1;
	}
	
	int other_interval = numRows - 1;
	
	char converted_string[len + 1]; // adding 1 to length to make room for null char
	int c_s_index = 0, z_start_index = 1, z_index = 1;
	
	
	for (i = 0; i < numRows; i++){
		if (i == 0 || i == numRows - 1) { // top part
			index = i;
			while (index < len){
				converted_string[c_s_index++] = s[index];
				//printf("[Debug] %c", s[index]);
				index += top_bottom_interval;
				
			}
		} else {
			index = i;
			z_index = z_start_index;
			while (index < len){
				converted_string[c_s_index++] = s[index];
				if (index == z_index && numRows > 3){
					index += numRows;
					z_index = index + other_interval;
				} else {
					index += other_interval;
				}
				//printf("\n[Debug] index: {%i}", index);
			}
			z_start_index += other_interval + 1;
			//printf("\n[Debug] z_start_index: {%i}", z_start_index);
		}
	}
	
	converted_string[len] = '\0';
	char *c = malloc(100 * sizeof(char));
	if (c == NULL) {
		printf("\n[Error] c is null");
		return NULL;
	} else {
		printf("\n[Debug] size of c: {%lu}", sizeof(c));
	}
	
	index = 0;
	//while (*c++ = converted_string[index++]) ;
	*c = converted_string[0];
	return c;
}

void assertEquals(char *expected, char *actually){
	int c_comp = 0;//strcmp(expected, actually);
	printf("[Debug] actually {%s}", actually);
	//printf("\n[Test] Expected: --%s-- Actual: --%s-- Result: --%s--", expected, actually, c_comp == 0 ? "Passed" : "Failed");
}
