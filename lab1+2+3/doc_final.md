Logic:
    1.Regex:
        - we used regex to find the patterns of identifiers/constants. For proof go to regex_proof

    2.Tokens split:
        we used the following logic in splitting the tokens:
         if we want to split a string by another ( i.e. split the following text by "," "Ana, are, mere" ) but also keeping the separators ( in our case "," ) we will replace the separator with DEFAULTseparatorDEFAULT and then split by DEFAULT

         example: separator : ",", string: "Ana, are, mere"
            -> "AnaDEFAULT,DEFAULT areDEFAULT,DEFAULT mere"
            after splitting the resulted string by DEFAULT we will get:
                ["Ana", ",", "are", ",", "mere"]


        we split first by separators, then every result is splitted by operators

        Note: this works for cases like "b*b-4*a*c" like in p2.txt

        Note: for this logic the order of the tokens in tokens.txt matters

    
    3. To form the PIF i used the course algorythm

        if token is reserved word OR separator OR operator
            addToPif(token, -1)
        else if token is identifier or Constant:
            pos = symbolTable.add(token)
            addToPif(token, pos)
        else
            error