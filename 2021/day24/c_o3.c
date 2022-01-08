#include <stdio.h>

// FOLLOWING SOURCED FROM IDA FREEWARE DECOMPILER

int __cdecl main(int argc, const char** argv, const char** envp) {
    int v3; // eax
    int v4; // ebx
    int v5; // eax
    int v6; // er12
    int v7; // eax
    int v8; // ebp
    int v9; // eax
    int v10; // ebx
    int v11; // eax
    int v12; // ebx
    int v13; // eax
    int v14; // ebp
    int v15; // eax
    int v16; // ebx
    int v17; // eax
    int v18; // ebp
    int v19; // eax
    int v20; // ebx
    int v21; // eax
    int v22; // ebp
    int v23; // eax
    int v24; // ebx
    int v25; // eax
    int v26; // ebp
    int v27; // eax
    int v28; // ebx
    int v29; // eax

    v3 = getc(stdin);
    v4 = (v3 + 12) * (v3 != 14);
    v5 = getc(stdin);
    v6 = (v4 % 26 + 13 != v5) * (v5 + 6) + (25 * (v4 % 26 + 13 != v5) + 1) * v4;
    v7 = getc(stdin);
    v8 = (v6 % 26 + 12 != v7) * (v7 + 4) + (25 * (v6 % 26 + 12 != v7) + 1) * v6;
    v9 = getc(stdin);
    v10 = (v8 % 26 + 14 != v9) * (v9 + 5) + (25 * (v8 % 26 + 14 != v9) + 1) * v8;
    v11 = getc(stdin);
    v12 = v11 * (v10 % 26 + 13 != v11) + (25 * (v10 % 26 + 13 != v11) + 1) * v10;
    v13 = getc(stdin);
    v14 = (v13 + 4) * (v12 % 26 - 7 != v13) + v12 / 26 * (25 * (v12 % 26 - 7 != v13) + 1);
    v15 = getc(stdin);
    v16 = (v14 % 26 - 13 != v15) * (v15 + 15) + (25 * (v14 % 26 - 13 != v15) + 1) * (v14 / 26);
    v17 = getc(stdin);
    v18 = (v17 + 14) * (v16 % 26 + 10 != v17) + (25 * (v16 % 26 + 10 != v17) + 1) * v16;
    v19 = getc(stdin);
    v20 = (v18 % 26 - 7 != v19) * (v19 + 6) + (25 * (v18 % 26 - 7 != v19) + 1) * (v18 / 26);
    v21 = getc(stdin);
    v22 = (v21 + 14) * (v20 % 26 + 11 != v21) + (25 * (v20 % 26 + 11 != v21) + 1) * v20;
    v23 = getc(stdin);
    v24 = (v23 + 8) * (v22 % 26 - 9 != v23) + v22 / 26 * (25 * (v22 % 26 - 9 != v23) + 1);
    v25 = getc(stdin);
    v26 = (v25 + 5) * (v24 % 26 - 2 != v25) + v24 / 26 * (25 * (v24 % 26 - 2 != v25) + 1);
    v27 = getc(stdin);
    v28 = (v27 + 14) * (v26 % 26 - 9 != v27) + v26 / 26 * (25 * (v26 % 26 - 9 != v27) + 1);
    v29 = getc(stdin);
    _printf_chk(
        1LL,
        "z = %d",
        (v29 + 4) * (v28 % 26 - 14 != v29) + v28 / 26 * (25 * (unsigned int) (v28 % 26 - 14 != v29) + 1));
    return 0;
}
