# Copyright (c) 2020 -- Élie Michel <elie.michel@telecom-paris.fr>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# The Software is provided “as is”, without warranty of any kind, express or
# implied, including but not limited to the warranties of merchantability,
# fitness for a particular purpose and non-infringement. In no event shall the
# authors or copyright holders be liable for any claim, damages or other
# liability, whether in an action of contract, tort or otherwise, arising
# from, out of or in connection with the software or the use or other dealings
# in the Software.

###############################################################################

# This dictionnary holds the list of OpenGL functions made depreciated, along
# with some help message displayed as a warning when using it.
depreciated_functions = {
	"glGenTextures": "Use glCreateTextures instead.",
	"glGenBuffers": "Use glCreateBuffers instead."
}

###############################################################################

MODERN_GLAD_BEGIN = """
/**
 * Wrapper around glad.h that flags most functions as depreciated (because they are).
 * by Elie Michel (c) 2020
 * Requires C++14 (for the [[depreciated]] attribute)
 */

#include <glad/glad.h>

#ifndef __modern_glad_h_
#define __modern_glad_h_

"""

MODERN_GLAD_END = """

#endif // __modern_glad_h_
"""

MODERN_GLAD_FUNCTION_TPL = """
#undef {0}
#define {0}(...) {{auto {0} [[deprecated("Not part of ModernGlad. {1}")]] = [](){{}}; {0}; }}
"""

###############################################################################

import os
import sys

def main():
	header_file = sys.argv[1]
	print("Generating ModernGLAD header at '{}'...".format(header_file))
	os.makedirs(os.path.dirname(header_file), exist_ok=True)

	with open(header_file, "w") as f:
		f.write(MODERN_GLAD_BEGIN)
		for func, reason in depreciated_functions.items():
			f.write(MODERN_GLAD_FUNCTION_TPL.format(func, reason))
		f.write(MODERN_GLAD_END)

if __name__ == "__main__":
	main()
