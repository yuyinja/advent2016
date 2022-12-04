#include <stdio.h>
#include <stdlib.h>

void init_array(int *arr, int arr_max);
int binary_search(int *instr_arr, int max_instr, int instr_index, int arr_min, int arr_max);

int main(int argc, char *argv[])
{
    char *infile = argv[1];
    FILE* filePointer;
    int bufferLength = 255;
    char buffer[bufferLength];

    filePointer = fopen(infile, "r");

    // temporary malloc for id list...
    int *ids = calloc((128*8), sizeof(int));

    int row_max = 128;
    int rowInstr_num = 7;
    int col_max = 8;
    int colInstr_num = 3;
    int max_id = 0;

    while(fgets(buffer, bufferLength, filePointer)) {
        // printf("%s\n" , buffer);
        // initiate instruction arrays
        int *row_instruct = malloc(sizeof(int) * rowInstr_num);
        int *col_instruct = malloc(sizeof(int) * colInstr_num);
        for (int i = 0; i < rowInstr_num; ++i)
        {
            if (buffer[i] == 'B')
            {
                row_instruct[i] = 1;
            }
            else if (buffer[i] == 'F')
            {
                row_instruct[i] = -1;
            }
            // printf("%c %d, %d |", buffer[i], row_instruct[i], i);
        }
        for (int i = 0; i < colInstr_num; ++i)
        {
            if (buffer[i + 7] == 'R')
            {
                col_instruct[i] = 1;
            }
            else if (buffer[i + 7] == 'L')
            {
                col_instruct[i] = -1;
            }
        }
        int row_num = binary_search(row_instruct, rowInstr_num, 0, 0, row_max);
        int col_num = binary_search(col_instruct, colInstr_num, 0, 0, col_max);
        int id = (row_num * 8) + col_num;
        ids[id] = 1;
        if (id > max_id)
        {
            max_id = id;
        }
        // printf("Row: %d, Col: %d, id: %d\n", row_num, col_num, id);

        free(row_instruct);
        free(col_instruct);
    }

    printf("Max ID: %d\n", max_id);
    // realloc to go to max ids
    ids = realloc(ids, sizeof(int) * max_id+1);
    for (int i = 0; i < max_id+1; ++i)
    {
        if (ids[i] == 0)
        {
            if (ids[i+1] && ids[i-1])
            {
                printf("Your seat: %d \n", i);
            }
        }
    }

    free(ids);
    fclose(filePointer);

    return 0;
}

int binary_search(int *instr_arr, int max_instr, int instr_index, int arr_min, int arr_max)
{
    if (instr_index == (max_instr))
    {
        return arr_min;
    }
    else
    {
        int diff = ((arr_max - arr_min) / 2);
        if (instr_arr[instr_index] == -1)
        {
            arr_max = (arr_max - diff);
        }
        else if (instr_arr[instr_index] == 1)
        {
            arr_min = (arr_min + diff);
        }
        // printf("\nDebug: index: %d, instr: %d, max: %d, diff: %d, arr_min: %d, arr_max: %d\n", instr_index, instr_arr[instr_index], max_instr, diff, arr_min, arr_max);
        instr_index++;
        return binary_search(instr_arr, max_instr, instr_index, arr_min, arr_max);

    }
}
