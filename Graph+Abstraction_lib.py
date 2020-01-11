#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 01:17:26 2020

@author: Justice_Roy
"""
#CONSTANTS
DEFAULT_BACKGROUND = "background.jpg"
DEFAULT_FONT = "font.tff"
DEFAULT_PROBLEM_BACKGROUND = "problem_background.jpg"
DEFAULT_PROBLEM_FONT = "problem_font.jpg"
class Digraph:
    #We initialise with the first node
    def __init__(self, node):
        self.edges = {}
        self.edges[node] = []
        self.current_node = node
    
    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    
    def add_edge(self, source, destination):
        if (source not in self.edges) or (destination not in self.edges):
            raise ValueError('Node not in graph')
        self.edges[source].append(destination)
        
    def next_nodes(self, node):
        return self.edges[node]
    
    def traverse_node(self, node):
        self.current_node = node
        
    def __repr__(self):
        return f"{self.edges}"

class Node:
    ''' Nodes represented by a unique id for the score, meant as a base class 
    for the three types'''
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f"{self.id} : {self.name}"

class Message(Node):
    def __init__(self, id, name, text, background = DEFAULT_BACKGROUND, font = DEFAULT_FONT):
        Node.__init__(self, id, name)
        self.text = text
        self.background = background
        self.font = font
        
class Problem(Node):
    #Remember to implement failure building in your graph building script
    def __init__(self, id, name, question, answer, failure_node = False, 
                 background = DEFAULT_PROBLEM_BACKGROUND, font = DEFAULT_PROBLEM_FONT):
        #Failure refers to the possibility of failure, not whether one occurred.
        Node._init__(self, id, name)
        self.question = question
        self.answer = answer
        self.background = background
        self.font = font
        self.failure_node = failure_node

#Consider implementing name as the choice button name and the text showing below it.    
class Choice(Node):
    def __init__(self, id, name, text, *choices):
        Node.__init__(self, id, name)
        self.name = name
        self.text = text
        self.num_choices = len(choices)
        self.choices = choices
                  
def game_execute():
    """Function which traverses the graph after initial setup, i.e., 
    goes through the scenes"""
    global game_graph
    while True:
       
        score_sequence_append(game_graph.current_node.id)
        
        #TODO Implement ending
        
        ##Choice Nodes make this easier, so we'll have them
        node_call = {'Message' : message_wrapper,
                     'Problem' : problem_wrapper,
                     'Choice' : choice_wrapper,
                     }
        #Calls the correct function using the name of current_node's class
        node_class = (type(game_graph.current_node)).__name__
        node_call[node_class]()
        
        
#TODO Implement problem(), message(), choice()
def problem(question, answer, failure, background, font):
    pass

def message(text, background, font):
    pass

#You may consider implementing the choice arguments as args
def choice(text, num_choices, choice1, choice2, choice3 = None):
    
    return chosen_node
        
#All the wrapper functions call their corresponding functions with the right
#arguments, while changing the sate of the program and keeping score.
#TODO Bring all calls of the corresponding functions inside their wrappers in
#line with Rishab's implementation
def message_wrapper():
    global game_graph
    message_ = game_graph.current_node
    message(message_.text, message_.background, message_.font)
    next_node = game_graph.edges[message_][0]
    game_graph.traverse_node(next_node)
    
def problem_wrapper():
    global game_graph
    global head_roll_count
    problem_ = game_graph.current_node
    problem_result = problem(problem_.question, problem_.answer, problem._failure_node
                             problem_.background, problem_.font)
    
    if problem_result == "Failure":
        head_roll_count += 1
        score_sequence_append('F')
        next_node = game_graph.current_node.failure_node
    elif problem_result == "Success":
        next_node = game_graph.edges[game_graph.current_node][0]
    game_graph.traverse_node(next_node)

def choice_wrapper():
    global game_graph
    choice_ = game_graph.current_node
    choice_node = choice(choice_.text, choice_.num_choices, *choice_.choices)
    game_graph.traverse_node(choice_node)
 
    
#TODO Implement score sequence storing
def score_sequence_append():
    pass

###Globals
head_roll_count = 0
#TODO Implement Graph Creating Script
game_graph = None


###Tests:
# =============================================================================
# a = Message("M1", "start_message", "This si the first message")
# b = Message("M2", "second_message", "This is the second message")
# d = Digraph(a)
# d.add_node(b)
# d.add_edge(a, b)
# game_graph = d
# #message_wrapper()
# =============================================================================

