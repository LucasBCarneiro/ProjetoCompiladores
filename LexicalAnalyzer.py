import re

class LexicalAnalyzer:
    lin_num = 1

    def tokenize(self, code):
        rules = [
            # Palavras Reservadas
            ("PRS01", r"integer"),
            ("PRS02", r"real"),
            ("PRS03", r"character"),
            ("PRS04", r"string"),
            ("PRS05", r"boolean"),
            ("PRS06", r"void"),
            ("PRS07", r"true"),
            ("PRS08", r"false"),
            ("PRS09", r"varType"),
            ("PRS10", r"funcType"),
            ("PRS11", r"paramType"),
            ("PRS12", r"declarations"),
            ("PRS13", r"endDeclarations"),
            ("PRS14", r"program"),
            ("PRS15", r"endProgram"),
            ("PRS16", r"functions"),
            ("PRS17", r"endFunctions"),
            ("PRS18", r"endFunction"),
            ("PRS19", r"return"),
            ("PRS20", r"if"),
            ("PRS21", r"else"),
            ("PRS22", r"endif"),
            ("PRS23", r"while"),
            ("PRS24", r"endWhile"),
            ("PRS25", r"break"),
            ("PRS26", r"print"),

            # Símbolos Reservados
            ("SRS01", r";"),
            ("SRS02", r","),
            ("SRS03", r":"),
            ("SRS04", r"="),
            ("SRS05", r"\?"),
            ("SRS06", r"\("),
            ("SRS07", r"\)"),
            ("SRS08", r"\{"),
            ("SRS09", r"\}"),
            ("SRS10", r"\["),
            ("SRS11", r"\]"),
            ("SRS12", r"\+"),
            ("SRS13", r"-"),
            ("SRS14", r"\*"),
            ("SRS15", r"/"),
            ("SRS16", r"%"),
            ("SRS17", r"=="),
            ("SRS18", r"!=|#"),
            ("SRS19", r"<"),
            ("SRS20", r"<="),
            ("SRS21", r">"),
            ("SRS22", r">="),

            # Identificadores e Constantes
            ("IDN01", r"[a-zA-Z][a-zA-Z0-9]*"),     # programName
            ("IDN02", r"[a-zA-Z_][a-zA-Z0-9_]*" ),     # variable
            ("IDN03", r"[a-zA-Z_][a-zA-Z0-9_]*"),     # functionName
            ("IDN04", r"\d+"),                        # intConst
            ("IDN05", r"\d+\.\d+([eE][+-]?\d+)?"),     # realConst
            ("IDN06", r"\".*?\""),                    # stringConst
            ("IDN07", r"'.'"),                        # charConst

            # Outros
            ("NOVALINHA", r"\n"),
            ("PULAR", r"[ \t]+"),
            ("OUTROCHAR", r"."),  # caractere inválido
        ]


        tokens_join = "|".join("(?P<%s>%s)" % x for x in rules)
        lin_start = 0

        # Listas de saída
        token = []
        lexeme = []
        row = []
        column = []

        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == "NOVALINHA":
                lin_start = m.end()
                self.lin_num += 1
            elif token_type == "PULAR":
                continue
            elif token_type == "OUTROCHAR":
                print("%r não esperado na linha %d" % (token_lexeme, self.lin_num))
            else:
                col = m.start() - lin_start
                column.append(col)
                token.append(token_type)
                lexeme.append(token_lexeme)
                row.append(self.lin_num)

        return token, lexeme, row, column
