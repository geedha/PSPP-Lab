/*
 ============================================================================
 Name        : matrix.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int i,j,row,col;
	scanf("%d",&row);
	scanf("%d",&col);

	int mat1[row][col];
	int mat2[row][col];
	int sum[row][col];

	for(i=0;i<row;i++)
		for(j=0;j<col;j++)
		{
			scanf("%d",&mat1[i][j]);
		}

for(i=0;i<row;i++)
	for(j=0;j<col;j++)
	{
				scanf("%d",&mat2[i][j]);
	}
for (i = 0; i< row; i++)
{
      for (j = 0 ; j < col; j++) {
         sum[i][j] = mat1[i][j] + mat2[i][j];
         printf("%d\t", sum[i][j]);
      }
      printf("\n");
   }









	return EXIT_SUCCESS;
}
