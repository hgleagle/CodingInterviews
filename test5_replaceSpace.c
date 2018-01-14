/*
 * 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 方案1：拷贝到新创建的空间, 空间复杂度O(n) */
void replace_space1(char *str, int length)
{
    int i = 0;
    int j = 0;
    int new_len = length * 3;
    char *new_str;

    printf("%s\n", str);
    new_str = (char *)malloc(new_len);
    if (new_str == NULL) {
        exit(1);
    }
    memset(new_str, 0, new_len);

    while (i < length) {
        if (str[i] == ' ') {
            memcpy(new_str + j, "%20", 3);
            j += 3;
        } else {
            memcpy(new_str + j, str + i, 1);
            j += 1;
        }
        i++;
    }
    printf("%s\n", new_str);
    free(new_str);
}

/* 方案2：str已分配好足够空间，从后往前,空间复杂度更好 */
void replace_space2(char *str, int length)
{
    int i = 0;
    int j = 0;
    int new_len;
    int old_len = 0;
    int replace_num = 0;

    if (str == NULL || length <= 0) {
        return;
    }

    printf("%s\n", str);
    while (str[i] != '\0') {
        if (str[i] == ' ') {
            replace_num += 1;
        }
        i++;
        old_len++;
    }
    printf("%d %d\n", replace_num, old_len);

    new_len = old_len + replace_num * 2;
    if (new_len > length)
        return;

    i = old_len;
    j = new_len;
    while (i >= 0 && j > i) {
        printf("%s\n", str);
        if (str[i] == ' ') {
            str[j--] = '0';
            str[j--] = '2';
            str[j--] = '%';
        } else {
            str[j--] = str[i];
        }
        i--;
    }
    printf("%s\n", str);
}


int main(void)
{
    const int length = 100;
    char str[length] = "hello world";

    replace_space2(str, length);
}
