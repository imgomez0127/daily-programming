(*
 This creates a node where the
 structure of the node is
 char Key
 'a option Value
 bool isEnd
 node list Children
 *)
type 'a trie = Node of char * 'a option * bool * 'a trie list

let null_char = '\x00'

let explode (str : string) : char list =
  let rec explode_inner cur_index chars =
    if cur_index < String.length str then
      let new_char = str.[cur_index] in
      explode_inner (cur_index+1) (chars@[new_char])
    else chars in
  explode_inner 0 []

let rec insert (x:'a trie) (chars:char list) (value:'a) : 'a trie =
  (match chars with
  | [] -> let Node(c, _, _, children) = x in Node(c, Some(value), true, children)
  | c::cs ->
    (let Node(c1, v, b, children) = x in
     let next_node_opt = (List.find_opt
                            (fun n -> let Node(c2, _, _, _) = n in c = c2)
                            children
                         ) in
     let next_node =
       (match next_node_opt with
        | Some(n) -> n
        | None -> Node(c, None, false, [])
       ) in
     let modified_children = (List.filter
                                (fun n -> let Node(c2, _, _, _) = n in c <> c2)
                                children
                             ) in
     Node(c1, v, b, (insert next_node cs value)::modified_children)
    )
  )

let rec search (x:'a trie) (chars:char list) : 'a option =
  (match chars with
   | [] -> let Node(_, v, b, _) = x in
     if b == false
     then None
     else v
   | c::cs ->
     (let Node(_, _, _, children) = x in
      let next_node_opt = (List.find_opt
                             (fun n -> let Node(c2, _, _, _) = n in c = c2)
                             children
                          ) in
      (match next_node_opt with
       | Some(n) -> (search n cs)
       | None -> None
      ))
  )

let root = Node(null_char, None, false, [])
