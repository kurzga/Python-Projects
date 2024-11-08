import matplotlib.pyplot as plt

def odd_even(num):
    return num % 2

def collatz_sequence(num):
    sequence = [num]
    while num != 1:
        if odd_even(num) == 0:
            num //= 2
        else:
            num = 3 * num + 1
        sequence.append(num)
    return sequence

# Main script
if __name__ == "__main__":
    start = int(input("Başlangıç sayısını girin: "))
    end = int(input("Bitiş sayısını girin: "))
    
    plt.figure(figsize=(14, 8))
    
    for number in range(start, end + 1):
        sequence = collatz_sequence(number)
        plt.plot(range(len(sequence)), sequence, marker='o', linestyle='-', label=f'{number}')
    
    plt.xlabel('Adım')
    plt.ylabel('Değer')
    plt.title(f'{start} ile {end} Arasındaki Sayıların Collatz Dizileri')
    plt.grid(True)
    plt.legend()
    plt.show()