import read_MNIST_Class, os

def main():
    mnist = read_MNIST_Class.read_MNIST()
    a = int(input("Negative Digit :"))
    b = int(input("Positive Digit :"))
    X = mnist.load_mnist('training', digits=[a,b])
    print(X)
    mnist.printPlot(X)
    print(os.getcwd())


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()