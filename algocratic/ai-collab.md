# AI Collaboration Guide

## Ontological Studies Division — Working With AI Tools

-----

> *“AI tools are collaborators, not replacements. They extend your capabilities; they don’t substitute for your understanding.”*

-----

## The AlgoCratic Position on AI

At AlgoCratic Futures, we expect employees to leverage every available tool—including AI. However, we measure success by **what you understand and can do**, not by what an AI produced for you.

The goal: **Use AI to accelerate learning, not bypass it.**

-----

## Approved Usage Patterns

### Pattern 1: Operational Definition → Implementation

You provide the “what.” AI helps with the “how.”

```
YOU:  "A stack is a collection where the last element added is the 
       first removed. Help me design a class that implements this."

AI:   [Provides implementation guidance]

YOU:  [Modify, extend, and demonstrate you understand it]
```

**What makes this good:**

- You defined the concept (shows understanding)
- You’re asking for implementation guidance, not copy-paste code
- You still have to understand and modify the result

**Red flag version:**

```
"Write me a stack class in Python"
[Copy-paste without reading]
[Submit]
```

-----

### Pattern 2: Translation Support

You have working code in one language. You want to understand the equivalent in another.

```
YOU:  "Here's my working Python stack implementation. Help me 
       understand what needs to change for C++. I'm confused 
       about how to handle the memory."

AI:   [Explains memory management, pointer vs reference, etc.]

YOU:  [Implement the C++ version, explaining the differences]
```

**What makes this good:**

- You already solved it once (proves capability)
- You’re asking to *understand*, not just *get* the translation
- You identify what confuses you specifically

**Red flag version:**

```
"Convert this Python code to C++"
[Accept output without understanding why it changed]
```

-----

### Pattern 3: Debugging Assistance

Something’s broken. You need help diagnosing.

```
YOU:  "My circular queue works in Python but crashes in C++ when 
       I try to enqueue after wrapping around. Here's both 
       implementations. The crash happens at line 42. I think 
       it's a pointer issue but I'm not sure."

AI:   [Helps identify the issue, explains the underlying problem]

YOU:  [Fix it yourself, document what you learned]
```

**What makes this good:**

- You described the problem specifically
- You showed what you already tried
- You hypothesized a cause
- You’ll fix it yourself after understanding

**Red flag version:**

```
"Fix this code, it doesn't work"
[Accept fix without understanding why it was broken]
```

-----

### Pattern 4: Concept Exploration

You want to understand something more deeply.

```
YOU:  "I implemented a BST and noticed that if I insert values 
       in sorted order, the tree becomes a line. Why does this 
       happen, and what are the consequences?"

AI:   [Explains tree balance, performance degradation, etc.]

YOU:  [Document understanding, experiment to verify]
```

**What makes this good:**

- You observed something through your own work
- You’re asking “why” not “how”
- You’ll verify understanding through experimentation

-----

### Pattern 5: Visualization Development

Multi-phase prompting to create visualizations.

```
PHASE 1:
YOU:  "I want to visualize a circular queue showing the buffer, 
       front pointer, and rear pointer. What information should 
       I display at each step?"

AI:   [Suggests visualization elements]

PHASE 2:
YOU:  "Based on that, here's my plan: [your design]. What Python 
       library would be simplest for this kind of text-based 
       visualization?"

AI:   [Suggests approach]

PHASE 3:
YOU:  [Implement it, compare with existing tools, document insights]
```

**What makes this good:**

- You’re driving the design decisions
- Multi-phase shows iteration and thought
- You’re not asking AI to build the whole thing

-----

## Documentation Requirements

For every mission, maintain `/docs/ai-log.md`:

```markdown
# AI Collaboration Log

## Session 1: [Date]

### Prompt:
[What you asked]

### Response Summary:
[Key points from AI response - don't paste the whole thing]

### What I Learned:
[Genuine insight, not just "it gave me code"]

### What I Changed:
[How you modified or built upon the AI's suggestion]

---

## Session 2: [Date]
...
```

-----

## What Demonstrates Understanding

We’re not measuring “did you use AI”—we’re measuring “do you understand.”

**Evidence of understanding:**

- You can explain your code without looking at it
- You can predict what will happen before running
- You can modify the code to do something slightly different
- You can identify what the AI got wrong
- You can teach it to someone else

**Evidence of copy-paste without understanding:**

- You can’t explain why something works
- You’re surprised by the behavior
- You can’t fix it when it breaks
- Your AI log is empty or vague

-----

## Prohibited Uses

These will result in mission failure:

1. **Asking AI to complete entire missions**
- “Write me a complete circular queue implementation with tests”
1. **Submitting AI output without modification or understanding**
- Copy-paste code you can’t explain
1. **Using AI to bypass learning**
- Getting answers without engaging with the problem first
1. **Lying in your AI log**
- Claiming you didn’t use AI when you did
- Fake documentation of “learning”

-----

## Ethical Framing

AI tools are like calculators in math class:

- Calculators can do arithmetic faster than you
- But if you don’t understand arithmetic, you can’t check if the calculator is right
- And you can’t do anything the calculator wasn’t designed for

Similarly:

- AI can generate code faster than you
- But if you don’t understand the code, you can’t verify it’s correct
- And you can’t solve problems the AI wasn’t trained on

**Your job is to understand.** AI is a tool that helps you get there faster—if you use it right.

-----

## Sample Good vs Bad Prompts

### For Stack Implementation

**Good:**

- “I want to implement a stack using an array. Should my top index point to the top element, or to the next empty slot? What are the tradeoffs?”
- “My pop function returns garbage in C++. Here’s my code. I think I might be returning after deleting, but I’m not sure.”

**Bad:**

- “Write a stack class”
- “Fix my code” [with no context]

### For BST Implementation

**Good:**

- “I’m trying to insert into a BST recursively, but I’m having trouble with the base case. The node I create doesn’t stay attached to the tree. Here’s my function…”
- “Why do I need to pass the node pointer by reference in C++? My insert works if I use `BSTNode*&` but not with just `BSTNode*`.”

**Bad:**

- “Write a BST with insert and search”
- “I don’t understand trees, explain everything”

### For Debugging

**Good:**

- “My circular queue reports ‘full’ immediately after initialization. Here’s my isFull function. I’m using front == rear to detect full, but I wonder if that’s also true when empty?”

**Bad:**

- “Why doesn’t this work” [paste code with no description]

-----

## Remember

Every professional developer uses AI tools. The ones who succeed are those who:

1. **Know what they’re asking for** (clear problem definition)
1. **Verify the output** (don’t trust blindly)
1. **Understand what they use** (can explain and modify)
1. **Learn from the interaction** (each use builds knowledge)

AI makes you faster. Understanding makes you capable.

-----

*AlgoCratic Futures — Tools Extend Capability, They Don’t Replace It*