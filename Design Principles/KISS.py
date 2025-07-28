'''

The KISS principle, which stands for "Keep It Simple, Stupid" (some variations use "Keep It Short and Simple" or "Keep It Super Simple"), is a design principle that suggests simplicity should be a key goal in design, development, and other fields, such as engineering, software development, and user interface design. The principle advocates for simplicity in systems, processes, and products, aiming to minimize complexity and make things easier to understand and use.

'''
# ❌ Over‑engineered: nested loops to square numbers
def squares_bad(nums):
    res = []
    for n in nums:
        res.append(n * n)
    return res

# ✅ KISS: use list comprehension
def squares(nums):
    return [n * n for n in nums]
