# TypeScript Hello World!

## 1. Create the `hello.ts` file

Let's create a file called `hello.ts` with the following contents:

```typescript
function greet(): void {
  console.log("HELLO TYPESCRIPT!");
}

greet();
```

## 2. Compile the TypeScript file

We then compile the TypeScript file using the tsc command:
```
tsc hello.ts
```

## 3. Verify the generated files
If you run ls in your repo, you'll see two files: one for TypeScript (hello.ts) and the other for JavaScript (hello.js):``
ls
``

## 4. Run the JavaScript file
Finally, run the generated JavaScript file using node:
```bash
node hello.js
```

## Output
```
HELLO TYPESCRIPT!
```
