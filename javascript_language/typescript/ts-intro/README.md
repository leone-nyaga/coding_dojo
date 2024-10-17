#TypeScript Hello World!

+ Let's create a file called "hello.ts"
+ The contents of the file are:
```typescript
function greet(): void {
  console.log("HELLO TYPESCRIPT!");
}

greet();

+ we then compile the typescript file:
tsc hello.ts
+ this will convert the typescrit file to a javascript file.
+ if you ls into your repo, you'll see two files one for ts and the other for js.
+ run ```node hello.js``` for the output:
```HELLO TYPESCRIPT!
