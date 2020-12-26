#!/usr/bin/env ruby
require 'set'

def top_sort(graph)
  edge_count = Array.new(graph.length, 0)
  process = Set.new
  seen = Set.new
  order = []

  graph.each do |node|
    node.edges.each do |edge|
      edge_count[edge] += 1
    end
  end

  (0..edge_count.length-1).each do |i|
    if edge_count[i] == 0
      process.add(graph[i])
    end
  end

  while process.length != 0
    new_process = Set.new
    process.each do |cur_node|
      order.append(cur_node)
      seen.add(cur_node)
      cur_node.edges.each do |edge|
        edge_count[edge] -= 1
        if edge_count[edge] == 0 and not seen === graph[edge]
          new_process.add(graph[edge])
        end
      end
    end
    process = new_process
  end

  return order
end

class Node
  attr_accessor :value, :edges

  def initialize(value, edges=[])
    @value = value
    @edges = edges
  end
end

if __FILE__ == $0
  graph = [Node.new(2),
           Node.new(3, [4, 6]),
           Node.new(5, [7]),
           Node.new(7, [4, 7]),
           Node.new(8, [5]),
           Node.new(9),
           Node.new(10),
           Node.new(11, [0, 5, 6]),
          ]
  order = top_sort(graph).map{ |node| node.value}
  p "Order: #{order}"
end
