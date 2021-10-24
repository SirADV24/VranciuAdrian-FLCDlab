"""
    git link: 

    alphabetically binary search tree, both constants and identifers represented by the same st


    Code logic:
        
        1. Binary search tree structure
            Node class keep as data the name of the token && the position
            It has a left and a right node with the logic that left.data < self.data <= right.data ( if left && right exists )

        2. ST logic

            GetWrapper is just a wrapper of the get function ( for syntactic sugar )

            Get method will perform a classic tree search, returning the whole node if it founds it, -1 otherwise

            AddWrapper is just a wrapper of the add function ( for syntactic sugar )

            Add method will add the new value , dynamically calculating the position based on the type

                - first it checks if the root is null, if so it will create it ( creating the tree )
                - while current node data is not equal to the data we are trying to add || current node is not null 
                    we will search for the position of the new data in the tree 
"""