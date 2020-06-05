#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    start_at = list(
        filter(lambda t: t[1].source == "NONE", enumerate(tickets)))[0]
    end_at = list(
        filter(lambda t: t[1].destination == "NONE", enumerate(tickets)))[0]

    def filter_next(ticket):
        return list(filter(lambda t: t[1].source == ticket.destination, enumerate(tickets)))[0]
    airport = start_at
    while airport != end_at:
        if airport[1].source != "NONE":
            route.append(airport[1].source)
        airport = filter_next(airport[1])
    route.append(airport[1].source)
    route.append(end_at[1].destination)
    return route


if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    expected = ["PDX", "DCA", "NONE"]
    result = reconstruct_trip(tickets, 3)
    print(expected)
    print(result)
