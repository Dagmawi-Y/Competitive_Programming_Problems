class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # Move forward history to the end of the current history list
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index = len(self.history) - 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]
