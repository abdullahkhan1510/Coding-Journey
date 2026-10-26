def enqueue(queue, item):
    queue.append(item)


def dequeue(queue):
    if len(queue) > 0:
        return queue.pop(0)
    return None


def main():
    queue = []

    enqueue(queue, "Alice")
    enqueue(queue, "Bob")
    enqueue(queue, "Charlie")

    print(queue)
    print(dequeue(queue))
    print(queue)


if __name__ == "__main__":
    main()