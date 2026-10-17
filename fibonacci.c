
int main() {
    int n = 10, i, a = 0, b = 1, next;
printf("Fibonacci Series: ");
    for(i = 0; i < n; i++) {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
    return 0;
}
