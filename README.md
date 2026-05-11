The contents of the python file is written to indicate 
code smells
duplicated code
poor variable naming
bad practices
maintainability issues.
Why this code is intentionally bad

This code contains several quality problems:
| Problem               | Example                    |
| --------------------- | -------------------------- |
| Poor variable names   | `a`, `b`, `x1`, `x2`       |
| Duplicate code        | repeated `predict()`       |
| Hardcoded secret      | `password = "admin123"`    |
| Unused variable       | `unused_variable`          |
| Redundant assignments | `x1=a`, `x2=a`             |
| Weak structure        | everything in global scope |
| Meaningless condition | same output in if/else     |

SonarCloud should flag many of these.
