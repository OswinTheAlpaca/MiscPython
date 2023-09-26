LEXEMES = r"""(?umx)

(?P<keywords>\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b) |

(?P<identifiers>\b([_a-zA-Z][_a-zA-Z0-9]*)\b) |

(?P<constants>\b((0(b|B)[01]+)|((0(x|X)[\da-fA-F]+)|(\d+))(([uU](ll|LL))|([lL](u|U)?))?)\b) |

(?P<strings>"([^"\\]|\\.)*"|'([^'\\]|\\.)*') |

(?P<symbols>[\{\}\[\]\(\)<>,;:\?\*=\/\+-]) |

(?P<operators>&|\||!|<<|>>|[!<>]=|[-+*/%=^~]+) |

(?P<spaces>\s+|\t+) |

(?P<comments>\/\*([^*]|\*[^\/])*\*\/|\/\/[^\n]*)
"""

