# https://www.typescriptlang.org/

## TypeScript: Documentation - TypeScript 5.3

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-3.html)

Was this page helpful?

# TypeScript 5\.3

## Import Attributes

TypeScript 5\.3 supports the latest updates to the [import attributes](https://github.com/tc39/proposal-import-attributes) proposal.

One use\-case of import attributes is to provide information about the expected format of a module to the runtime.

\`\`\`
// We only want this to be interpreted as JSON,// not a runnable/malicious JavaScript file with a \`.json\` extension.import obj from "./something.json" with { type: "json" };
\`\`\`
The contents of these attributes are not checked by TypeScript since they’re host\-specific, and are simply left alone so that browsers and runtimes can handle them (and possibly error).

\`\`\`
// TypeScript is fine with this.// But your browser? Probably not.import \* as foo from "./foo.js" with { type: "fluffy bunny" };
\`\`\`
Dynamic `import()` calls can also use import attributes through a second argument.

\`\`\`
const obj = await import("./something.json", { with: { type: "json" }});
\`\`\`
The expected type of that second argument is defined by a type called `ImportCallOptions`, which by default just expects a property called `with`.

Note that import attributes are an evolution of an earlier proposal called [“import assertions”, which were implemented in TypeScript 4\.5](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5/#import-assertions).
The most obvious difference is the use of the `with` keyword over the `assert` keyword.
But the less\-visible difference is that runtimes are now free to use attributes to guide the resolution and interpretation of import paths, whereas import assertions could only assert some characteristics after loading a module.

Over time, TypeScript will be deprecating the old syntax for import assertions in favor of the proposed syntax for import attributes.
Existing code using `assert` should migrate towards the `with` keyword.
New code that needs an import attribute should use `with` exclusively.

We’d like to thank [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) for [implementing this proposal](https://github.com/microsoft/TypeScript/pull/54242)!
And we’d also like to call out [Wenlu Wang](https://github.com/Kingwl) for their implementation of [import assertions](https://github.com/microsoft/TypeScript/pull/40698)!

## Stable Support `resolution-mode` in Import Types

In TypeScript 4\.7, TypeScript added support for a `resolution-mode` attribute in `/// ` to control whether a specifier should be resolved via `import` or `require` semantics.

\`\`\`
/// \// or/// \
\`\`\`
A corresponding field was added to import assertions on type\-only imports as well;
however, it was only supported in nightly versions of TypeScript.
The rationale was that in spirit, import *assertions* were not intended to guide module resolution.
So this feature was shipped experimentally in a nightly\-only mode to get more feedback.

But given that *[import attributes](#import-attributes)* can guide resolution, and that we’ve seen reasonable use\-cases, TypeScript 5\.3 now supports the `resolution-mode` attribute for `import type`.

\`\`\`
// Resolve \`pkg\` as if we were importing with a \`require()\`import type { TypeFromRequire } from "pkg" with { "resolution\-mode": "require"};// Resolve \`pkg\` as if we were importing with an \`import\`import type { TypeFromImport } from "pkg" with { "resolution\-mode": "import"};export interface MergedType extends TypeFromRequire, TypeFromImport {}
\`\`\`
These import attributes can also be used on `import()` types.

\`\`\`
export type TypeFromRequire = import("pkg", { with: { "resolution\-mode": "require" } }).TypeFromRequire;export type TypeFromImport = import("pkg", { with: { "resolution\-mode": "import" } }).TypeFromImport;export interface MergedType extends TypeFromRequire, TypeFromImport {}
\`\`\`
For more information, [check out the change here](https://github.com/microsoft/TypeScript/pull/55725)

## `resolution-mode` Supported in All Module Modes

Previously, using `resolution-mode` was only allowed under the `moduleResolution` options `node16` and `nodenext`.
To make it easier to look up modules specifically for type purposes, `resolution-mode` now works appropriately in all other `moduleResolution` options like `bundler`, `node10`, and simply doesn’t error under `classic`.

For more information, [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/55725).

## `switch (true)` Narrowing

TypeScript 5\.3 now can perform narrowing based on conditions in each `case` clause within a `switch (true)`.

\`\`\`
function f(x: unknown) { switch (true) { case typeof x === "string": // 'x' is a 'string' here console.log(x.toUpperCase()); // falls through... case Array.isArray(x): // 'x' is a 'string \| any\[]' here. console.log(x.length); // falls through... default: // 'x' is 'unknown' here. // ... }}
\`\`\`
[This feature](https://github.com/microsoft/TypeScript/pull/55991) was spearheaded [initial work](https://github.com/microsoft/TypeScript/pull/53681) by [Mateusz Burzyński](https://github.com/Andarist)
We’d like to extend a “thank you!” for this contribution.

## Narrowing On Comparisons to Booleans

Occasionally you may find yourself performing a direct comparison with `true` or `false` in a condition.
Usually these are unnecessary comparisons, but you might prefer it as a point of style, or to avoid certain issues around JavaScript truthiness.
Regardless, previously TypeScript just didn’t recognize such forms when performing narrowing.

TypeScript 5\.3 now keeps up and understands these expressions when narrowing variables.

\`\`\`
interface A { a: string;}interface B { b: string;}type MyType = A \| B;function isA(x: MyType): x is A { return "a" in x;}function someFn(x: MyType) { if (isA(x) === true) { console.log(x.a); // works! }}
\`\`\`
We’d like to thank [Mateusz Burzyński](https://github.com/Andarist) for [the pull request](https://github.com/microsoft/TypeScript/pull/53681) that implemented this.

## `instanceof` Narrowing Through `Symbol.hasInstance`

A slightly esoteric feature of JavaScript is that it is possible to override the behavior of the `instanceof` operator.
To do so, the value on the right side of the `instanceof` operator needs to have a specific method named by `Symbol.hasInstance`.

\`\`\`
class Weirdo { static \[Symbol.hasInstance](testedValue) { // wait, what? return testedValue === undefined; }}// falseconsole.log(new Thing() instanceof Weirdo);// trueconsole.log(undefined instanceof Weirdo);
\`\`\`
To better model this behavior in `instanceof`, TypeScript now checks if such a `[Symbol.hasInstance]` method exists and is declared as a type predicate function.
If it does, the tested value on the left side of the `instanceof` operator will be narrowed appropriately by that type predicate.

\`\`\`
interface PointLike { x: number; y: number;}class Point implements PointLike { x: number; y: number; constructor(x: number, y: number) { this.x = x; this.y = y; } distanceFromOrigin() { return Math.sqrt(this.x \*\* 2 \+ this.y \*\* 2\); } static \[Symbol.hasInstance](val: unknown): val is PointLike { return !!val \&\& typeof val === "object" \&\& "x" in val \&\& "y" in val \&\& typeof val.x === "number" \&\& typeof val.y === "number"; }}function f(value: unknown) { if (value instanceof Point) { // Can access both of these \- correct! value.x; value.y; // Can't access this \- we have a 'PointLike', // but we don't \*actually\* have a 'Point'. value.distanceFromOrigin(); }}
\`\`\`
As you can see in this example, `Point` defines its own `[Symbol.hasInstance]` method.
It actually acts as a custom type guard over a separate type called `PointLike`.
In the function `f`, we were able to narrow `value` down to a `PointLike` with `instanceof`, but *not* a `Point`.
That means that we can access the properties `x` and `y`, but not the method `distanceFromOrigin`.

For more information, you can [read up on this change here](https://github.com/microsoft/TypeScript/pull/55052).

## Checks for `super` Property Accesses on Instance Fields

In JavaScript, it’s possible to access a declaration in a base class through the `super` keyword.

\`\`\`
class Base { someMethod() { console.log("Base method called!"); }}class Derived extends Base { someMethod() { console.log("Derived method called!"); super.someMethod(); }}new Derived().someMethod();// Prints:// Derived method called!// Base method called!
\`\`\`
This is different from writing something like `this.someMethod()`, since that could invoke an overridden method.
This is a subtle distinction, made more subtle by the fact that often the two can be interchangeable if a declaration is never overridden at all.

\`\`\`
class Base { someMethod() { console.log("someMethod called!"); }}class Derived extends Base { someOtherMethod() { // These act identically. this.someMethod(); super.someMethod(); }}new Derived().someOtherMethod();// Prints:// someMethod called!// someMethod called!
\`\`\`
The problem is using them interchangeably is that `super` only works on members declared on the prototype — *not* instance properties.
That means that if you wrote `super.someMethod()`, but `someMethod` was defined as a field, you’d get a runtime error!

\`\`\`
class Base { someMethod = () =\> { console.log("someMethod called!"); }}class Derived extends Base { someOtherMethod() { super.someMethod(); }}new Derived().someOtherMethod();// 💥// Doesn't work because 'super.someMethod' is 'undefined'.
\`\`\`
TypeScript 5\.3 now more\-closely inspects `super` property accesses/method calls to see if they correspond to class fields.
If they do, we’ll now get a type\-checking error.

[This check](https://github.com/microsoft/TypeScript/pull/54056) was contributed thanks to [Jack Works](https://github.com/Jack-Works)!

## Interactive Inlay Hints for Types

TypeScript’s inlay hints now support jumping to the definition of types!
This makes it easier to casually navigate your code.



See more at [the implementation here](https://github.com/microsoft/TypeScript/pull/55141).

## Settings to Prefer `type` Auto\-Imports

Previously when TypeScript generated auto\-imports for something in a type position, it would add a `type` modifier based on your settings.
For example, when getting an auto\-import on `Person` in the following:

\`\`\`
export let p: Person
\`\`\`
TypeScript’s editing experience would usually add an import for `Person` as:

\`\`\`
import { Person } from "./types";export let p: Person
\`\`\`
and under certain settings like `verbatimModuleSyntax`, it would add the `type` modifier:

\`\`\`
import { type Person } from "./types";export let p: Person
\`\`\`
However, maybe your codebase isn’t able to use some of these options; or you just have a preference for explicit `type` imports when possible.

[With a recent change](https://github.com/microsoft/TypeScript/pull/56090), TypeScript now enables this to be an editor\-specific option.
In Visual Studio Code, you can enable it in the UI under “TypeScript › Preferences: Prefer Type Only Auto Imports”, or as the JSON configuration option `typescript.preferences.preferTypeOnlyAutoImports`

## Optimizations by Skipping JSDoc Parsing

When running TypeScript via `tsc`, the compiler will now avoid parsing JSDoc.
This drops parsing time on its own, but also reduces memory usage to store comments along with time spent in garbage collection.
All\-in\-all, you should see slightly faster compiles and quicker feedback in `--watch` mode.

[The specific changes can be viewed here](https://github.com/microsoft/TypeScript/pull/52921).

Because not every tool using TypeScript will need to store JSDoc (e.g. typescript\-eslint and Prettier), this parsing strategy has been surfaced as part of the API itself.
This can enable these tools to gain the same memory and speed improvements we’ve brought to the TypeScript compiler.
The new options for comment parsing strategy are described in `JSDocParsingMode`.
More information is available [on this pull request](https://github.com/microsoft/TypeScript/pull/55739).

## Optimizations by Comparing Non\-Normalized Intersections

In TypeScript, unions and intersections always follow a specific form, where intersections can’t contain union types.
That means that when we create an intersection over a union like `A & (B | C)`, that intersection will be normalized into `(A & B) | (A & C)`.
Still, in some cases the type system will maintain the original form for display purposes.

It turns out that the original form can be used for some clever fast\-path comparisons between types.

For example, let’s say we have `SomeType & (Type1 | Type2 | ... | Type99999NINE)` and we want to see if that’s assignable to `SomeType`.
Recall that we don’t really have an intersection as our source type — we have a union that looks like `(SomeType & Type1) | (SomeType & Type2) | ... |(SomeType & Type99999NINE)`.
When checking if a union is assignable to some target type, we have to check if *every* member of the union is assignable to the target type, and that can be very slow.

In TypeScript 5\.3, we peek at the original intersection form that we were able to tuck away.
When we compare the types, we do a quick check to see if the target exists in any constituent of the source intersection.

For more information, [see this pull request](https://github.com/microsoft/TypeScript/pull/55851).

## Consolidation Between `tsserverlibrary.js` and `typescript.js`

TypeScript itself ships two library files: `tsserverlibrary.js` and `typescript.js`.
There are certain APIs available only in `tsserverlibrary.js` (like the `ProjectService` API), which may be useful to some importers.
Still, the two are distinct bundles with a lot of overlap, duplicating code in the package.
What’s more, it can be challenging to consistently use one over the other due to auto\-imports or muscle memory.
Accidentally loading both modules is far too easy, and code may not work properly on a different instance of the API.
Even if it does work, loading a second bundle increases resource usage.

Given this, we’ve decided to consolidate the two.
`typescript.js` now contains what `tsserverlibrary.js` used to contain, and `tsserverlibrary.js` now simply re\-exports `typescript.js`.
Comparing the before/after of this consolidation, we saw the following reduction in package size:

|  | Before | After | Diff | Diff (percent) |
| --- | --- | --- | --- | --- |
| Packed | 6\.90 MiB | 5\.48 MiB | \-1\.42 MiB | \-20\.61% |
| Unpacked | 38\.74 MiB | 30\.41 MiB | \-8\.33 MiB | \-21\.50% |

|  | Before | After | Diff | Diff (percent) |
| --- | --- | --- | --- | --- |
| `lib/tsserverlibrary.d.ts` | 570\.95 KiB | 865\.00 B | \-570\.10 KiB | \-99\.85% |
| `lib/tsserverlibrary.js` | 8\.57 MiB | 1012\.00 B | \-8\.57 MiB | \-99\.99% |
| `lib/typescript.d.ts` | 396\.27 KiB | 570\.95 KiB | \+174\.68 KiB | \+44\.08% |
| `lib/typescript.js` | 7\.95 MiB | 8\.57 MiB | \+637\.53 KiB | \+7\.84% |

In other words, this is over a 20\.5% reduction in package size.

For more information, you can [see the work involved here](https://github.com/microsoft/TypeScript/pull/55273).

## Breaking Changes and Correctness Improvements

### `lib.d.ts` Changes

Types generated for the DOM may have an impact on your codebase.
For more information, [see the DOM updates for TypeScript 5\.3](https://github.com/microsoft/TypeScript/pull/55798).

### Checks for `super` Accesses on Instance Properties

TypeScript 5\.3 now detects when the declaration referenced by a `super.` property access is a class field and issues an error.
This prevents errors that might occur at runtime.

[See more on this change here](https://github.com/microsoft/TypeScript/pull/54056).

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 5.3.md) ❤

Contributors to this page:  
ABELLast updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 4.9

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html)

Was this page helpful?

# TypeScript 4\.9

## The `satisfies` Operator

TypeScript developers are often faced with a dilemma: we want to ensure that some expression *matches* some type, but also want to keep the *most specific* type of that expression for inference purposes.

For example:

\`\`\`
// Each property can be a string or an RGB tuple.const palette = { red: \[255, 0, 0], green: "\#00ff00", bleu: \[0, 0, 255]// ^^^^ sacrebleu \- we've made a typo!};// We want to be able to use string methods on 'green'...const greenNormalized = palette.green.toUpperCase();
\`\`\`
Notice that we’ve written `bleu`, whereas we probably should have written `blue`.
We could try to catch that `bleu` typo by using a type annotation on `palette`, but we’d lose the information about each property.

\`\`\`
type Colors = "red" \| "green" \| "blue";type RGB = \[red: number, green: number, blue: number];const palette: Record\ = { red: \[255, 0, 0], green: "\#00ff00", bleu: \[0, 0, 255]// \~\~\~\~ The typo is now correctly detected};// But we now have an undesirable error here \- 'palette.green' "could" be of type RGB and// property 'toUpperCase' does not exist on type 'string \| RGB'.const greenNormalized = palette.green.toUpperCase();
\`\`\`
The new `satisfies` operator lets us validate that the type of an expression matches some type, without changing the resulting type of that expression.
As an example, we could use `satisfies` to validate that all the properties of `palette` are compatible with `string | number[]`:

\`\`\`
type Colors = "red" \| "green" \| "blue";type RGB = \[red: number, green: number, blue: number];const palette = { red: \[255, 0, 0], green: "\#00ff00", bleu: \[0, 0, 255]// \~\~\~\~ The typo is now caught!} satisfies Record\;// toUpperCase() method is still accessible!const greenNormalized = palette.green.toUpperCase();
\`\`\`
`satisfies` can be used to catch lots of possible errors.
For example, we could ensure that an object has *all* the keys of some type, but no more:

\`\`\`
type Colors = "red" \| "green" \| "blue";// Ensure that we have exactly the keys from 'Colors'.const favoriteColors = { "red": "yes", "green": false, "blue": "kinda", "platypus": false// \~\~\~\~\~\~\~\~\~\~ error \- "platypus" was never listed in 'Colors'.} satisfies Record\;// All the information about the 'red', 'green', and 'blue' properties are retained.const g: boolean = favoriteColors.green;
\`\`\`
Maybe we don’t care about if the property names match up somehow, but we do care about the types of each property.
In that case, we can also ensure that all of an object’s property values conform to some type.

\`\`\`
type RGB = \[red: number, green: number, blue: number];const palette = { red: \[255, 0, 0], green: "\#00ff00", blue: \[0, 0] // \~\~\~\~\~\~ error!} satisfies Record\;// Information about each property is still maintained.const redComponent = palette.red.at(0\);const greenNormalized = palette.green.toUpperCase();
\`\`\`
For more examples, you can see the [issue proposing this](https://github.com/microsoft/TypeScript/issues/47920) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/46827).
We’d like to thank [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who implemented and iterated on this feature with us.

## Unlisted Property Narrowing with the `in` Operator

As developers, we often need to deal with values that aren’t fully known at runtime.
In fact, we often don’t know if properties exist, whether we’re getting a response from a server or reading a configuration file.
JavaScript’s `in` operator can check whether a property
exists on an object.

Previously, TypeScript allowed us to narrow away any types that don’t explicitly list a property.

\`\`\`
interface RGB { red: number; green: number; blue: number;}interface HSV { hue: number; saturation: number; value: number;}function setColor(color: RGB \| HSV) { if ("hue" in color) { // 'color' now has the type HSV } // ...}
\`\`\`
Here, the type `RGB` didn’t list the `hue` and got narrowed away, and leaving us with the type `HSV`.

But what about examples where no type listed a given property?
In those cases, the language didn’t help us much.
Let’s take the following example in JavaScript:

\`\`\`
function tryGetPackageName(context) { const packageJSON = context.packageJSON; // Check to see if we have an object. if (packageJSON \&\& typeof packageJSON === "object") { // Check to see if it has a string name property. if ("name" in packageJSON \&\& typeof packageJSON.name === "string") { return packageJSON.name; } } return undefined;}
\`\`\`
Rewriting this to canonical TypeScript would just be a matter of defining and using a type for `context`;
however, picking a safe type like `unknown` for the `packageJSON` property would cause issues in older versions of TypeScript.

\`\`\`
interface Context { packageJSON: unknown;}function tryGetPackageName(context: Context) { const packageJSON = context.packageJSON; // Check to see if we have an object. if (packageJSON \&\& typeof packageJSON === "object") { // Check to see if it has a string name property. if ("name" in packageJSON \&\& typeof packageJSON.name === "string") { // \~\~\~\~ // error! Property 'name' does not exist on type 'object. return packageJSON.name; // \~\~\~\~ // error! Property 'name' does not exist on type 'object. } } return undefined;}
\`\`\`
This is because while the type of `packageJSON` was narrowed from `unknown` to `object`, the `in` operator strictly narrowed to types that actually defined the property being checked.
As a result, the type of `packageJSON` remained `object`.

TypeScript 4\.9 makes the `in` operator a little bit more powerful when narrowing types that *don’t* list the property at all.
Instead of leaving them as\-is, the language will intersect their types with `Record`.

So in our example, `packageJSON` will have its type narrowed from `unknown` to `object` to `object & Record`
That allows us to access `packageJSON.name` directly and narrow that independently.

\`\`\`
interface Context { packageJSON: unknown;}function tryGetPackageName(context: Context): string \| undefined { const packageJSON = context.packageJSON; // Check to see if we have an object. if (packageJSON \&\& typeof packageJSON === "object") { // Check to see if it has a string name property. if ("name" in packageJSON \&\& typeof packageJSON.name === "string") { // Just works! return packageJSON.name; } } return undefined;}
\`\`\`
TypeScript 4\.9 also tightens up a few checks around how `in` is used, ensuring that the left side is assignable to the type `string | number | symbol`, and the right side is assignable to `object`.
This helps check that we’re using valid property keys, and not accidentally checking primitives.

For more information, [read the implementing pull request](https://github.com/microsoft/TypeScript/pull/50666)

## Auto\-Accessors in Classes

TypeScript 4\.9 supports an upcoming feature in ECMAScript called auto\-accessors.
Auto\-accessors are declared just like properties on classes, except that they’re declared with the `accessor` keyword.

\`\`\`
class Person { accessor name: string; constructor(name: string) { this.name = name; }}
\`\`\`
Under the covers, these auto\-accessors “de\-sugar” to a `get` and `set` accessor with an unreachable private property.

\`\`\`
class Person { \#\_\_name: string; get name() { return this.\#\_\_name; } set name(value: string) { this.\#\_\_name = value; } constructor(name: string) { this.name = name; }}
\`\`\`
You can [read up more about the auto\-accessors pull request on the original PR](https://github.com/microsoft/TypeScript/pull/49705).

## Checks For Equality on `NaN`

A major gotcha for JavaScript developers is checking against the value `NaN` using the built\-in equality operators.

For some background, `NaN` is a special numeric value that stands for “Not a Number”.
Nothing is ever equal to `NaN` \- even `NaN`!

\`\`\`
console.log(NaN == 0\) // falseconsole.log(NaN === 0\) // falseconsole.log(NaN == NaN) // falseconsole.log(NaN === NaN) // false
\`\`\`
But at least symmetrically *everything* is always not\-equal to `NaN`.

\`\`\`
console.log(NaN != 0\) // trueconsole.log(NaN !== 0\) // trueconsole.log(NaN != NaN) // trueconsole.log(NaN !== NaN) // true
\`\`\`
This technically isn’t a JavaScript\-specific problem, since any language that contains IEEE\-754 floats has the same behavior;
but JavaScript’s primary numeric type is a floating point number, and number parsing in JavaScript can often result in `NaN`.
In turn, checking against `NaN` ends up being fairly common, and the correct way to do so is to use [`Number.isNaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN) \- *but* as we mentioned, lots of people accidentally end up checking with `someValue === NaN` instead.

TypeScript now errors on direct comparisons against `NaN`, and will suggest using some variation of `Number.isNaN` instead.

\`\`\`
function validate(someValue: number) { return someValue !== NaN; // \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~ // error: This condition will always return 'true'. // Did you mean '!Number.isNaN(someValue)'?}
\`\`\`
We believe that this change should strictly help catch beginner errors, similar to how TypeScript currently issues errors on comparisons against object and array literals.

We’d like to extend our thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who [contributed this check](https://github.com/microsoft/TypeScript/pull/50626).

## File\-Watching Now Uses File System Events

In earlier versions, TypeScript leaned heavily on *polling* for watching individual files.
Using a polling strategy meant checking the state of a file periodically for updates.
On Node.js, [`fs.watchFile`](https://nodejs.org/docs/latest-v18.x/api/fs.html#fswatchfilefilename-options-listener) is the built\-in way to get a polling file\-watcher.
While polling tends to be more predictable across platforms and file systems, it means that your CPU has to periodically get interrupted and check for updates to the file, even when nothing’s changed.
For a few dozen files, this might not be noticeable;
but on a bigger project with lots of files \- or lots of files in `node_modules` \- this can become a resource hog.

Generally speaking, a better approach is to use file system events.
Instead of polling, we can announce that we’re interested in updates of specific files and provide a callback for when those files *actually do* change.
Most modern platforms in use provide facilities and APIs like `CreateIoCompletionPort`, `kqueue`, `epoll`, and `inotify`.
Node.js mostly abstracts these away by providing [`fs.watch`](https://nodejs.org/docs/latest-v18.x/api/fs.html#fswatchfilename-options-listener).
File system events usually work great, but there are [lots of caveats](https://nodejs.org/docs/latest-v18.x/api/fs.html#caveats) to using them, and in turn, to using the `fs.watch` API.
A watcher needs to be careful to consider [inode watching](https://nodejs.org/docs/latest-v18.x/api/fs.html#inodes), [unavailability on certain file systems](https://nodejs.org/docs/latest-v18.x/api/fs.html#availability) (e.g.networked file systems), whether recursive file watching is available, whether directory renames trigger events, and even file watcher exhaustion!
In other words, it’s not quite a free lunch, especially if you’re looking for something cross\-platform.

As a result, our default was to pick the lowest common denominator: polling.
Not always, but most of the time.

Over time, we’ve provided the means to [choose other file\-watching strategies](https://www.typescriptlang.org/docs/handbook/configuring-watch.html).
This allowed us to get feedback and harden our file\-watching implementation against most of these platform\-specific gotchas.
As TypeScript has needed to scale to larger codebases, and has improved in this area, we felt swapping to file system events as the default would be a worthwhile investment.

In TypeScript 4\.9, file watching is powered by file system events by default, only falling back to polling if we fail to set up event\-based watchers.
For most developers, this should provide a much less resource\-intensive experience when running in `--watch` mode, or running with a TypeScript\-powered editor like Visual Studio or VS Code.

[The way file\-watching works can still be configured](https://www.typescriptlang.org/docs/handbook/configuring-watch.html) through environment variables and `watchOptions` \- and [some editors like VS Code can support `watchOptions` independently](https://code.visualstudio.com/docs/getstarted/settings#:~:text=typescript%2etsserver%2ewatchOptions).
Developers using more exotic set\-ups where source code resides on a networked file systems (like NFS and SMB) may need to opt back into the older behavior; though if a server has reasonable processing power, it might just be better to enable SSH and run TypeScript remotely so that it has direct local file access.
VS Code has plenty of [remote extensions](https://marketplace.visualstudio.com/search?term=remote&target=VSCode&category=All%20categories&sortBy=Relevance) to make this easier.

You can [read up more on this change on GitHub](https://github.com/microsoft/TypeScript/pull/50366).

## “Remove Unused Imports” and “Sort Imports” Commands for Editors

Previously, TypeScript only supported two editor commands to manage imports.
For our examples, take the following code:

\`\`\`
import { Zebra, Moose, HoneyBadger } from "./zoo";import { foo, bar } from "./helper";let x: Moose \| HoneyBadger = foo();
\`\`\`
The first was called “Organize Imports” which would remove unused imports, and then sort the remaining ones.
It would rewrite that file to look like this one:

\`\`\`
import { foo } from "./helper";import { HoneyBadger, Moose } from "./zoo";let x: Moose \| HoneyBadger = foo();
\`\`\`
In TypeScript 4\.3, we introduced a command called “Sort Imports” which would *only* sort imports in the file, but not remove them \- and would rewrite the file like this.

\`\`\`
import { bar, foo } from "./helper";import { HoneyBadger, Moose, Zebra } from "./zoo";let x: Moose \| HoneyBadger = foo();
\`\`\`
The caveat with “Sort Imports” was that in Visual Studio Code, this feature was only available as an on\-save command \- not as a manually triggerable command.

TypeScript 4\.9 adds the other half, and now provides “Remove Unused Imports”.
TypeScript will now remove unused import names and statements, but will otherwise leave the relative ordering alone.

\`\`\`
import { Moose, HoneyBadger } from "./zoo";import { foo } from "./helper";let x: Moose \| HoneyBadger = foo();
\`\`\`
This feature is available to all editors that wish to use either command;
but notably, Visual Studio Code (1\.73 and later) will have support built in *and* will surface these commands via its Command Palette.
Users who prefer to use the more granular “Remove Unused Imports” or “Sort Imports” commands should be able to reassign the “Organize Imports” key combination to them if desired.

You can [view specifics of the feature here](https://github.com/microsoft/TypeScript/pull/50931).

## Go\-to\-Definition on `return` Keywords

In the editor, when running a go\-to\-definition on the `return` keyword, TypeScript will now jump you to the top of the corresponding function.
This can be helpful to get a quick sense of which function a `return` belongs to.

We expect TypeScript will expand this functionality to more keywords [such as `await` and `yield`](https://github.com/microsoft/TypeScript/issues/51223) or [`switch`, `case`, and `default`](https://github.com/microsoft/TypeScript/issues/51225).

[This feature was implemented](https://github.com/microsoft/TypeScript/pull/51227) thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk).

## Performance Improvements

TypeScript has a few small, but notable, performance improvements.

First, TypeScript’s `forEachChild` function has been rewritten to use a function table lookup instead of a `switch` statement across all syntax nodes.
`forEachChild` is a workhorse for traversing syntax nodes in the compiler, and is used heavily in the binding stage of our compiler, along with parts of the language service.
The refactoring of `forEachChild` yielded up to a 20% reduction of time spent in our binding phase and across language service operations.

Once we discovered this performance win for `forEachChild`, we tried it out on `visitEachChild`, a function we use for transforming nodes in the compiler and language service.
The same refactoring yielded up to a 3% reduction in time spent in generating project output.

The initial exploration in `forEachChild` was [inspired by a blog post](https://artemis.sh/2022/08/07/emulating-calculators-fast-in-js.html) by [Artemis Everfree](https://artemis.sh/).
While we have some reason to believe the root cause of our speed\-up might have more to do with function size/complexity than the issues described in the blog post, we’re grateful that we were able to learn from the experience and try out a relatively quick refactoring that made TypeScript faster.

Finally, the way TypeScript preserves the information about a type in the true branch of a conditional type has been optimized.
In a type like

\`\`\`
interface Zoo\ { // ...}type MakeZoo\ = A extends Animal ? Zoo\ : never;
\`\`\`
TypeScript has to “remember” that `A` must also be an `Animal` when checking if `Zoo` is valid.
This is basically done by creating a special type that used to hold the intersection of `A` with `Animal`;
however, TypeScript previously did this eagerly which isn’t always necessary.
Furthermore, some faulty code in our type\-checker prevented these special types from being simplified.
TypeScript now defers intersecting these types until it’s necessary.
For codebases with heavy use of conditional types, you might witness significant speed\-ups with TypeScript, but in our performance testing suite, we saw a more modest 3% reduction in type\-checking time.

You can read up more on these optimizations on their respective pull requests:

* [`forEachChild` as a jump\-table](https://github.com/microsoft/TypeScript/pull/50225)
* [`visitEachChild` as a jump\-table](https://github.com/microsoft/TypeScript/pull/50266)
* [Optimize substitition types](https://github.com/microsoft/TypeScript/pull/50397)

## Correctness Fixes and Breaking Changes

### `lib.d.ts` Updates

While TypeScript strives to avoid major breaks, even small changes in the built\-in libraries can cause issues.
We don’t expect major breaks as a result of DOM and `lib.d.ts` updates, but there may be some small ones.

### Better Types for `Promise.resolve`

`Promise.resolve` now uses the `Awaited` type to unwrap Promise\-like types passed to it.
This means that it more often returns the right `Promise` type, but that improved type can break existing code if it was expecting `any` or `unknown` instead of a `Promise`.
For more information, [see the original change](https://github.com/microsoft/TypeScript/pull/33074).

### JavaScript Emit No Longer Elides Imports

When TypeScript first supported type\-checking and compilation for JavaScript, it accidentally supported a feature called import elision.
In short, if an import is not used as a value, or the compiler can detect that the import doesn’t refer to a value at runtime, the compiler will drop the import during emit.

This behavior was questionable, especially the detection of whether the import doesn’t refer to a value, since it means that TypeScript has to trust sometimes\-inaccurate declaration files.
In turn, TypeScript now preserves imports in JavaScript files.

\`\`\`
// Input:import { someValue, SomeClass } from "some\-module";/\*\* @type {SomeClass} \*/let val = someValue;// Previous Output:import { someValue } from "some\-module";/\*\* @type {SomeClass} \*/let val = someValue;// Current Output:import { someValue, SomeClass } from "some\-module";/\*\* @type {SomeClass} \*/let val = someValue;
\`\`\`
More information is available at [the implementing change](https://github.com/microsoft/TypeScript/pull/50404).

### `exports` is Prioritized Over `typesVersions`

Previously, TypeScript incorrectly prioritized the `typesVersions` field over the `exports` field when resolving through a `package.json` under `--moduleResolution node16`.
If this change impacts your library, you may need to add `types@` version selectors in your `package.json`’s `exports` field.

\`\`\`
 { "type": "module", "main": "./dist/main.js" "typesVersions": { "\<4\.8": { ".": \["4\.8\-types/main.d.ts"] }, "\*": { ".": \["modern\-types/main.d.ts"] } }, "exports": { ".": {\+ "types@\<4\.8": "4\.8\-types/main.d.ts",\+ "types": "modern\-types/main.d.ts", "import": "./dist/main.js" } } }
\`\`\`
For more information, [see this pull request](https://github.com/microsoft/TypeScript/pull/50890).

## `substitute` Replaced With `constraint` on `SubstitutionType`s

As part of an optimization on substitution types, `SubstitutionType` objects no longer contain the `substitute` property representing the effective substitution (usually an intersection of the base type and the implicit constraint) \- instead, they just contain the `constraint` property.

For more details, [read more on the original pull request](https://github.com/microsoft/TypeScript/pull/50397).

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 4.9.md) ❤

Contributors to this page:  
NBM제NLast updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 5.4

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-4.html)

Was this page helpful?

# TypeScript 5\.4

## Preserved Narrowing in Closures Following Last Assignments

TypeScript can usually figure out a more specific type for a variable based on checks that you might perform.
This process is called narrowing.

\`\`\`
function uppercaseStrings(x: string \| number) { if (typeof x === "string") { // TypeScript knows 'x' is a 'string' here. return x.toUpperCase(); }}
\`\`\`
One common pain point was that these narrowed types weren’t always preserved within function closures.

\`\`\`
function getUrls(url: string \| URL, names: string\[]) { if (typeof url === "string") { url = new URL(url); } return names.map(name =\> { url.searchParams.set("name", name) // \~\~\~\~\~\~\~\~\~\~\~\~ // error! // Property 'searchParams' does not exist on type 'string \| URL'. return url.toString(); });}
\`\`\`
Here, TypeScript decided that it wasn’t “safe” to assume that `url` was *actually* a `URL` object in our callback function because it was mutated elsewhere;
however, in this instance, that arrow function is *always* created after that assignment to `url`, and it’s also the *last* assignment to `url`.

TypeScript 5\.4 takes advantage of this to make narrowing a little smarter.
When parameters and `let` variables are used in non\-[hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting) functions, the type\-checker will look for a last assignment point.
If one is found, TypeScript can safely narrow from outside the containing function.
What that means is the above example just works now.

Note that narrowing analysis doesn’t kick in if the variable is assigned anywhere in a nested function.
This is because there’s no way to know for sure whether the function will be called later.

\`\`\`
function printValueLater(value: string \| undefined) { if (value === undefined) { value = "missing!"; } setTimeout(() =\> { // Modifying 'value', even in a way that shouldn't affect // its type, will invalidate type refinements in closures. value = value; }, 500\); setTimeout(() =\> { console.log(value.toUpperCase()); // \~\~\~\~\~ // error! 'value' is possibly 'undefined'. }, 1000\);}
\`\`\`
This should make lots of typical JavaScript code easier to express.
You can [read more about the change on GitHub](https://github.com/microsoft/TypeScript/pull/56908).

## The `NoInfer` Utility Type

When calling generic functions, TypeScript is able to infer type arguments from whatever you pass in.

\`\`\`
function doSomething\(arg: T) { // ...}// We can explicitly say that 'T' should be 'string'.doSomething\("hello!");// We can also just let the type of 'T' get inferred.doSomething("hello!");
\`\`\`
One challenge, however, is that it is not always clear what the “best” type is to infer.
This might lead to TypeScript rejecting valid calls, accepting questionable calls, or just reporting worse error messages when it catches a bug.

For example, let’s imagine a `createStreetLight` function that takes a list of color names, along with an optional default color.

\`\`\`
function createStreetLight\(colors: C\[], defaultColor?: C) { // ...}createStreetLight(\["red", "yellow", "green"], "red");
\`\`\`
What happens when we pass in a `defaultColor` that wasn’t in the original `colors` array?
In this function, `colors` is supposed to be the “source of truth” and describe what can be passed to `defaultColor`.

\`\`\`
// Oops! This is undesirable, but is allowed!createStreetLight(\["red", "yellow", "green"], "blue");
\`\`\`
In this call, type inference decided that `"blue"` was just as valid of a type as `"red"` or `"yellow"` or `"green"`.
So instead of rejecting the call, TypeScript infers the type of `C` as `"red" | "yellow" | "green" | "blue"`.
You might say that inference just blue up in our faces!

One way people currently deal with this is to add a separate type parameter that’s bounded by the existing type parameter.

\`\`\`
function createStreetLight\(colors: C\[], defaultColor?: D) {}createStreetLight(\["red", "yellow", "green"], "blue");// \~\~\~\~\~\~// error!// Argument of type '"blue"' is not assignable to parameter of type '"red" \| "yellow" \| "green" \| undefined'.
\`\`\`
This works, but is a little bit awkward because `D` probably won’t be used anywhere else in the signature for `createStreetLight`.
While not bad *in this case*, using a type parameter only once in a signature is often a code smell.

That’s why TypeScript 5\.4 introduces a new `NoInfer` utility type.
Surrounding a type in `NoInfer` gives a signal to TypeScript not to dig in and match against the inner types to find candidates for type inference.

Using `NoInfer`, we can rewrite `createStreetLight` as something like this:

\`\`\`
function createStreetLight\(colors: C\[], defaultColor?: NoInfer\) { // ...}createStreetLight(\["red", "yellow", "green"], "blue");// \~\~\~\~\~\~// error!// Argument of type '"blue"' is not assignable to parameter of type '"red" \| "yellow" \| "green" \| undefined'.
\`\`\`
Excluding the type of `defaultColor` from being explored for inference means that `"blue"` never ends up as an inference candidate, and the type\-checker can reject it.

You can see the specific changes in [the implementing pull request](https://github.com/microsoft/TypeScript/pull/56794), along with [the initial implementation](https://github.com/microsoft/TypeScript/pull/52968) provided thanks to [Mateusz Burzyński](https://github.com/Andarist)!

## `Object.groupBy` and `Map.groupBy`

TypeScript 5\.4 adds declarations for JavaScript’s new `Object.groupBy` and `Map.groupBy` static methods.

`Object.groupBy` takes an iterable, and a function that decides which “group” each element should be placed in.
The function needs to make a “key” for each distinct group, and `Object.groupBy` uses that key to make an object where every key maps to an array with the original element in it.

So the following JavaScript:

\`\`\`
const array = \[0, 1, 2, 3, 4, 5];const myObj = Object.groupBy(array, (num, index) =\> { return num % 2 === 0 ? "even": "odd";});
\`\`\`
is basically equivalent to writing this:

\`\`\`
const myObj = { even: \[0, 2, 4], odd: \[1, 3, 5],};
\`\`\`
`Map.groupBy` is similar, but produces a `Map` instead of a plain object.
This might be more desirable if you need the guarantees of `Map`s, you’re dealing with APIs that expect `Map`s, or you need to use any kind of key for grouping \- not just keys that can be used as property names in JavaScript.

\`\`\`
const myObj = Map.groupBy(array, (num, index) =\> { return num % 2 === 0 ? "even" : "odd";});
\`\`\`
and just as before, you could have created `myObj` in an equivalent way:

\`\`\`
const myObj = new Map();myObj.set("even", \[0, 2, 4]);myObj.set("odd", \[1, 3, 5]);
\`\`\`
Note that in the above example of `Object.groupBy`, the object produced uses all optional properties.

\`\`\`
interface EvenOdds { even?: number\[]; odd?: number\[];}const myObj: EvenOdds = Object.groupBy(...);myObj.even;// \~\~\~\~// Error to access this under 'strictNullChecks'.
\`\`\`
This is because there’s no way to guarantee in a general way that *all* the keys were produced by `groupBy`.

Note also that these methods are only accessible by configuring your `target` to `esnext` or adjusting your `lib` settings.
We expect they will eventually be available under a stable `es2024` target.

We’d like to extend a thanks to [Kevin Gibbons](https://github.com/bakkot) for [adding the declarations to these `groupBy` methods](https://github.com/microsoft/TypeScript/pull/56805).

## Support for `require()` calls in `--moduleResolution bundler` and `--module preserve`

TypeScript has a `moduleResolution` option called `bundler` that is meant to model the way modern bundlers figure out which file an import path refers to.
One of the limitations of the option is that it had to be paired with `--module esnext`, making it impossible to use the `import ... = require(...)` syntax.

\`\`\`
// previously erroredimport myModule = require("module/path");
\`\`\`
That might not seem like a big deal if you’re planning on just writing standard ECMAScript `import`s, but there’s a difference when using a package with [conditional exports](https://nodejs.org/api/packages.html#conditional-exports).

In TypeScript 5\.4, `require()` can now be used when setting the `module` setting to a new option called `preserve`.

Between `--module preserve` and `--moduleResolution bundler`, the two more accurately model what bundlers and runtimes like Bun will allow, and how they’ll perform module lookups.
In fact, when using `--module preserve`, the `bundler` option will be implicitly set for `--moduleResolution` (along with `--esModuleInterop` and `--resolveJsonModule`)

\`\`\`
{ "compilerOptions": { "module": "preserve", // ^ also implies: // "moduleResolution": "bundler", // "esModuleInterop": true, // "resolveJsonModule": true, // ... }}
\`\`\`
Under `--module preserve`, an ECMAScript `import` will always be emitted as\-is, and `import ... = require(...)` will be emitted as a `require()` call (though in practice you may not even use TypeScript for emit, since it’s likely you’ll be using a bundler for your code).
This holds true regardless of the file extension of the containing file.
So the output of this code:

\`\`\`
import \* as foo from "some\-package/foo";import bar = require("some\-package/bar");
\`\`\`
should look something like this:

\`\`\`
import \* as foo from "some\-package/foo";var bar = require("some\-package/bar");
\`\`\`
What this also means is that the syntax you choose directs how [conditional exports](https://nodejs.org/api/packages.html#conditional-exports) are matched.
So in the above example, if the `package.json` of `some-package` looks like this:

\`\`\`
{ "name": "some\-package", "version": "0\.0\.1", "exports": { "./foo": { "import": "./esm/foo\-from\-import.mjs", "require": "./cjs/foo\-from\-require.cjs" }, "./bar": { "import": "./esm/bar\-from\-import.mjs", "require": "./cjs/bar\-from\-require.cjs" } }}
\`\`\`
TypeScript will resolve these paths to `[...]/some-package/esm/foo-from-import.mjs` and `[...]/some-package/cjs/bar-from-require.cjs`.

For more information, you can [read up on these new settings here](https://github.com/microsoft/TypeScript/pull/56785).

## Checked Import Attributes and Assertions

Import attributes and assertions are now checked against the global `ImportAttributes` type.
This means that runtimes can now more accurately describe the import attributes

\`\`\`
// In some global file.interface ImportAttributes { type: "json";}// In some other moduleimport \* as ns from "foo" with { type: "not\-json" };// \~\~\~\~\~\~\~\~\~\~// error!//// Type '{ type: "not\-json"; }' is not assignable to type 'ImportAttributes'.// Types of property 'type' are incompatible.// Type '"not\-json"' is not assignable to type '"json"'.
\`\`\`
[This change](https://github.com/microsoft/TypeScript/pull/56034) was provided thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk).

## Quick Fix for Adding Missing Parameters

TypeScript now has a quick fix to add a new parameter to functions that are called with too many arguments.





This can be useful when threading a new argument through several existing functions, which can be cumbersome today.

[This quick fix](https://github.com/microsoft/TypeScript/pull/56411) was provided courtsey of [Oleksandr Tarasiuk](https://github.com/a-tarasyuk).

## Upcoming Changes from TypeScript 5\.0 Deprecations

TypeScript 5\.0 deprecated the following options and behaviors:

* `charset`
* `target: ES3`
* `importsNotUsedAsValues`
* `noImplicitUseStrict`
* `noStrictGenericChecks`
* `keyofStringsOnly`
* `suppressExcessPropertyErrors`
* `suppressImplicitAnyIndexErrors`
* `out`
* `preserveValueImports`
* `prepend` in project references
* implicitly OS\-specific `newLine`

To continue using them, developers using TypeScript 5\.0 and other more recent versions have had to specify a new option called `ignoreDeprecations` with the value `"5.0"`.

However, TypScript 5\.4 will be the last version in which these will continue to function as normal.
By TypeScript 5\.5 (likely June 2024\), these will become hard errors, and code using them will need to be migrated away.

For more information, you can [read up on this plan on GitHub](https://github.com/microsoft/TypeScript/issues/51909), which contains suggestions in how to best adapt your codebase.

## Notable Behavioral Changes

This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### `lib.d.ts` Changes

Types generated for the DOM may have an impact on type\-checking your codebase.
For more information, [see the DOM updates for TypeScript 5\.4](https://github.com/microsoft/TypeScript/pull/57027).

### More Accurate Conditional Type Constraints

The following code no longer allows the second variable declaration in the function `foo`.

\`\`\`
type IsArray\ = T extends any\[] ? true : false;function foo\(x: IsArray\) { let first: true = x; // Error let second: false = x; // Error, but previously wasn't}
\`\`\`
Previously, when TypeScript checked the initializer for `second`, it needed to determine whether `IsArray` was assignable to the unit type `false`.
While `IsArray` isn’t compatible any obvious way, TypeScript looks at the *constraint* of that type as well.
In a conditional type like `T extends Foo ? TrueBranch : FalseBranch`, where `T` is generic, the type system would look at the constraint of `T`, substitute it in for `T` itself, and decide on either the true or false branch.

But this behavior was inaccurate because it was overly eager.
Even if the constraint of `T` isn’t assignable to `Foo`, that doesn’t mean that it won’t be instantiated with something that is.
And so the more correct behavior is to produce a union type for the constraint of the conditional type in cases where it can’t be proven that `T` *never* or *always* extends `Foo.`

TypeScript 5\.4 adopts this more accurate behavior.
What this means in practice is that you may begin to find that some conditional type instances are no longer compatible with their branches.

[You can read about the specific changes here](https://github.com/microsoft/TypeScript/pull/56004).

### More Aggressive Reduction of Intersections Between Type Variables and Primitive Types

TypeScript now reduces intersections with type variables and primitives more aggressively, depending on how the type variable’s constraint overlaps with those primitives.

\`\`\`
declare function intersect\(x: T, y: U): T \& U;function foo\(x: T, str: string, num: number) { // Was 'T \& string', now is just 'T' let a = intersect(x, str); // Was 'T \& number', now is just 'never' let b = intersect(x, num) // Was '(T \& "abc") \| (T \& "def")', now is just 'T' let c = Math.random() \() { let x: \`\-${keyof T \& string}\`; // Used to error, now doesn't. x = "\-id";}
\`\`\`
This behavior is more desirable, but may cause breaks in code using constructs like conditional types, where these rule changes are easy to witness.

[See this change](https://github.com/microsoft/TypeScript/pull/56598) for more details.

### Errors When Type\-Only Imports Conflict with Local Values

Previously, TypeScript would permit the following code under `isolatedModules` if the import to `Something` only referred to a type.

\`\`\`
import { Something } from "./some/path";let Something = 123;
\`\`\`
However, it’s not safe for single\-file compilers to assume whether it’s “safe” to drop the `import`, even if the code is guaranteed to fail at runtime.
In TypeScript 5\.4, this code will trigger an error like the following:

\`\`\`
Import 'Something' conflicts with local value, so must be declared with a type\-only import when 'isolatedModules' is enabled.
\`\`\`
The fix should be to either make a local rename, or, as the error states, add the `type` modifier to the import:

\`\`\`
import type { Something } from "./some/path";// orimport { type Something } from "./some/path";
\`\`\`
[See more information on the change itself](https://github.com/microsoft/TypeScript/pull/56354).

### New Enum Assignability Restrictions

When two enums have the same declared names and enum member names, they were previously always considered compatible;
however, when the values were known, TypeScript would silently allow them to have differing values.

TypeScript 5\.4 tightens this restriction by requiring the values to be identical when they are known.

\`\`\`
namespace First { export enum SomeEnum { A = 0, B = 1, }}namespace Second { export enum SomeEnum { A = 0, B = 2, }}function foo(x: First.SomeEnum, y: Second.SomeEnum) { // Both used to be compatible \- no longer the case, // TypeScript errors with something like: // // Each declaration of 'SomeEnum.B' differs in its value, where '1' was expected but '2' was given. x = y; y = x;}
\`\`\`
Additionally, there are new restrictions for when one of the enum members does not have a statically known value.
In these cases, the other enum must at least be implicitly numeric (e.g. it has no statically resolved initializer), or it is explicitly numeric (meaning TypeScript could resolve the value to something numeric).
Practically speaking, what this means is that string enum members are only ever compatible with other string enums of the same value.

\`\`\`
namespace First { export declare enum SomeEnum { A, B, }}namespace Second { export declare enum SomeEnum { A, B = "some known string", }}function foo(x: First.SomeEnum, y: Second.SomeEnum) { // Both used to be compatible \- no longer the case, // TypeScript errors with something like: // // One value of 'SomeEnum.B' is the string '"some known string"', and the other is assumed to be an unknown numeric value. x = y; y = x;}
\`\`\`
For more information, [see the pull request that introduced this change](https://github.com/microsoft/TypeScript/pull/55924).

### Name Restrictions on Enum Members

TypeScript no longer allows enum members to use the names `Infinity`, `-Infinity`, or `NaN`.

\`\`\`
// Errors on all of these://// An enum member cannot have a numeric name.enum E { Infinity = 0, "\-Infinity" = 1, NaN = 2,}
\`\`\`
[See more details here](https://github.com/microsoft/TypeScript/pull/56161).

### Better Mapped Type Preservation Over Tuples with `any` Rest Elements

Previously, applying a mapped type with `any` into a tuple would create an `any` element type.
This is undesirable and is now fixed.

\`\`\`
Promise.all(\["", ...(\[] as any)]) .then((result) =\> { const head = result\[0]; // 5\.3: any, 5\.4: string const tail = result.slice(1\); // 5\.3 any, 5\.4: any\[] });
\`\`\`
For more information, see [the fix](https://github.com/microsoft/TypeScript/pull/57031) along with [the follow\-on discussion around behavioral changes](https://github.com/microsoft/TypeScript/issues/57389) and [further tweaks](https://github.com/microsoft/TypeScript/issues/57389).

### Emit Changes

While not a breaking change per se, developers may have implicitly taken dependencies on TypeScript’s JavaScript or declaration emit outputs.
The following are notable changes.

* [Preserve type parameter names more often when shadowed](https://github.com/microsoft/TypeScript/pull/55820)
* [Move complex parameter lists of async function into downlevel generator body](https://github.com/microsoft/TypeScript/pull/56296)
* [Do not remove binding alias in function declarations](https://github.com/microsoft/TypeScript/pull/57020)
* [ImportAttributes should go through the same emit phases when in an ImportTypeNode](https://github.com/microsoft/TypeScript/pull/56395)
The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 5.4.md) ❤

Contributors to this page:  
NILast updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 5.2

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html)

Was this page helpful?

# TypeScript 5\.2

## `using` Declarations and Explicit Resource Management

TypeScript 5\.2 adds support for the upcoming [Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management) feature in ECMAScript.
Let’s explore some of the motivations and understand what the feature brings us.

It’s common to need to do some sort of “clean\-up” after creating an object.
For example, you might need to close network connections, delete temporary files, or just free up some memory.

Let’s imagine a function that creates a temporary file, reads and writes to it for various operations, and then closes and deletes it.

\`\`\`
import \* as fs from "fs";export function doSomeWork() { const path = ".some\_temp\_file"; const file = fs.openSync(path, "w\+"); // use file... // Close the file and delete it. fs.closeSync(file); fs.unlinkSync(path);}
\`\`\`
This is fine, but what happens if we need to perform an early exit?

\`\`\`
export function doSomeWork() { const path = ".some\_temp\_file"; const file = fs.openSync(path, "w\+"); // use file... if (someCondition()) { // do some more work... // Close the file and delete it. fs.closeSync(file); fs.unlinkSync(path); return; } // Close the file and delete it. fs.closeSync(file); fs.unlinkSync(path);}
\`\`\`
We’re starting to see some duplication of clean\-up which can be easy to forget.
We’re also not guaranteed to close and delete the file if an error gets thrown.
This could be solved by wrapping this all in a `try`/`finally` block.

\`\`\`
export function doSomeWork() { const path = ".some\_temp\_file"; const file = fs.openSync(path, "w\+"); try { // use file... if (someCondition()) { // do some more work... return; } } finally { // Close the file and delete it. fs.closeSync(file); fs.unlinkSync(path); }}
\`\`\`
While this is more robust, it’s added quite a bit of “noise” to our code.
There are also other foot\-guns we can run into if we start adding more clean\-up logic to our `finally` block — for example, exceptions preventing other resources from being disposed.
This is what the [explicit resource management](https://github.com/tc39/proposal-explicit-resource-management) proposal aims to solve.
The key idea of the proposal is to support resource disposal — this clean\-up work we’re trying to deal with — as a first class idea in JavaScript.

This starts by adding a new built\-in `symbol` called `Symbol.dispose`, and we can create objects with methods named by `Symbol.dispose`.
For convenience, TypeScript defines a new global type called `Disposable` which describes these.

\`\`\`
class TempFile implements Disposable { \#path: string; \#handle: number; constructor(path: string) { this.\#path = path; this.\#handle = fs.openSync(path, "w\+"); } // other methods \[Symbol.dispose]() { // Close the file and delete it. fs.closeSync(this.\#handle); fs.unlinkSync(this.\#path); }}
\`\`\`
Later on we can call those methods.

\`\`\`
export function doSomeWork() { const file = new TempFile(".some\_temp\_file"); try { // ... } finally { file\[Symbol.dispose](); }}
\`\`\`
Moving the clean\-up logic to `TempFile` itself doesn’t buy us much;
we’ve basically just moved all the clean\-up work from the `finally` block into a method, and that’s always been possible.
But having a well\-known “name” for this method means that JavaScript can build other features on top of it.

That brings us to the first star of the feature: `using` declarations!
`using` is a new keyword that lets us declare new fixed bindings, kind of like `const`.
The key difference is that variables declared with `using` get their `Symbol.dispose` method called at the end of the scope!

So we could simply have written our code like this:

\`\`\`
export function doSomeWork() { using file = new TempFile(".some\_temp\_file"); // use file... if (someCondition()) { // do some more work... return; }}
\`\`\`
Check it out — no `try`/`finally` blocks!
At least, none that we see.
Functionally, that’s exactly what `using` declarations will do for us, but we don’t have to deal with that.

You might be familiar with [`using` declarations in C\#](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/using), [`with` statements in Python](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement), or [`try`\-with\-resource declarations in Java](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html).
These are all similar to JavaScript’s new `using` keyword, and provide a similar explicit way to perform a “tear\-down” of an object at the end of a scope.

`using` declarations do this clean\-up at the very end of their containing scope or right before an “early return” like a `return` or a `throw`n error.
They also dispose in a first\-in\-last\-out order like a stack.

\`\`\`
function loggy(id: string): Disposable { console.log(\`Creating ${id}\`); return { \[Symbol.dispose]() { console.log(\`Disposing ${id}\`); } }}function func() { using a = loggy("a"); using b = loggy("b"); { using c = loggy("c"); using d = loggy("d"); } using e = loggy("e"); return; // Unreachable. // Never created, never disposed. using f = loggy("f");}func();// Creating a// Creating b// Creating c// Creating d// Disposing d// Disposing c// Creating e// Disposing e// Disposing b// Disposing a
\`\`\`
`using` declarations are supposed to be resilient to exceptions;
if an error is thrown, it’s rethrown after disposal.
On the other hand, the body of your function might execute as expected, but the `Symbol.dispose` might throw.
In that case, that exception is rethrown as well.

But what happens if both the logic before and during disposal throws an error?
For those cases, `SuppressedError` has been introduced as a new subtype of `Error`.
It features a `suppressed` property that holds the last\-thrown error, and an `error` property for the most\-recently thrown error.

\`\`\`
class ErrorA extends Error { name = "ErrorA";}class ErrorB extends Error { name = "ErrorB";}function throwy(id: string) { return { \[Symbol.dispose]() { throw new ErrorA(\`Error from ${id}\`); } };}function func() { using a = throwy("a"); throw new ErrorB("oops!")}try { func();}catch (e: any) { console.log(e.name); // SuppressedError console.log(e.message); // An error was suppressed during disposal. console.log(e.error.name); // ErrorA console.log(e.error.message); // Error from a console.log(e.suppressed.name); // ErrorB console.log(e.suppressed.message); // oops!}
\`\`\`
You might have noticed that we’re using synchronous methods in these examples.
However, lots of resource disposal involves *asynchronous* operations, and we need to wait for those to complete before we continue running any other code.

That’s why there is also a new `Symbol.asyncDispose`, and it brings us to the next star of the show — `await using` declarations.
These are similar to `using` declarations, but the key is that they look up whose disposal must be `await`ed.
They use a different method named by `Symbol.asyncDispose`, though they can operate on anything with a `Symbol.dispose` as well.
For convenience, TypeScript also introduces a global type called `AsyncDisposable` that describes any object with an asynchronous dispose method.

\`\`\`
async function doWork() { // Do fake work for half a second. await new Promise(resolve =\> setTimeout(resolve, 500\));}function loggy(id: string): AsyncDisposable { console.log(\`Constructing ${id}\`); return { async \[Symbol.asyncDispose]() { console.log(\`Disposing (async) ${id}\`); await doWork(); }, }}async function func() { await using a = loggy("a"); await using b = loggy("b"); { await using c = loggy("c"); await using d = loggy("d"); } await using e = loggy("e"); return; // Unreachable. // Never created, never disposed. await using f = loggy("f");}func();// Constructing a// Constructing b// Constructing c// Constructing d// Disposing (async) d// Disposing (async) c// Constructing e// Disposing (async) e// Disposing (async) b// Disposing (async) a
\`\`\`
Defining types in terms of `Disposable` and `AsyncDisposable` can make your code much easier to work with if you expect others to do tear\-down logic consistently.
In fact, lots of existing types exist in the wild which have a `dispose()` or `close()` method.
For example, the Visual Studio Code APIs even define [their own `Disposable` interface](https://code.visualstudio.com/api/references/vscode-api#Disposable).
APIs in the browser and in runtimes like Node.js, Deno, and Bun might also choose to use `Symbol.dispose` and `Symbol.asyncDispose` for objects which already have clean\-up methods, like file handles, connections, and more.

Now maybe this all sounds great for libraries, but a little bit heavy\-weight for your scenarios.
If you’re doing a lot of ad\-hoc clean\-up, creating a new type might introduce a lot of over\-abstraction and questions about best\-practices.
For example, take our `TempFile` example again.

\`\`\`
class TempFile implements Disposable { \#path: string; \#handle: number; constructor(path: string) { this.\#path = path; this.\#handle = fs.openSync(path, "w\+"); } // other methods \[Symbol.dispose]() { // Close the file and delete it. fs.closeSync(this.\#handle); fs.unlinkSync(this.\#path); }}export function doSomeWork() { using file = new TempFile(".some\_temp\_file"); // use file... if (someCondition()) { // do some more work... return; }}
\`\`\`
All we wanted was to remember to call two functions — but was this the best way to write it?
Should we be calling `openSync` in the constructor, create an `open()` method, or pass in the handle ourselves?
Should we expose a method for every possible operation we need to perform, or should we just make the properties public?

That brings us to the final stars of the feature: `DisposableStack` and `AsyncDisposableStack`.
These objects are useful for doing both one\-off clean\-up, along with arbitrary amounts of cleanup.
A `DisposableStack` is an object that has several methods for keeping track of `Disposable` objects, and can be given functions for doing arbitrary clean\-up work.
We can also assign them to `using` variables because — get this — *they’re also `Disposable`*!
So here’s how we could’ve written the original example.

\`\`\`
function doSomeWork() { const path = ".some\_temp\_file"; const file = fs.openSync(path, "w\+"); using cleanup = new DisposableStack(); cleanup.defer(() =\> { fs.closeSync(file); fs.unlinkSync(path); }); // use file... if (someCondition()) { // do some more work... return; } // ...}
\`\`\`
Here, the `defer()` method just takes a callback, and that callback will be run once `cleanup` is disposed of.
Typically, `defer` (and other `DisposableStack` methods like `use` and `adopt`)
should be called immediately after creating a resource.
As the name suggests, `DisposableStack` disposes of everything it keeps track of like a stack, in a first\-in\-last\-out order, so `defer`ing immediately after creating a value helps avoid odd dependency issues.
`AsyncDisposableStack` works similarly, but can keep track of `async` functions and `AsyncDisposable`s, and is itself an `AsyncDisposable.`

The `defer` method is similar in many ways to the `defer` keyword in [Go](https://go.dev/tour/flowcontrol/12), [Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Defer-Statement), [Zig](https://ziglang.org/documentation/master/#defer), [Odin](https://odin-lang.org/docs/overview/#defer-statement), and others, where the conventions should be similar.

Because this feature is so recent, most runtimes will not support it natively.
To use it, you will need runtime polyfills for the following:

* `Symbol.dispose`
* `Symbol.asyncDispose`
* `DisposableStack`
* `AsyncDisposableStack`
* `SuppressedError`

However, if all you’re interested in is `using` and `await using`, you should be able to get away with only polyfilling the built\-in `symbol`s.
Something as simple as the following should work for most cases:

\`\`\`
Symbol.dispose ??= Symbol("Symbol.dispose");Symbol.asyncDispose ??= Symbol("Symbol.asyncDispose");
\`\`\`
You will also need to set your compilation `target` to `es2022` or below, and configure your `lib` setting to either include `"esnext"` or `"esnext.disposable"`.

\`\`\`
{ "compilerOptions": { "target": "es2022", "lib": \["es2022", "esnext.disposable", "dom"] }}
\`\`\`
For more information on this feature, [take a look at the work on GitHub](https://github.com/microsoft/TypeScript/pull/54505)!

## Decorator Metadata

TypeScript 5\.2 implements [an upcoming ECMAScript feature called decorator metadata](https://github.com/tc39/proposal-decorator-metadata).

The key idea of this feature is to make it easy for decorators to create and consume metadata on any class they’re used on or within.

Whenever decorator functions are used, they now have access to a new `metadata` property on their context object.
The `metadata` property just holds a simple object.
Since JavaScript lets us add properties arbitrarily, it can be used as a dictionary that is updated by each decorator.
Alternatively, since every `metadata` object will be identical for each decorated portion of a class, it can be used as a key into a `Map`.
After all decorators on or in a class get run, that object can be accessed on the class via `Symbol.metadata`.

\`\`\`
interface Context { name: string; metadata: Record\;}function setMetadata(\_target: any, context: Context) { context.metadata\[context.name] = true;}class SomeClass { @setMetadata foo = 123; @setMetadata accessor bar = "hello!"; @setMetadata baz() { }}const ourMetadata = SomeClass\[Symbol.metadata];console.log(JSON.stringify(ourMetadata));// { "bar": true, "baz": true, "foo": true }
\`\`\`
This can be useful in a number of different scenarios.
Metadata could possibly be attached for lots of uses like debugging, serialization, or performing dependency injection with decorators.
Since metadata objects are created per decorated class, frameworks can either privately use them as keys into a `Map` or `WeakMap`, or tack properties on as necessary.

For example, let’s say we wanted to use decorators to keep track of which properties and accessors are serializable when using `JSON.stringify` like so:

\`\`\`
import { serialize, jsonify } from "./serializer";class Person { firstName: string; lastName: string; @serialize age: number @serialize get fullName() { return \`${this.firstName} ${this.lastName}\`; } toJSON() { return jsonify(this) } constructor(firstName: string, lastName: string, age: number) { // ... }}
\`\`\`
Here, the intent is that only `age` and `fullName` should be serialized because they are marked with the `@serialize` decorator.
We define a `toJSON` method for this purpose, but it just calls out to `jsonify` which uses the metadata that `@serialize` created.

Here’s an example of how the module `./serialize.ts` might be defined:

\`\`\`
const serializables = Symbol();type Context = \| ClassAccessorDecoratorContext \| ClassGetterDecoratorContext \| ClassFieldDecoratorContext ;export function serialize(\_target: any, context: Context): void { if (context.static \|\| context.private) { throw new Error("Can only serialize public instance members.") } if (typeof context.name === "symbol") { throw new Error("Cannot serialize symbol\-named properties."); } const propNames = (context.metadata\[serializables] as string\[] \| undefined) ??= \[]; propNames.push(context.name);}export function jsonify(instance: object): string { const metadata = instance.constructor\[Symbol.metadata]; const propNames = metadata?.\[serializables] as string\[] \| undefined; if (!propNames) { throw new Error("No members marked with @serialize."); } const pairStrings = propNames.map(key =\> { const strKey = JSON.stringify(key); const strValue = JSON.stringify((instance as any)\[key]); return \`${strKey}: ${strValue}\`; }); return \`{ ${pairStrings.join(", ")} }\`;}
\`\`\`
This module has a local `symbol` called `serializables` to store and retrieve the names of properties marked `@serializable`.
It stores a list of these property names on the metadata on each invocation of `@serializable`.
When `jsonify` is called, the list of properties is fetched off of the metadata and used to retrieve the actual values from the instance, eventually serializing those names and values.

Using a `symbol` technically makes this data accessible to others.
An alternative might be to use a `WeakMap` using the metadata object as a key.
This keeps data private and happens to use fewer type assertions in this case, but is otherwise similar.

\`\`\`
const serializables = new WeakMap\();type Context = \| ClassAccessorDecoratorContext \| ClassGetterDecoratorContext \| ClassFieldDecoratorContext ;export function serialize(\_target: any, context: Context): void { if (context.static \|\| context.private) { throw new Error("Can only serialize public instance members.") } if (typeof context.name !== "string") { throw new Error("Can only serialize string properties."); } let propNames = serializables.get(context.metadata); if (propNames === undefined) { serializables.set(context.metadata, propNames = \[]); } propNames.push(context.name);}export function jsonify(instance: object): string { const metadata = instance.constructor\[Symbol.metadata]; const propNames = metadata \&\& serializables.get(metadata); if (!propNames) { throw new Error("No members marked with @serialize."); } const pairStrings = propNames.map(key =\> { const strKey = JSON.stringify(key); const strValue = JSON.stringify((instance as any)\[key]); return \`${strKey}: ${strValue}\`; }); return \`{ ${pairStrings.join(", ")} }\`;}
\`\`\`
As a note, these implementations don’t handle subclassing and inheritance.
That’s left as an exercise to you (and you might find that it is easier in one version of the file than the other!).

Because this feature is still fresh, most runtimes will not support it natively.
To use it, you will need a polyfill for `Symbol.metadata`.
Something as simple as the following should work for most cases:

\`\`\`
Symbol.metadata ??= Symbol("Symbol.metadata");
\`\`\`
You will also need to set your compilation `target` to `es2022` or below, and configure your `lib` setting to either include `"esnext"` or `"esnext.decorators"`.

\`\`\`
{ "compilerOptions": { "target": "es2022", "lib": \["es2022", "esnext.decorators", "dom"] }}
\`\`\`
We’d like to thank [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) for contributing [the implementation of decorator metadata](https://github.com/microsoft/TypeScript/pull/54657) for TypeScript 5\.2!

## Named and Anonymous Tuple Elements

Tuple types have supported optional labels or names for each element.

\`\`\`
type Pair\ = \[first: T, second: T];
\`\`\`
These labels don’t change what you’re allowed to do with them — they’re solely to help with readability and tooling.

However, TypeScript previously had a rule that tuples could not mix and match between labeled and unlabeled elements.
In other words, either no element could have a label in a tuple, or all elements needed one.

\`\`\`
// ✅ fine \- no labelstype Pair1\ = \[T, T];// ✅ fine \- all fully labeledtype Pair2\ = \[first: T, second: T];// ❌ previously an errortype Pair3\ = \[first: T, T];// \~// Tuple members must all have names// or all not have names.
\`\`\`
This could be annoying for rest elements where we’d be forced to just add a label like `rest` or `tail`.

\`\`\`
// ❌ previously an errortype TwoOrMore\_A\ = \[first: T, second: T, ...T\[]];// \~\~\~\~\~\~// Tuple members must all have names// or all not have names.// ✅type TwoOrMore\_B\ = \[first: T, second: T, rest: ...T\[]];
\`\`\`
It also meant that this restriction had to be enforced internally in the type system, meaning TypeScript would lose labels.

\`\`\`
type HasLabels = \[a: string, b: string];type HasNoLabels = \[number, number];type Merged = \[...HasNoLabels, ...HasLabels];// ^ \[number, number, string, string]//// 'a' and 'b' were lost in 'Merged'
\`\`\`
In TypeScript 5\.2, the all\-or\-nothing restriction on tuple labels has been lifted.
The language can now also preserve labels when spreading into an unlabeled tuple.

We’d like to extend our thanks to [Josh Goldberg](https://github.com/JoshuaKGoldberg) and [Mateusz Burzyński](https://github.com/Andarist) who [collaborated to lift this restriction](https://github.com/microsoft/TypeScript/pull/53356).

## Easier Method Usage for Unions of Arrays

In previous versions of TypeScript, calling a method on a union of arrays could end in pain.

\`\`\`
declare let array: string\[] \| number\[];array.filter(x =\> !!x);// \~\~\~\~\~\~ error!// This expression is not callable.// Each member of the union type '...' has signatures,// but none of those signatures are compatible// with each other.
\`\`\`
In this example, TypeScript would try to see if each version of `filter` is compatible across `string[]` and `number[]`.
Without a coherent strategy, TypeScript threw its hands in the air and said “I can’t make it work”.

In TypeScript 5\.2, before giving up in these cases, unions of arrays are treated as a special case.
A new array type is constructed out of each member’s element type, and then the method is invoked on that.

Taking the above example, `string[] | number[]` is transformed into `(string | number)[]` (or `Array`), and `filter` is invoked on that type.
There is a slight caveat which is that `filter` will produce an `Array` instead of a `string[] | number[]`;
but for a freshly produced value there is less risk of something “going wrong”.

This means lots of methods like `filter`, `find`, `some`, `every`, and `reduce` should all be invokable on unions of arrays in cases where they were not previously.

You can [read up more details on the implementing pull request](https://github.com/microsoft/TypeScript/pull/53489).

## Type\-Only Import Paths with TypeScript Implementation File Extensions

TypeScript now allows both declaration *and* implementation file extensions to be included in type\-only import paths, regardless of whether `allowImportingTsExtensions` is enabled.

This means that you can now write `import type` statements that use `.ts`, `.mts`, `.cts`, and `.tsx` file extensions.

\`\`\`
import type { JustAType } from "./justTypes.ts";export function f(param: JustAType) { // ...}
\`\`\`
It also means that `import()` types, which can be used in both TypeScript and JavaScript with JSDoc, can use those file extensions.

\`\`\`
/\*\* \* @param {import("./justTypes.ts").JustAType} param \*/export function f(param) { // ...}
\`\`\`
For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/54746).

## Comma Completions for Object Members

It can be easy to forget to add a comma when adding a new property to an object.
Previously, if you forgot a comma and requested auto\-completion, TypeScript would confusingly give poor unrelated completion results.

TypeScript 5\.2 now gracefully provides object member completions when you’re missing a comma.
But to just skip past hitting you with a syntax error, it will *also* auto\-insert the missing comma.



For more information, [see the implementation here](https://github.com/microsoft/TypeScript/pull/52899).

## Inline Variable Refactoring

TypeScript 5\.2 now has a refactoring to inline the contents of a variable to all usage sites.

.

Using the “inline variable” refactoring will eliminate the variable and replace all the variable’s usages with its initializer.
Note that this may cause that initializer’s side\-effects to run at a different time, and as many times as the variable has been used.

For more details, [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/54281).

## Optimized Checks for Ongoing Type Compatibility

Because TypeScript is a structural type system, types occasionally need to be compared in a member\-wise fashion;
however, recursive types add some issues here.
For example:

\`\`\`
interface A { value: A; other: string;}interface B { value: B; other: number;}
\`\`\`
When checking whether the type `A` is compatible with the type `B`, TypeScript will end up checking whether the types of `value` in `A` and `B` are respectively compatible.
At this point, the type system needs to stop checking any further and proceed to check other members.
To do this, the type system has to track when any two types are already being related.

Previously TypeScript already kept a stack of type pairs, and iterated through that to determine whether those types are being related.
When this stack is shallow that’s not a problem; but when the stack isn’t shallow, that, uh, [is a problem](https://accidentallyquadratic.tumblr.com/).

In TypeScript 5\.3, a simple `Set` helps track this information.
This reduced the time spent on a reported test case that used the [drizzle](https://github.com/drizzle-team/drizzle-orm) library by over 33%!

\`\`\`
Benchmark 1: old Time (mean ± σ): 3\.115 s ± 0\.067 s \[User: 4\.403 s, System: 0\.124 s] Range (min … max): 3\.018 s … 3\.196 s 10 runs Benchmark 2: new Time (mean ± σ): 2\.072 s ± 0\.050 s \[User: 3\.355 s, System: 0\.135 s] Range (min … max): 1\.985 s … 2\.150 s 10 runs Summary 'new' ran 1\.50 ± 0\.05 times faster than 'old'
\`\`\`
[Read more on the change here](https://github.com/microsoft/TypeScript/pull/55224).

## Breaking Changes and Correctness Fixes

TypeScript strives not to unnecessarily introduce breaks;
however, occasionally we must make corrections and improvements so that code can be better\-analyzed.

### `lib.d.ts` Changes

Types generated for the DOM may have an impact on your codebase.
For more information, [see the DOM updates for TypeScript 5\.2](https://github.com/microsoft/TypeScript/pull/54725).

### `labeledElementDeclarations` May Hold `undefined` Elements

In order [to support a mixture of labeled and unlabeled elements](https://github.com/microsoft/TypeScript/pull/53356), TypeScript’s API has changed slightly.
The `labeledElementDeclarations` property of `TupleType` may hold `undefined` for at each position where an element is unlabeled.

\`\`\`
 interface TupleType {\- labeledElementDeclarations?: readonly (NamedTupleMember \| ParameterDeclaration)\[];\+ labeledElementDeclarations?: readonly (NamedTupleMember \| ParameterDeclaration \| undefined)\[]; }
\`\`\`
### `module` and `moduleResolution` Must Match Under Recent Node.js settings

The `--module` and `--moduleResolution` options each support a `node16` and `nodenext` setting.
These are effectively “modern Node.js” settings that should be used on any recent Node.js project.
What we’ve found is that when these two options don’t agree on whether they are using Node.js\-related settings, projects are effectively misconfigured.

In TypeScript 5\.2, when using `node16` or `nodenext` for either of the `--module` and `--moduleResolution` options, TypeScript now requires the other to have a similar Node.js\-related setting.
In cases where the settings diverge, you’ll likely get an error message like either

\`\`\`
Option 'moduleResolution' must be set to 'NodeNext' (or left unspecified) when option 'module' is set to 'NodeNext'.
\`\`\`
or

\`\`\`
Option 'module' must be set to 'Node16' when option 'moduleResolution' is set to 'Node16'.
\`\`\`
So for example `--module esnext --moduleResolution node16` will be rejected — but you may be better off just using `--module nodenext` alone, or `--module esnext --moduleResolution bundler`.

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/54567).

### Consistent Export Checking for Merged Symbols

When two declarations merge, they must agree on whether they are both exported.
Due to a bug, TypeScript missed specific cases in ambient contexts, like in declaration files or `declare module` blocks.
For example, it would not issue an error on a case like the following, where `replaceInFile` is declared once as an exported function, and one as an un\-exported namespace.

\`\`\`
declare module 'replace\-in\-file' { export function replaceInFile(config: unknown): Promise\; export {}; namespace replaceInFile { export function sync(config: unknown): unknown\[]; }}
\`\`\`
In an ambient module, adding an `export { ... }` or a similar construct like `export default ...` implicitly changes whether all declarations are automatically exported.
TypeScript now recognizes these unfortunately confusing semantics more consistently, and issues an error on the fact that all declarations of `replaceInFile` need to agree in their modifiers, and will issue the following error:

\`\`\`
Individual declarations in merged declaration 'replaceInFile' must be all exported or all local.
\`\`\`
For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/54659).

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 5.2.md) ❤

Contributors to this page:  
ABEILast updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 5.0

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html)

Was this page helpful?

# TypeScript 5\.0

## Decorators

Decorators are an upcoming ECMAScript feature that allow us to customize classes and their members in a reusable way.

Let’s consider the following code:

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; } greet() { console.log(\`Hello, my name is ${this.name}.\`); }}const p = new Person("Ray");p.greet();
\`\`\`
`greet` is pretty simple here, but let’s imagine it’s something way more complicated \- maybe it does some async logic, it’s recursive, it has side effects, etc.
Regardless of what kind of ball\-of\-mud you’re imagining, let’s say you throw in some `console.log` calls to help debug `greet`.

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; } greet() { console.log("LOG: Entering method."); console.log(\`Hello, my name is ${this.name}.\`); console.log("LOG: Exiting method.") }}
\`\`\`
This pattern is fairly common.
It sure would be nice if there was a way we could do this for every method!

This is where decorators come in.
We can write a function called `loggedMethod` that looks like the following:

\`\`\`
function loggedMethod(originalMethod: any, \_context: any) { function replacementMethod(this: any, ...args: any\[]) { console.log("LOG: Entering method.") const result = originalMethod.call(this, ...args); console.log("LOG: Exiting method.") return result; } return replacementMethod;}
\`\`\`
“What’s the deal with all of these `any`s?
What is this, `any`Script!?”

Just be patient \- we’re keeping things simple for now so that we can focus on what this function is doing.
Notice that `loggedMethod` takes the original method (`originalMethod`) and returns a function that

1. logs an “Entering…” message
2. passes along `this` and all of its arguments to the original method
3. logs an “Exiting…” message, and
4. returns whatever the original method returned.

Now we can use `loggedMethod` to *decorate* the method `greet`:

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; } @loggedMethod greet() { console.log(\`Hello, my name is ${this.name}.\`); }}const p = new Person("Ray");p.greet();// Output://// LOG: Entering method.// Hello, my name is Ray.// LOG: Exiting method.
\`\`\`
We just used `loggedMethod` as a decorator above `greet` \- and notice that we wrote it as `@loggedMethod`.
When we did that, it got called with the method *target* and a *context object*.
Because `loggedMethod` returned a new function, that function replaced the original definition of `greet`.

We didn’t mention it yet, but `loggedMethod` was defined with a second parameter.
It’s called a “context object”, and it has some useful information about how the decorated method was declared \- like whether it was a `#private` member, or `static`, or what the name of the method was.
Let’s rewrite `loggedMethod` to take advantage of that and print out the name of the method that was decorated.

\`\`\`
function loggedMethod(originalMethod: any, context: ClassMethodDecoratorContext) { const methodName = String(context.name); function replacementMethod(this: any, ...args: any\[]) { console.log(\`LOG: Entering method '${methodName}'.\`) const result = originalMethod.call(this, ...args); console.log(\`LOG: Exiting method '${methodName}'.\`) return result; } return replacementMethod;}
\`\`\`
We’re now using the context parameter \- and that it’s the first thing in `loggedMethod` that has a type stricter than `any` and `any[]`.
TypeScript provides a type called `ClassMethodDecoratorContext` that models the context object that method decorators take.

Apart from metadata, the context object for methods also has a useful function called `addInitializer`.
It’s a way to hook into the beginning of the constructor (or the initialization of the class itself if we’re working with `static`s).

As an example \- in JavaScript, it’s common to write something like the following pattern:

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; this.greet = this.greet.bind(this); } greet() { console.log(\`Hello, my name is ${this.name}.\`); }}
\`\`\`
Alternatively, `greet` might be declared as a property initialized to an arrow function.

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; } greet = () =\> { console.log(\`Hello, my name is ${this.name}.\`); };}
\`\`\`
This code is written to ensure that `this` isn’t re\-bound if `greet` is called as a stand\-alone function or passed as a callback.

\`\`\`
const greet = new Person("Ray").greet;// We don't want this to fail!greet();
\`\`\`
We can write a decorator that uses `addInitializer` to call `bind` in the constructor for us.

\`\`\`
function bound(originalMethod: any, context: ClassMethodDecoratorContext) { const methodName = context.name; if (context.private) { throw new Error(\`'bound' cannot decorate private properties like ${methodName as string}.\`); } context.addInitializer(function () { this\[methodName] = this\[methodName].bind(this); });}
\`\`\`
`bound` isn’t returning anything \- so when it decorates a method, it leaves the original alone.
Instead, it will add logic before any other fields are initialized.

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; } @bound @loggedMethod greet() { console.log(\`Hello, my name is ${this.name}.\`); }}const p = new Person("Ray");const greet = p.greet;// Works!greet();
\`\`\`
Notice that we stacked two decorators \- `@bound` and `@loggedMethod`.
These decorations run in “reverse order”.
That is, `@loggedMethod` decorates the original method `greet`, and `@bound` decorates the result of `@loggedMethod`.
In this example, it doesn’t matter \- but it could if your decorators have side\-effects or expect a certain order.

Also worth noting \- if you’d prefer stylistically, you can put these decorators on the same line.

\`\`\`
 @bound @loggedMethod greet() { console.log(\`Hello, my name is ${this.name}.\`); }
\`\`\`
Something that might not be obvious is that we can even make functions that *return* decorator functions.
That makes it possible to customize the final decorator just a little.
If we wanted, we could have made `loggedMethod` return a decorator and customize how it logs its messages.

\`\`\`
function loggedMethod(headMessage = "LOG:") { return function actualDecorator(originalMethod: any, context: ClassMethodDecoratorContext) { const methodName = String(context.name); function replacementMethod(this: any, ...args: any\[]) { console.log(\`${headMessage} Entering method '${methodName}'.\`) const result = originalMethod.call(this, ...args); console.log(\`${headMessage} Exiting method '${methodName}'.\`) return result; } return replacementMethod; }}
\`\`\`
If we did that, we’d have to call `loggedMethod` before using it as a decorator.
We could then pass in any string as the prefix for messages that get logged to the console.

\`\`\`
class Person { name: string; constructor(name: string) { this.name = name; } @loggedMethod("⚠️") greet() { console.log(\`Hello, my name is ${this.name}.\`); }}const p = new Person("Ray");p.greet();// Output://// ⚠️ Entering method 'greet'.// Hello, my name is Ray.// ⚠️ Exiting method 'greet'.
\`\`\`
Decorators can be used on more than just methods!
They can be used on properties/fields, getters, setters, and auto\-accessors.
Even classes themselves can be decorated for things like subclassing and registration.

To learn more about decorators in\-depth, you can read up on [Axel Rauschmayer’s extensive summary](https://2ality.com/2022/10/javascript-decorators.html).

For more information about the changes involved, you can [view the original pull request](https://github.com/microsoft/TypeScript/pull/50820).

### Differences with Experimental Legacy Decorators

If you’ve been using TypeScript for a while, you might be aware of the fact that it’s had support for “experimental” decorators for years.
While these experimental decorators have been incredibly useful, they modeled a much older version of the decorators proposal, and always required an opt\-in compiler flag called `--experimentalDecorators`.
Any attempt to use decorators in TypeScript without this flag used to prompt an error message.

`--experimentalDecorators` will continue to exist for the foreseeable future;
however, without the flag, decorators will now be valid syntax for all new code.
Outside of `--experimentalDecorators`, they will be type\-checked and emitted differently.
The type\-checking rules and emit are sufficiently different that while decorators *can* be written to support both the old and new decorators behavior, any existing decorator functions are not likely to do so.

This new decorators proposal is not compatible with `--emitDecoratorMetadata`, and it does not allow decorating parameters.
Future ECMAScript proposals may be able to help bridge that gap.

On a final note: in addition to allowing decorators to be placed before the `export` keyword, the proposal for decorators now provides the option of placing decorators after `export` or `export default`.
The only exception is that mixing the two styles is not allowed.

\`\`\`
// ✅ allowed@register export default class Foo { // ...}// ✅ also allowedexport default @register class Bar { // ...}// ❌ error \- before \*and\* after is not allowed@before export @after class Bar { // ...}
\`\`\`
### Writing Well\-Typed Decorators

The `loggedMethod` and `bound` decorator examples above are intentionally simple and omit lots of details about types.

Typing decorators can be fairly complex.
For example, a well\-typed version of `loggedMethod` from above might look something like this:

\`\`\`
function loggedMethod\( target: (this: This, ...args: Args) =\> Return, context: ClassMethodDecoratorContext\ Return\>) { const methodName = String(context.name); function replacementMethod(this: This, ...args: Args): Return { console.log(\`LOG: Entering method '${methodName}'.\`) const result = target.call(this, ...args); console.log(\`LOG: Exiting method '${methodName}'.\`) return result; } return replacementMethod;}
\`\`\`
We had to separately model out the type of `this`, the parameters, and the return type of the original method, using the type parameters `This`, `Args`, and `Return`.

Exactly how complex your decorators functions are defined depends on what you want to guarantee.
Just keep in mind, your decorators will be used more than they’re written, so a well\-typed version will usually be preferable \- but there’s clearly a trade\-off with readability, so try to keep things simple.

More documentation on writing decorators will be available in the future \- but [this post](https://2ality.com/2022/10/javascript-decorators.html) should have a good amount of detail for the mechanics of decorators.

## `const` Type Parameters

When inferring the type of an object, TypeScript will usually choose a type that’s meant to be general.
For example, in this case, the inferred type of `names` is `string[]`:

\`\`\`
type HasNames = { names: readonly string\[] };function getNamesExactly\(arg: T): T\["names"] { return arg.names;}// Inferred type: string\[]const names = getNamesExactly({ names: \["Alice", "Bob", "Eve"]});
\`\`\`
Usually the intent of this is to enable mutation down the line.

However, depending on what exactly `getNamesExactly` does and how it’s intended to be used, it can often be the case that a more\-specific type is desired.

Up until now, API authors have typically had to recommend adding `as const` in certain places to achieve the desired inference:

\`\`\`
// The type we wanted:// readonly \["Alice", "Bob", "Eve"]// The type we got:// string\[]const names1 = getNamesExactly({ names: \["Alice", "Bob", "Eve"]});// Correctly gets what we wanted:// readonly \["Alice", "Bob", "Eve"]const names2 = getNamesExactly({ names: \["Alice", "Bob", "Eve"]} as const);
\`\`\`
This can be cumbersome and easy to forget.
In TypeScript 5\.0, you can now add a `const` modifier to a type parameter declaration to cause `const`\-like inference to be the default:

\`\`\`
type HasNames = { names: readonly string\[] };function getNamesExactly\(arg: T): T\["names"] {// ^^^^^ return arg.names;}// Inferred type: readonly \["Alice", "Bob", "Eve"]// Note: Didn't need to write 'as const' hereconst names = getNamesExactly({ names: \["Alice", "Bob", "Eve"] });
\`\`\`
Note that the `const` modifier doesn’t *reject* mutable values, and doesn’t require immutable constraints.
Using a mutable type constraint might give surprising results.
For example:

\`\`\`
declare function fnBad\(args: T): void;// 'T' is still 'string\[]' since 'readonly \["a", "b", "c"]' is not assignable to 'string\[]'fnBad(\["a", "b" ,"c"]);
\`\`\`
Here, the inferred candidate for `T` is `readonly ["a", "b", "c"]`, and a `readonly` array can’t be used where a mutable one is needed.
In this case, inference falls back to the constraint, the array is treated as `string[]`, and the call still proceeds successfully.

A better definition of this function should use `readonly string[]`:

\`\`\`
declare function fnGood\(args: T): void;// T is readonly \["a", "b", "c"]fnGood(\["a", "b" ,"c"]);
\`\`\`
Similarly, remember to keep in mind that the `const` modifier only affects inference of object, array and primitive expressions that were written within the call, so arguments which wouldn’t (or couldn’t) be modified with `as const` won’t see any change in behavior:

\`\`\`
declare function fnGood\(args: T): void;const arr = \["a", "b" ,"c"];// 'T' is still 'string\[]'\-\- the 'const' modifier has no effect herefnGood(arr);
\`\`\`
[See the pull request](https://github.com/microsoft/TypeScript/pull/51865) and the ([first](https://github.com/microsoft/TypeScript/issues/30680) and second [second](https://github.com/microsoft/TypeScript/issues/41114)) motivating issues for more details.

## Supporting Multiple Configuration Files in `extends`

When managing multiple projects, it can be helpful to have a “base” configuration file that other `tsconfig.json` files can extend from.
That’s why TypeScript supports an `extends` field for copying over fields from `compilerOptions`.

\`\`\`
// packages/front\-end/src/tsconfig.json{ "extends": "../../../tsconfig.base.json", "compilerOptions": { "outDir": "../lib", // ... }}
\`\`\`
However, there are scenarios where you might want to extend from multiple configuration files.
For example, imagine using [a TypeScript base configuration file shipped to npm](https://github.com/tsconfig/bases).
If you want all your projects to also use the options from the `@tsconfig/strictest` package on npm, then there’s a simple solution: have `tsconfig.base.json` extend from `@tsconfig/strictest`:

\`\`\`
// tsconfig.base.json{ "extends": "@tsconfig/strictest/tsconfig.json", "compilerOptions": { // ... }}
\`\`\`
This works to a point.
If you have any projects that *don’t* want to use `@tsconfig/strictest`, they have to either manually disable the options, or create a separate version of `tsconfig.base.json` that *doesn’t* extend from `@tsconfig/strictest`.

To give some more flexibility here, Typescript 5\.0 now allows the `extends` field to take multiple entries.
For example, in this configuration file:

\`\`\`
{ "extends": \["a", "b", "c"], "compilerOptions": { // ... }}
\`\`\`
Writing this is kind of like extending `c` directly, where `c` extends `b`, and `b` extends `a`.
If any fields “conflict”, the latter entry wins.

So in the following example, both `strictNullChecks` and `noImplicitAny` are enabled in the final `tsconfig.json`.

\`\`\`
// tsconfig1\.json{ "compilerOptions": { "strictNullChecks": true }}// tsconfig2\.json{ "compilerOptions": { "noImplicitAny": true }}// tsconfig.json{ "extends": \["./tsconfig1\.json", "./tsconfig2\.json"], "files": \["./index.ts"]}
\`\`\`
As another example, we can rewrite our original example in the following way.

\`\`\`
// packages/front\-end/src/tsconfig.json{ "extends": \["@tsconfig/strictest/tsconfig.json", "../../../tsconfig.base.json"], "compilerOptions": { "outDir": "../lib", // ... }}
\`\`\`
For more details, [read more on the original pull request](https://github.com/microsoft/TypeScript/pull/50403).

## All `enum`s Are Union `enum`s

When TypeScript originally introduced enums, they were nothing more than a set of numeric constants with the same type.

\`\`\`
enum E { Foo = 10, Bar = 20,}
\`\`\`
The only thing special about `E.Foo` and `E.Bar` was that they were assignable to anything expecting the type `E`.
Other than that, they were pretty much just `number`s.

\`\`\`
function takeValue(e: E) {}takeValue(E.Foo); // workstakeValue(123\); // error!
\`\`\`
It wasn’t until TypeScript 2\.0 introduced enum literal types that enums got a bit more special.
Enum literal types gave each enum member its own type, and turned the enum itself into a *union* of each member type.
They also allowed us to refer to only a subset of the types of an enum, and to narrow away those types.

\`\`\`
// Color is like a union of Red \| Orange \| Yellow \| Green \| Blue \| Violetenum Color { Red, Orange, Yellow, Green, Blue, /\* Indigo, \*/ Violet}// Each enum member has its own type that we can refer to!type PrimaryColor = Color.Red \| Color.Green \| Color.Blue;function isPrimaryColor(c: Color): c is PrimaryColor { // Narrowing literal types can catch bugs. // TypeScript will error here because // we'll end up comparing 'Color.Red' to 'Color.Green'. // We meant to use \|\|, but accidentally wrote \&\&. return c === Color.Red \&\& c === Color.Green \&\& c === Color.Blue;}
\`\`\`
One issue with giving each enum member its own type was that those types were in some part associated with the actual value of the member.
In some cases it’s not possible to compute that value \- for instance, an enum member could be initialized by a function call.

\`\`\`
enum E { Blah = Math.random()}
\`\`\`
Whenever TypeScript ran into these issues, it would quietly back out and use the old enum strategy.
That meant giving up all the advantages of unions and literal types.

TypeScript 5\.0 manages to make all enums into union enums by creating a unique type for each computed member.
That means that all enums can now be narrowed and have their members referenced as types as well.

For more details on this change, you can [read the specifics on GitHub](https://github.com/microsoft/TypeScript/pull/50528).

## `--moduleResolution bundler`

TypeScript 4\.7 introduced the `node16` and `nodenext` options for its `--module` and `--moduleResolution` settings.
The intent of these options was to better model the precise lookup rules for ECMAScript modules in Node.js;
however, this mode has many restrictions that other tools don’t really enforce.

For example, in an ECMAScript module in Node.js, any relative import needs to include a file extension.

\`\`\`
// entry.mjsimport \* as utils from "./utils"; // ❌ wrong \- we need to include the file extension.import \* as utils from "./utils.mjs"; // ✅ works
\`\`\`
There are certain reasons for this in Node.js and the browser \- it makes file lookups faster and works better for naive file servers.
But for many developers using tools like bundlers, the `node16`/`nodenext` settings were cumbersome because bundlers don’t have most of these restrictions.
In some ways, the `node` resolution mode was better for anyone using a bundler.

But in some ways, the original `node` resolution mode was already out of date.
Most modern bundlers use a fusion of the ECMAScript module and CommonJS lookup rules in Node.js.
For example, extensionless imports work just fine just like in CommonJS, but when looking through the [`export` conditions](https://nodejs.org/api/packages.html#nested-conditions) of a package, they’ll prefer an `import` condition just like in an ECMAScript file.

To model how bundlers work, TypeScript now introduces a new strategy: `--moduleResolution bundler`.

\`\`\`
{ "compilerOptions": { "target": "esnext", "moduleResolution": "bundler" }}
\`\`\`
If you are using a modern bundler like Vite, esbuild, swc, Webpack, Parcel, and others that implement a hybrid lookup strategy, the new `bundler` option should be a good fit for you.

On the other hand, if you’re writing a library that’s meant to be published on npm, using the `bundler` option can hide compatibility issues that may arise for your users who *aren’t* using a bundler.
So in these cases, using the `node16` or `nodenext` resolution options is likely to be a better path.

To read more on `--moduleResolution bundler`, [take a look at the implementing pull request](https://github.com/microsoft/TypeScript/pull/51669).

## Resolution Customization Flags

JavaScript tooling may now model “hybrid” resolution rules, like in the `bundler` mode we described above.
Because tools may differ in their support slightly, TypeScript 5\.0 provides ways to enable or disable a few features that may or may not work with your configuration.

### `allowImportingTsExtensions`

`--allowImportingTsExtensions` allows TypeScript files to import each other with a TypeScript\-specific extension like `.ts`, `.mts`, or `.tsx`.

This flag is only allowed when `--noEmit` or `--emitDeclarationOnly` is enabled, since these import paths would not be resolvable at runtime in JavaScript output files.
The expectation here is that your resolver (e.g. your bundler, a runtime, or some other tool) is going to make these imports between `.ts` files work.

### `resolvePackageJsonExports`

`--resolvePackageJsonExports` forces TypeScript to consult [the `exports` field of `package.json` files](https://nodejs.org/api/packages.html#exports) if it ever reads from a package in `node_modules`.

This option defaults to `true` under the `node16`, `nodenext`, and `bundler` options for `--moduleResolution`.

### `resolvePackageJsonImports`

`--resolvePackageJsonImports` forces TypeScript to consult [the `imports` field of `package.json` files](https://nodejs.org/api/packages.html#imports) when performing a lookup that starts with `#` from a file whose ancestor directory contains a `package.json`.

This option defaults to `true` under the `node16`, `nodenext`, and `bundler` options for `--moduleResolution`.

### `allowArbitraryExtensions`

In TypeScript 5\.0, when an import path ends in an extension that isn’t a known JavaScript or TypeScript file extension, the compiler will look for a declaration file for that path in the form of `{file basename}.d.{extension}.ts`.
For example, if you are using a CSS loader in a bundler project, you might want to write (or generate) declaration files for those stylesheets:

\`\`\`
/\* app.css \*/.cookie\-banner { display: none;}
\`\`\`
\`\`\`
// app.d.css.tsdeclare const css: { cookieBanner: string;};export default css;
\`\`\`
\`\`\`
// App.tsximport styles from "./app.css";styles.cookieBanner; // string
\`\`\`
By default, this import will raise an error to let you know that TypeScript doesn’t understand this file type and your runtime might not support importing it.
But if you’ve configured your runtime or bundler to handle it, you can suppress the error with the new `--allowArbitraryExtensions` compiler option.

Note that historically, a similar effect has often been achievable by adding a declaration file named `app.css.d.ts` instead of `app.d.css.ts` \- however, this just worked through Node’s `require` resolution rules for CommonJS.
Strictly speaking, the former is interpreted as a declaration file for a JavaScript file named `app.css.js`.
Because relative files imports need to include extensions in Node’s ESM support, TypeScript would error on our example in an ESM file under `--moduleResolution node16` or `nodenext`.

For more information, read up [the proposal for this feature](https://github.com/microsoft/TypeScript/issues/50133) and [its corresponding pull request](https://github.com/microsoft/TypeScript/pull/51435).

### `customConditions`

`--customConditions` takes a list of additional [conditions](https://nodejs.org/api/packages.html#nested-conditions) that should succeed when TypeScript resolves from an [`exports`](https://nodejs.org/api/packages.html#exports) or [`imports`](https://nodejs.org/api/packages.html#imports) field of a `package.json`.
These conditions are added to whatever existing conditions a resolver will use by default.

For example, when this field is set in a `tsconfig.json` as so:

\`\`\`
{ "compilerOptions": { "target": "es2022", "moduleResolution": "bundler", "customConditions": \["my\-condition"] }}
\`\`\`
Any time an `exports` or `imports` field is referenced in `package.json`, TypeScript will consider conditions called `my-condition`.

So when importing from a package with the following `package.json`

\`\`\`
{ // ... "exports": { ".": { "my\-condition": "./foo.mjs", "node": "./bar.mjs", "import": "./baz.mjs", "require": "./biz.mjs" } }}
\`\`\`
TypeScript will try to look for files corresponding to `foo.mjs`.

This field is only valid under the `node16`, `nodenext`, and `bundler` options for `--moduleResolution`

## `--verbatimModuleSyntax`

By default, TypeScript does something called *import elision*.
Basically, if you write something like

\`\`\`
import { Car } from "./car";export function drive(car: Car) { // ...}
\`\`\`
TypeScript detects that you’re only using an import for types and drops the import entirely.
Your output JavaScript might look something like this:

\`\`\`
export function drive(car) { // ...}
\`\`\`
Most of the time this is good, because if `Car` isn’t a value that’s exported from `./car`, we’ll get a runtime error.

But it does add a layer of complexity for certain edge cases.
For example, notice there’s no statement like `import "./car";` \- the import was dropped entirely.
That actually makes a difference for modules that have side\-effects or not.

TypeScript’s emit strategy for JavaScript also has another few layers of complexity \- import elision isn’t always just driven by how an import is used \- it often consults how a value is declared as well.
So it’s not always clear whether code like the following

\`\`\`
export { Car } from "./car";
\`\`\`
should be preserved or dropped.
If `Car` is declared with something like a `class`, then it can be preserved in the resulting JavaScript file.
But if `Car` is only declared as a `type` alias or `interface`, then the JavaScript file shouldn’t export `Car` at all.

While TypeScript might be able to make these emit decisions based on information from across files, not every compiler can.

The `type` modifier on imports and exports helps with these situations a bit.
We can make it explicit whether an import or export is only being used for type analysis, and can be dropped entirely in JavaScript files by using the `type` modifier.

\`\`\`
// This statement can be dropped entirely in JS outputimport type \* as car from "./car";// The named import/export 'Car' can be dropped in JS outputimport { type Car } from "./car";export { type Car } from "./car";
\`\`\`
`type` modifiers are not quite useful on their own \- by default, module elision will still drop imports, and nothing forces you to make the distinction between `type` and plain imports and exports.
So TypeScript has the flag `--importsNotUsedAsValues` to make sure you use the `type` modifier, `--preserveValueImports` to prevent *some* module elision behavior, and `--isolatedModules` to make sure that your TypeScript code works across different compilers.
Unfortunately, understanding the fine details of those 3 flags is hard, and there are still some edge cases with unexpected behavior.

TypeScript 5\.0 introduces a new option called `--verbatimModuleSyntax` to simplify the situation.
The rules are much simpler \- any imports or exports without a `type` modifier are left around.
Anything that uses the `type` modifier is dropped entirely.

\`\`\`
// Erased away entirely.import type { A } from "a";// Rewritten to 'import { b } from "bcd";'import { b, type c, type d } from "bcd";// Rewritten to 'import {} from "xyz";'import { type xyz } from "xyz";
\`\`\`
With this new option, what you see is what you get.

That does have some implications when it comes to module interop though.
Under this flag, ECMAScript `import`s and `export`s won’t be rewritten to `require` calls when your settings or file extension implied a different module system.
Instead, you’ll get an error.
If you need to emit code that uses `require` and `module.exports`, you’ll have to use TypeScript’s module syntax that predates ES2015:

| Input TypeScript | Output JavaScript |
| --- | --- |
| \`\`\` import foo = require("foo"); \`\`\` | \`\`\` const foo = require("foo"); \`\`\` |
| \`\`\` function foo() {}function bar() {}function baz() {}export = { foo, bar, baz}; \`\`\` | \`\`\` function foo() {}function bar() {}function baz() {}module.exports = { foo, bar, baz}; \`\`\` |

While this is a limitation, it does help make some issues more obvious.
For example, it’s very common to forget to set the [`type` field in `package.json`](https://nodejs.org/api/packages.html#type) under `--module node16`.
As a result, developers would start writing CommonJS modules instead of ES modules without realizing it, giving surprising lookup rules and JavaScript output.
This new flag ensures that you’re intentional about the file type you’re using because the syntax is intentionally different.

Because `--verbatimModuleSyntax` provides a more consistent story than `--importsNotUsedAsValues` and `--preserveValueImports`, those two existing flags are being deprecated in its favor.

For more details, read up on \[the original pull request] and [its proposal issue](https://github.com/microsoft/TypeScript/issues/51479).

## Support for `export type *`

When TypeScript 3\.8 introduced type\-only imports, the new syntax wasn’t allowed on `export * from "module"` or `export * as ns from "module"` re\-exports. TypeScript 5\.0 adds support for both of these forms:

\`\`\`
// models/vehicles.tsexport class Spaceship { // ...}// models/index.tsexport type \* as vehicles from "./vehicles";// main.tsimport { vehicles } from "./models";function takeASpaceship(s: vehicles.Spaceship) { // ✅ ok \- \`vehicles\` only used in a type position}function makeASpaceship() { return new vehicles.Spaceship(); // ^^^^^^^^ // 'vehicles' cannot be used as a value because it was exported using 'export type'.}
\`\`\`
You can [read more about the implementation here](https://github.com/microsoft/TypeScript/pull/52217).

## `@satisfies` Support in JSDoc

TypeScript 4\.9 introduced the `satisfies` operator.
It made sure that the type of an expression was compatible, without affecting the type itself.
For example, let’s take the following code:

\`\`\`
interface CompilerOptions { strict?: boolean; outDir?: string; // ...}interface ConfigSettings { compilerOptions?: CompilerOptions; extends?: string \| string\[]; // ...}let myConfigSettings = { compilerOptions: { strict: true, outDir: "../lib", // ... }, extends: \[ "@tsconfig/strictest/tsconfig.json", "../../../tsconfig.base.json" ],} satisfies ConfigSettings;
\`\`\`
Here, TypeScript knows that `myConfigSettings.extends` was declared with an array \- because while `satisfies` validated the type of our object, it didn’t bluntly change it to `CompilerOptions` and lose information.
So if we want to map over `extends`, that’s fine.

\`\`\`
declare function resolveConfig(configPath: string): CompilerOptions;let inheritedConfigs = myConfigSettings.extends.map(resolveConfig);
\`\`\`
This was helpful for TypeScript users, but plenty of people use TypeScript to type\-check their JavaScript code using JSDoc annotations.
That’s why TypeScript 5\.0 is supporting a new JSDoc tag called `@satisfies` that does exactly the same thing.

`/** @satisfies */` can catch type mismatches:

\`\`\`
// @ts\-check/\*\* \* @typedef CompilerOptions \* @prop {boolean} \[strict] \* @prop {string} \[outDir] \*//\*\* \* @satisfies {CompilerOptions} \*/let myCompilerOptions = { outdir: "../lib",// \~\~\~\~\~\~ oops! we meant outDir};
\`\`\`
But it will preserve the original type of our expressions, allowing us to use our values more precisely later on in our code.

\`\`\`
// @ts\-check/\*\* \* @typedef CompilerOptions \* @prop {boolean} \[strict] \* @prop {string} \[outDir] \*//\*\* \* @typedef ConfigSettings \* @prop {CompilerOptions} \[compilerOptions] \* @prop {string \| string\[]} \[extends] \*//\*\* \* @satisfies {ConfigSettings} \*/let myConfigSettings = { compilerOptions: { strict: true, outDir: "../lib", }, extends: \[ "@tsconfig/strictest/tsconfig.json", "../../../tsconfig.base.json" ],};let inheritedConfigs = myConfigSettings.extends.map(resolveConfig);
\`\`\`
`/** @satisfies */` can also be used inline on any parenthesized expression.
We could have written `myCompilerOptions` like this:

\`\`\`
let myConfigSettings = /\*\* @satisfies {ConfigSettings} \*/ ({ compilerOptions: { strict: true, outDir: "../lib", }, extends: \[ "@tsconfig/strictest/tsconfig.json", "../../../tsconfig.base.json" ],});
\`\`\`
Why?
Well, it usually makes more sense when you’re deeper in some other code, like a function call.

\`\`\`
compileCode(/\*\* @satisfies {CompilerOptions} \*/ ({ // ...}));
\`\`\`
[This feature](https://github.com/microsoft/TypeScript/pull/51753) was provided thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk)!

## `@overload` Support in JSDoc

In TypeScript, you can specify overloads for a function.
Overloads give us a way to say that a function can be called with different arguments, and possibly return different results.
They can restrict how callers can actually use our functions, and refine what results they’ll get back.

\`\`\`
// Our overloads:function printValue(str: string): void;function printValue(num: number, maxFractionDigits?: number): void;// Our implementation:function printValue(value: string \| number, maximumFractionDigits?: number) { if (typeof value === "number") { const formatter = Intl.NumberFormat("en\-US", { maximumFractionDigits, }); value = formatter.format(value); } console.log(value);}
\`\`\`
Here, we’ve said that `printValue` takes either a `string` or a `number` as its first argument.
If it takes a `number`, it can take a second argument to determine how many fractional digits we can print.

TypeScript 5\.0 now allows JSDoc to declare overloads with a new `@overload` tag.
Each JSDoc comment with an `@overload` tag is treated as a distinct overload for the following function declaration.

\`\`\`
// @ts\-check/\*\* \* @overload \* @param {string} value \* @return {void} \*//\*\* \* @overload \* @param {number} value \* @param {number} \[maximumFractionDigits] \* @return {void} \*//\*\* \* @param {string \| number} value \* @param {number} \[maximumFractionDigits] \*/function printValue(value, maximumFractionDigits) { if (typeof value === "number") { const formatter = Intl.NumberFormat("en\-US", { maximumFractionDigits, }); value = formatter.format(value); } console.log(value);}
\`\`\`
Now regardless of whether we’re writing in a TypeScript or JavaScript file, TypeScript can let us know if we’ve called our functions incorrectly.

\`\`\`
// all allowedprintValue("hello!");printValue(123\.45\);printValue(123\.45, 2\);printValue("hello!", 123\); // error!
\`\`\`
This new tag [was implemented](https://github.com/microsoft/TypeScript/pull/51234) thanks to [Tomasz Lenarcik](https://github.com/apendua).

## Passing Emit\-Specific Flags Under `--build`

TypeScript now allows the following flags to be passed under `--build` mode

* `--declaration`
* `--emitDeclarationOnly`
* `--declarationMap`
* `--sourceMap`
* `--inlineSourceMap`

This makes it way easier to customize certain parts of a build where you might have different development and production builds.

For example, a development build of a library might not need to produce declaration files, but a production build would.
A project can configure declaration emit to be off by default and simply be built with

\`\`\`
tsc \-\-build \-p ./my\-project\-dir
\`\`\`
Once you’re done iterating in the inner loop, a “production” build can just pass the `--declaration` flag.

\`\`\`
tsc \-\-build \-p ./my\-project\-dir \-\-declaration
\`\`\`
[More information on this change is available here](https://github.com/microsoft/TypeScript/pull/51241).

## Case\-Insensitive Import Sorting in Editors

In editors like Visual Studio and VS Code, TypeScript powers the experience for organizing and sorting imports and exports.
Often though, there can be different interpretations of when a list is “sorted”.

For example, is the following import list sorted?

\`\`\`
import { Toggle, freeze, toBoolean,} from "./utils";
\`\`\`
The answer might surprisingly be “it depends”.
If we *don’t* care about case\-sensitivity, then this list is clearly not sorted.
The letter `f` comes before both `t` and `T`.

But in most programming languages, sorting defaults to comparing the byte values of strings.
The way JavaScript compares strings means that `"Toggle"` always comes before `"freeze"` because according to the [ASCII character encoding](https://en.wikipedia.org/wiki/ASCII), uppercase letters come before lowercase.
So from that perspective, the import list is sorted.

TypeScript previously considered the import list to be sorted because it was doing a basic case\-sensitive sort.
This could be a point of frustration for developers who preferred a case\-*insensitive* ordering, or who used tools like ESLint which require case\-insensitive ordering by default.

TypeScript now detects case sensitivity by default.
This means that TypeScript and tools like ESLint typically won’t “fight” each other over how to best sort imports.

Our team has also been experimenting [with further sorting strategies which you can read about here](https://github.com/microsoft/TypeScript/pull/52115).
These options may eventually be configurable by editors.
For now, they are still unstable and experimental, and you can opt into them in VS Code today by using the `typescript.unstable` entry in your JSON options.
Below are all of the options you can try out (set to their defaults):

\`\`\`
{ "typescript.unstable": { // Should sorting be case\-sensitive? Can be: // \- true // \- false // \- "auto" (auto\-detect) "organizeImportsIgnoreCase": "auto", // Should sorting be "ordinal" and use code points or consider Unicode rules? Can be: // \- "ordinal" // \- "unicode" "organizeImportsCollation": "ordinal", // Under \`"organizeImportsCollation": "unicode"\`, // what is the current locale? Can be: // \- \[any other locale code] // \- "auto" (use the editor's locale) "organizeImportsLocale": "en", // Under \`"organizeImportsCollation": "unicode"\`, // should upper\-case letters or lower\-case letters come first? Can be: // \- false (locale\-specific) // \- "upper" // \- "lower" "organizeImportsCaseFirst": false, // Under \`"organizeImportsCollation": "unicode"\`, // do runs of numbers get compared numerically (i.e. "a1" \`, `=`:

\`\`\`
function func(ns: number \| string) { return ns \> 4; // Now also an error}
\`\`\`
To allow this if desired, you can explicitly coerce the operand to a `number` using `+`:

\`\`\`
function func(ns: number \| string) { return \+ns \> 4; // OK}
\`\`\`
This [correctness improvement](https://github.com/microsoft/TypeScript/pull/52048) was contributed courtesy of [Mateusz Burzyński](https://github.com/Andarist).

### Enum Overhaul

TypeScript has had some long\-standing oddities around `enum`s ever since its first release.
In 5\.0, we’re cleaning up some of these problems, as well as reducing the concept count needed to understand the various kinds of `enum`s you can declare.

There are two main new errors you might see as part of this.
The first is that assigning an out\-of\-domain literal to an `enum` type will now error as one might expect:

\`\`\`
enum SomeEvenDigit { Zero = 0, Two = 2, Four = 4}// Now correctly an errorlet m: SomeEvenDigit = 1;
\`\`\`
The other is that declaration of certain kinds of indirected mixed string/number `enum` forms would, incorrectly, create an all\-number `enum`:

\`\`\`
enum Letters { A = "a"}enum Numbers { one = 1, two = Letters.A}// Now correctly an errorconst t: number = Numbers.two;
\`\`\`
You can [see more details in relevant change](https://github.com/microsoft/TypeScript/pull/50528).

### More Accurate Type\-Checking for Parameter Decorators in Constructors Under `--experimentalDecorators`

TypeScript 5\.0 makes type\-checking more accurate for decorators under `--experimentalDecorators`.
One place where this becomes apparent is when using a decorator on a constructor parameter.

\`\`\`
export declare const inject: (entity: any) =\> (target: object, key: string \| symbol, index?: number) =\> void;export class Foo {}export class C { constructor(@inject(Foo) private x: any) { }}
\`\`\`
This call will fail because `key` expects a `string | symbol`, but constructor parameters receive a key of `undefined`.
The correct fix is to change the type of `key` within `inject`.
A reasonable workaround if you’re using a library that can’t be upgraded is is to wrap `inject` in a more type\-safe decorator function, and use a type\-assertion on `key`.

For more details, [see this issue](https://github.com/microsoft/TypeScript/issues/52435).

### Deprecations and Default Changes

In TypeScript 5\.0, we’ve deprecated the following settings and setting values:

* `--target: ES3`
* `--out`
* `--noImplicitUseStrict`
* `--keyofStringsOnly`
* `--suppressExcessPropertyErrors`
* `--suppressImplicitAnyIndexErrors`
* `--noStrictGenericChecks`
* `--charset`
* `--importsNotUsedAsValues`
* `--preserveValueImports`
* `prepend` in project references

These configurations will continue to be allowed until TypeScript 5\.5, at which point they will be removed entirely, however, you will receive a warning if you are using these settings.
In TypeScript 5\.0, as well as future releases 5\.1, 5\.2, 5\.3, and 5\.4, you can specify `"ignoreDeprecations": "5.0"` to silence those warnings.
We’ll also shortly be releasing a 4\.9 patch to allow specifying `ignoreDeprecations` to allow for smoother upgrades.
Aside from deprecations, we’ve changed some settings to better improve cross\-platform behavior in TypeScript.

`--newLine`, which controls the line endings emitted in JavaScript files, used to be inferred based on the current operating system if not specified.
We think builds should be as deterministic as possible, and Windows Notepad supports line\-feed line endings now, so the new default setting is `LF`.
The old OS\-specific inference behavior is no longer available.

`--forceConsistentCasingInFileNames`, which ensured that all references to the same file name in a project agreed in casing, now defaults to `true`.
This can help catch differences issues with code written on case\-insensitive file systems.

You can leave feedback and view more information on the [tracking issue for 5\.0 deprecations](https://github.com/microsoft/TypeScript/issues/51909)

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 5.0.md) ❤

Contributors to this page:  
ABEIMMKM1\+Last updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 4.8

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-8.html)

Was this page helpful?

# TypeScript 4\.8

## Improved Intersection Reduction, Union Compatibility, and Narrowing

TypeScript 4\.8 brings a series of correctness and consistency improvements under `--strictNullChecks`.
These changes affect how intersection and union types work, and are leveraged in how TypeScript narrows types.

For example, `unknown` is close in spirit to the union type `{} | null | undefined` because it accepts `null`, `undefined`, and any other type.
TypeScript now recognizes this, and allows assignments from `unknown` to `{} | null | undefined`.

\`\`\`
function f(x: unknown, y: {} \| null \| undefined) { x = y; // always worked y = x; // used to error, now works}
\`\`\`
Another change is that `{}` intersected with any other object type simplifies right down to that object type.
That meant that we were able to rewrite `NonNullable` to just use an intersection with `{}`, because `{} & null` and `{} & undefined` just get tossed away.

\`\`\`
\- type NonNullable\ = T extends null \| undefined ? never : T;\+ type NonNullable\ = T \& {};
\`\`\`
This is an improvement because intersection types like this can be reduced and assigned to, while conditional types currently cannot.
So `NonNullable>` now simplifies at least to `NonNullable`, whereas it didn’t before.

\`\`\`
function foo\(x: NonNullable\, y: NonNullable\\>) { x = y; // always worked y = x; // used to error, now works}
\`\`\`
These changes also allowed us to bring in sensible improvements in control flow analysis and type narrowing.
For example, `unknown` is now narrowed just like `{} | null | undefined` in truthy branches.

\`\`\`
function narrowUnknownishUnion(x: {} \| null \| undefined) { if (x) { x; // {} } else { x; // {} \| null \| undefined }}function narrowUnknown(x: unknown) { if (x) { x; // used to be 'unknown', now '{}' } else { x; // unknown }}
\`\`\`
Generic values also get narrowed similarly.
When checking that a value isn’t `null` or `undefined`, TypeScript now just intersects it with `{}` \- which again, is the same as saying it’s `NonNullable`.
Putting many of the changes here together, we can now define the following function without any type assertions.

\`\`\`
function throwIfNullable\(value: T): NonNullable\ { if (value === undefined \|\| value === null) { throw Error("Nullable value!"); } // Used to fail because 'T' was not assignable to 'NonNullable\'. // Now narrows to 'T \& {}' and succeeds because that's just 'NonNullable\'. return value;}
\`\`\`
`value` now gets narrowed to `T & {}`, and is now identical with `NonNullable` \- so the body of the function just works with no TypeScript\-specific syntax.

On their own, these changes may appear small \- but they represent fixes for many many paper cuts that have been reported over several years.

For more specifics on these improvements, you can [read more here](https://github.com/microsoft/TypeScript/pull/49119).

## Improved Inference for `infer` Types in Template String Types

TypeScript recently introduced a way to add `extends` constraints to `infer` type variables in conditional types.

\`\`\`
// Grabs the first element of a tuple if it's assignable to 'number',// and returns 'never' if it can't find one.type TryGetNumberIfFirst\ = T extends \[infer U extends number, ...unknown\[]] ? U : never;
\`\`\`
If these `infer` types appear in a template string type and are constrained to a primitive type, TypeScript will now try to parse out a literal type.

\`\`\`
// SomeNum used to be 'number'; now it's '100'.type SomeNum = "100" extends \`${infer U extends number}\` ? U : never;// SomeBigInt used to be 'bigint'; now it's '100n'.type SomeBigInt = "100" extends \`${infer U extends bigint}\` ? U : never;// SomeBool used to be 'boolean'; now it's 'true'.type SomeBool = "true" extends \`${infer U extends boolean}\` ? U : never;
\`\`\`
This can now better convey what a library will do at runtime, and give more precise types.

One note on this is that when TypeScript parses these literal types out it will greedily try to parse out as much of what looks like of the appropriate primitive type;
however it then checks to see if the print\-back of that primitive matches up with the string contents.
In other words, TypeScript checks whether the going from the string, to the primitive, and back matches.
If it doesn’t see that the string can be “round\-tripped”, then it will fall back to the base primitive type.

\`\`\`
// JustNumber is \`number\` here because TypeScript parses out \`"1\.0"\`, but \`String(Number("1\.0"))\` is \`"1"\` and doesn't match.type JustNumber = "1\.0" extends \`${infer T extends number}\` ? T : never; 
\`\`\`
You can [see more about this feature here](https://github.com/microsoft/TypeScript/pull/48094).

## `--build`, `--watch`, and `--incremental` Performance Improvements

TypeScript 4\.8 introduces several optimizations that should speed up scenarios around `--watch` and `--incremental`, along with project references builds using `--build`.
For example, TypeScript is now able to avoid spending time updating timestamps during no\-op changes in `--watch` mode, which makes rebuilds faster and avoids messing with other build tools that might be watching for TypeScript’s output.
Many other optimizations where we’re able to reuse information across `--build`, `--watch`, and `--incremental` have been introduced as well.

How big are these improvements?
Well, on a fairly large internal codebase, we’ve seen time reductions on the order of 10%\-25% on many simple common operations, with around 40% time reductions in no\-change scenarios.
We’ve seen similar results on the TypeScript codebase as well.

You can see [the changes, along with the performance results on GitHub](https://github.com/microsoft/TypeScript/pull/48784).

## Errors When Comparing Object and Array Literals

In many languages, operators like `==` perform what’s called “value” equality on objects.
For example, in Python it’s valid to check whether a list is empty by checking whether a value is equal to the empty list using `==`.

\`\`\`
if people\_at\_home == \[]: print("here's where I lie, broken inside. \(x: T, y: T): T;let \[a, b, c] = chooseRandomly(\[42, true, "hi!"], \[0, false, "bye!"]);// ^ ^ ^// \| \| \|// \| \| string// \| \|// \| boolean// \|// number
\`\`\`
When `chooseRandomly` needs to figure out a type for `T`, it will primarily look at `[42, true, "hi!"]` and `[0, false, "bye!"]`;
but TypeScript needs to figure out whether those two types should be `Array` or the tuple type `[number, boolean, string]`.
To do that, it will look for existing candidates as a hint to see whether there are any tuple types.
When TypeScript sees the binding pattern `[a, b, c]`, it creates the type `[any, any, any]`, and that type gets picked up as a low\-priority candidate for `T` which also gets used as a hint for the types of `[42, true, "hi!"]` and `[0, false, "bye!"]`.

You can see how this was good for `chooseRandomly`, but it fell short in other cases.
For example, take the following code

\`\`\`
declare function f\(x?: T): T;let \[x, y, z] = f();
\`\`\`
The binding pattern `[x, y, z]` hinted that `f` should produce an `[any, any, any]` tuple;
but `f` really shouldn’t change its type argument based on a binding pattern.
It can’t suddenly conjure up a new array\-like value based on what it’s being assigned to, so the binding pattern type has way too much influence on the produced type.
On top of that, because the binding pattern type is full of `any`s, we’re left with `x`, `y`, and `z` being typed as `any`.

In TypeScript 4\.8, these binding patterns are never used as candidates for type arguments.
Instead, they’re just consulted in case a parameter needs a more specific type like in our `chooseRandomly` example.
If you need to revert to the old behavior, you can always provide explicit type arguments.

You can [look at the change on GitHub](https://github.com/microsoft/TypeScript/pull/49086) if you’re curious to learn more.

## File\-Watching Fixes (Especially Across `git checkout`s)

We’ve had a long\-standing bug where TypeScript has a very hard time with certain file changes in `--watch` mode and editor scenarios.
Sometimes the symptoms are stale or inaccurate errors that might show up that require restarting `tsc` or VS Code.
Frequently these occur on Unix systems, and you might have seen these after saving a file with vim or swapping branches in git.

This was caused by assumptions of how Node.js handles rename events across file systems.
File systems used by Linux and macOS utilize [inodes](https://en.wikipedia.org/wiki/Inode), and [Node.js will attach file watchers to inodes rather than file paths](https://nodejs.org/api/fs.html#inodes).
So when Node.js returns [a watcher object](https://nodejs.org/api/fs.html#class-fsfswatcher), it might be watching a path or an inode depending on the platform and file system.

To be a bit more efficient, TypeScript tries to reuse the same watcher objects if it detects a path still exists on disk.
This is where things went wrong, because even if a file still exists at that path, a distinct file might have been created, and that file will have a different inode.
So TypeScript would end up reusing the watcher object instead of installing a new watcher at the original location, and watch for changes at what might be a totally irrelevant file.
So TypeScript 4\.8 now handles these cases on inode systems and properly installs a new watcher and fixes this.

We’d like to extend our thanks to [Marc Celani](https://github.com/MarcCelani-at) and his team at Airtable who invested lots of time in investigating the issues they were experiencing and pointing out the root cause.
You can view [the specific fixes around file\-watching here](https://github.com/microsoft/TypeScript/pull/48997).

## Find\-All\-References Performance Improvements

When running find\-all\-references in your editor, TypeScript is now able to act a little smarter as it aggregates references.
This reduced the amount of time TypeScript took to search a widely\-used identifier in its own codebase by about 20%.

[You can read up more on the improvement here](https://github.com/microsoft/TypeScript/pull/49581).

## Exclude Specific Files from Auto\-Imports

TypeScript 4\.8 introduces an editor preference for excluding files from auto\-imports.
In Visual Studio Code, file names or globs can be added under “Auto Import File Exclude Patterns” in the Settings UI, or in a `.vscode/settings.json` file:

\`\`\`
{ // Note that \`javascript.preferences.autoImportFileExcludePatterns\` can be specified for JavaScript too. "typescript.preferences.autoImportFileExcludePatterns": \[ "\*\*/node\_modules/@types/node" ]}
\`\`\`
This can be useful in cases where you can’t avoid having certain modules or libraries in your compilation but you rarely want to import from them.
These modules might have lots of exports that can pollute the auto\-imports list and make it harder to navigate, and this option can help in those situations.

You can [see more specifics about the implementation here](https://github.com/microsoft/TypeScript/pull/49578).

## Correctness Fixes and Breaking Changes

Due to the nature of type system changes, there are very few changes that can be made that don’t affect *some* code;
however, there are a few changes that are more likely to require adapting existing code.

### `lib.d.ts` Updates

While TypeScript strives to avoid major breaks, even small changes in the built\-in libraries can cause issues.
We don’t expect major breaks as a result of DOM and `lib.d.ts` updates, but one notable change is that the `cause` property on `Error`s now has the type `unknown` instead of `Error`.

### Unconstrained Generics No Longer Assignable to `{}`

In TypeScript 4\.8, for projects with `strictNullChecks` enabled, TypeScript will now correctly issue an error when an unconstrained type parameter is used in a position where `null` or `undefined` are not legal values.
That will include any type that expects `{}`, `object`, or an object type with all\-optional properties.

A simple example can be seen in the following.

\`\`\`
// Accepts any non\-null non\-undefined valuefunction bar(value: {}) { Object.keys(value); // This call throws on null/undefined at runtime.}// Unconstrained type parameter T...function foo\(x: T) { bar(x); // Used to be allowed, now is an error in 4\.8\. // \~ // error: Argument of type 'T' is not assignable to parameter of type '{}'.}foo(undefined);
\`\`\`
As demonstrated above, code like this has a potential bug \- the values `null` and `undefined` can be indirectly passed through these unconstrained type parameters to code that is not supposed to observe those values.

This behavior will also be visible in type positions. One example would be:

\`\`\`
interface Foo\ { x: Bar\;}interface Bar\ { }
\`\`\`
Existing code that didn’t want to handle `null` and `undefined` can be fixed by propagating the appropriate constraints through.

\`\`\`
\- function foo\(x: T) {\+ function foo\(x: T) {
\`\`\`
Another work\-around would be to check for `null` and `undefined` at runtime.

\`\`\`
 function foo\(x: T) {\+ if (x !== null \&\& x !== undefined) { bar(x);\+ } }
\`\`\`
And if you know that for some reason, your generic value can’t be `null` or `undefined`, you can just use a non\-null assertion.

\`\`\`
 function foo\(x: T) {\- bar(x);\+ bar(x!); }
\`\`\`
When it comes to types, you’ll often either need to propagate constraints, or intersect your types with `{}`.

For more information, you can [see the change that introduced this](https://github.com/microsoft/TypeScript/pull/49119) along with [the specific discussion issue regarding how unconstrained generics now work](https://github.com/microsoft/TypeScript/issues/49489).

### Decorators are placed on `modifiers` on TypeScript’s Syntax Trees

The current direction of decorators in TC39 means that TypeScript will have to handle a break in terms of placement of decorators.
Previously, TypeScript assumed decorators would always be placed prior to all keywords/modifiers.
For example

\`\`\`
@decoratorexport class Foo { // ...}
\`\`\`
Decorators as currently proposed do not support this syntax.
Instead, the `export` keyword must precede the decorator.

\`\`\`
export @decorator class Foo { // ...}
\`\`\`
Unfortunately, TypeScript’s trees are *concrete* rather than *abstract*, and our architecture expects syntax tree node fields to be entirely ordered before or after each other.
To support both legacy decorators and decorators as proposed, TypeScript will have to gracefully parse, and intersperse, modifiers and decorators.

To do this, it exposes a new type alias called `ModifierLike` which is a `Modifier` or a `Decorator`.

\`\`\`
export type ModifierLike = Modifier \| Decorator;
\`\`\`
Decorators are now placed in the same field as `modifiers` which is now a `NodeArray` when set, and the entire field is deprecated.

\`\`\`
\- readonly modifiers?: NodeArray\ \| undefined;\+ /\*\*\+ \* @deprecated ...\+ \* Use \`ts.canHaveModifiers()\` to test whether a \`Node\` can have modifiers.\+ \* Use \`ts.getModifiers()\` to get the modifiers of a \`Node\`.\+ \* ...\+ \*/\+ readonly modifiers?: NodeArray\ \| undefined;
\`\`\`
All existing `decorators` properties have been marked as deprecated and will always be `undefined` if read.
The type has also been changed to `undefined` so that existing tools know to handle them correctly.

\`\`\`
\- readonly decorators?: NodeArray\ \| undefined;\+ /\*\*\+ \* @deprecated ...\+ \* Use \`ts.canHaveDecorators()\` to test whether a \`Node\` can have decorators.\+ \* Use \`ts.getDecorators()\` to get the decorators of a \`Node\`.\+ \* ...\+ \*/\+ readonly decorators?: undefined;
\`\`\`
To avoid new deprecation warnings and other issues, TypeScript now exposes four new functions to use in place of the `decorators` and `modifiers` properties.
There are individual predicates for testing whether a node has support modifiers and decorators, along with respective accessor functions for grabbing them.

\`\`\`
function canHaveModifiers(node: Node): node is HasModifiers;function getModifiers(node: HasModifiers): readonly Modifier\[] \| undefined;function canHaveDecorators(node: Node): node is HasDecorators;function getDecorators(node: HasDecorators): readonly Decorator\[] \| undefined;
\`\`\`
As an example of how to access modifiers off of a node, you can write

\`\`\`
const modifiers = canHaveModifiers(myNode) ? getModifiers(myNode) : undefined;
\`\`\`
With the note that each call to `getModifiers` and `getDecorators` may allocate a new array.

For more information, see changes around

* [the restructuring of our tree nodes](https://github.com/microsoft/TypeScript/pull/49089)
* [the deprecations](https://github.com/microsoft/TypeScript/pull/50343)
* [exposing the predicate functions](https://github.com/microsoft/TypeScript/pull/50399)

### Types Cannot Be Imported/Exported in JavaScript Files

TypeScript previously allowed JavaScript files to import and export entities declared with a type, but no value, in `import` and `export` statements.
This behavior was incorrect, because named imports and exports for values that don’t exist will cause a runtime error under ECMAScript modules.
When a JavaScript file is type\-checked under `--checkJs` or through a `// @ts-check` comment, TypeScript will now issue an error.

\`\`\`
// @ts\-check// Will fail at runtime because 'SomeType' is not a value.import { someValue, SomeType } from "some\-module";/\*\* \* @type {SomeType} \*/export const myValue = someValue;/\*\* \* @typedef {string \| number} MyType \*/// Will fail at runtime because 'MyType' is not a value.export { MyType as MyExportedType };
\`\`\`
To reference a type from another module, you can instead directly qualify the import.

\`\`\`
\- import { someValue, SomeType } from "some\-module";\+ import { someValue } from "some\-module"; /\*\*\- \* @type {SomeType}\+ \* @type {import("some\-module").SomeType} \*/ export const myValue = someValue;
\`\`\`
To export a type, you can just use a `/** @typedef */` comment in JSDoc.
`@typedef` comments already automatically export types from their containing modules.

\`\`\`
 /\*\* \* @typedef {string \| number} MyType \*/\+ /\*\*\+ \* @typedef {MyType} MyExportedType\+ \*/\- export { MyType as MyExportedType };
\`\`\`
You can [read more about the change here](https://github.com/microsoft/TypeScript/pull/49580).

### Binding Patterns Do Not Directly Contribute to Inference Candidates

As mentioned above, binding patterns no longer change the type of inference results in function calls.
You can [read more about the original change here](https://github.com/microsoft/TypeScript/pull/49086).

### Unused Renames in Binding Patterns are Now Errors in Type Signatures

TypeScript’s type annotation syntax often looks like it can be used when destructuring values.
For example, take the following function.

\`\`\`
declare function makePerson({ name: string, age: number }): Person;
\`\`\`
You might read this signature and think that `makePerson` obviously takes an object with a `name` property with the type `string` and an `age` property with the type `number`;
however, JavaScript’s destructuring syntax is actually taking precedence here.
`makePerson` does say that it’s going to take an object with a `name` and an `age` property, but instead of specifying a type for them, it’s just saying that it renames `name` and `age` to `string` and `number` respectively.

In a pure type construct, writing code like this is useless, and typically a mistake since developers usually assume they’re writing a type annotation.

TypeScript 4\.8 makes these an error unless they’re referenced later in the signature.
The correct way to write the above signature would be as follows:

\`\`\`
declare function makePerson(options: { name: string, age: number }): Person;// ordeclare function makePerson({ name, age }: { name: string, age: number }): Person;
\`\`\`
This change can catch bugs in declarations, and has been helpful for improving existing code.
We’d like to extend our thanks to [GitHub user uhyo](https://github.com/uhyo) for providing this check.
[You can read up on the change here](https://github.com/microsoft/TypeScript/pull/41044).

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 4.8.md) ❤

Contributors to this page:  
ABLast updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 5.1

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-1.html)

Was this page helpful?

# TypeScript 5\.1

## Easier Implicit Returns for `undefined`\-Returning Functions

In JavaScript, if a function finishes running without hitting a `return`, it returns the value `undefined`.

\`\`\`
function foo() { // no return}// x = undefinedlet x = foo();
\`\`\`
However, in previous versions of TypeScript, the *only* functions that could have absolutely no return statements were `void`\- and `any`\-returning functions.
That meant that even if you explicitly said “this function returns `undefined`” you were forced to have at least one return statement.

\`\`\`
// ✅ fine \- we inferred that 'f1' returns 'void'function f1() { // no returns}// ✅ fine \- 'void' doesn't need a return statementfunction f2(): void { // no returns}// ✅ fine \- 'any' doesn't need a return statementfunction f3(): any { // no returns}// ❌ error!// A function whose declared type is neither 'void' nor 'any' must return a value.function f4(): undefined { // no returns}
\`\`\`
This could be a pain if some API expected a function returning `undefined` \- you would need to have either at least one explicit return of `undefined` or a `return` statement *and* an explicit annotation.

\`\`\`
declare function takesFunction(f: () =\> undefined): undefined;// ❌ error!// Argument of type '() =\> void' is not assignable to parameter of type '() =\> undefined'.takesFunction(() =\> { // no returns});// ❌ error!// A function whose declared type is neither 'void' nor 'any' must return a value.takesFunction((): undefined =\> { // no returns});// ❌ error!// Argument of type '() =\> void' is not assignable to parameter of type '() =\> undefined'.takesFunction(() =\> { return;});// ✅ workstakesFunction(() =\> { return undefined;});// ✅ workstakesFunction((): undefined =\> { return;});
\`\`\`
This behavior was frustrating and confusing, especially when calling functions outside of one’s control.
Understanding the interplay between inferring `void` over `undefined`, whether an `undefined`\-returning function needs a `return` statement, etc. seems like a distraction.

First, TypeScript 5\.1 now allows `undefined`\-returning functions to have no return statement.

\`\`\`
// ✅ Works in TypeScript 5\.1!function f4(): undefined { // no returns}// ✅ Works in TypeScript 5\.1!takesFunction((): undefined =\> { // no returns});
\`\`\`
Second, if a function has no return expressions and is being passed to something expecting a function that returns `undefined`, TypeScript infers `undefined` for that function’s return type.

\`\`\`
// ✅ Works in TypeScript 5\.1!takesFunction(function f() { // ^ return type is undefined // no returns});// ✅ Works in TypeScript 5\.1!takesFunction(function f() { // ^ return type is undefined return;});
\`\`\`
To address another similar pain\-point, under TypeScript’s `--noImplicitReturns` option, functions returning *only* `undefined` now have a similar exception to `void`, in that not every single code path must end in an explicit `return`.

\`\`\`
// ✅ Works in TypeScript 5\.1 under '\-\-noImplicitReturns'!function f(): undefined { if (Math.random()) { // do some stuff... return; }}
\`\`\`
For more information, you can read up on [the original issue](https://github.com/microsoft/TypeScript/issues/36288) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/53607).

## Unrelated Types for Getters and Setters

TypeScript 4\.3 made it possible to say that a `get` and `set` accessor pair might specify two different types.

\`\`\`
interface Serializer { set value(v: string \| number \| boolean); get value(): string;}declare let box: Serializer;// Allows writing a 'boolean'box.value = true;// Comes out as a 'string'console.log(box.value.toUpperCase());
\`\`\`
Initially we required that the `get` type had to be a subtype of the `set` type.
This meant that writing

\`\`\`
box.value = box.value;
\`\`\`
would always be valid.

However, there are plenty of existing and proposed APIs that have completely unrelated types between their getters and setters.
For example, consider one of the most common examples \- the `style` property in the DOM and [`CSSStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule) API.
Every style rule has [a `style` property](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule/style) that is a [`CSSStyleDeclaration`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration);
however, if you try to write to that property, it will only work correctly with a string!

TypeScript 5\.1 now allows completely unrelated types for `get` and `set` accessor properties, provided that they have explicit type annotations.
And while this version of TypeScript does not yet change the types for these built\-in interfaces, `CSSStyleRule` can now be defined in the following way:

\`\`\`
interface CSSStyleRule { // ... /\*\* Always reads as a \`CSSStyleDeclaration\` \*/ get style(): CSSStyleDeclaration; /\*\* Can only write a \`string\` here. \*/ set style(newValue: string); // ...}
\`\`\`
This also allows other patterns like requiring `set` accessors to accept only “valid” data, but specifying that `get` accessors may return `undefined` if some underlying state hasn’t been initialized yet.

\`\`\`
class SafeBox { \#value: string \| undefined; // Only accepts strings! set value(newValue: string) { } // Must check for 'undefined'! get value(): string \| undefined { return this.\#value; }}
\`\`\`
In fact, this is similar to how optional properties are checked under `--exactOptionalProperties`.

You can read up more on [the implementing pull request](https://github.com/microsoft/TypeScript/pull/53417).

## Decoupled Type\-Checking Between JSX Elements and JSX Tag Types

One pain point TypeScript had with JSX was its requirements on the type of every JSX element’s tag.

For context, a JSX element is either of the following:

\`\`\`
// A self\-closing JSX tag\// A regular element with an opening/closing tag\\
\`\`\`
When type\-checking `` or ``, TypeScript always looks up a namespace called `JSX` and fetches a type out of it called `Element` \- or more directly, it looks up `JSX.Element`.

But to check whether `Foo` or `Bar` themselves were valid to use as tag names, TypeScript would roughly just grab the types returned or constructed by `Foo` or `Bar` and check for compatibility with `JSX.Element` (or another type called `JSX.ElementClass` if the type is constructable).

The limitations here meant that components could not be used if they returned or “rendered” a more broad type than just `JSX.Element`.
For example, a JSX library might be fine with a component returning `string`s or `Promise`s.

As a more concrete example, [React is considering adding limited support for components that return `Promise`s](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md), but existing versions of TypeScript cannot express that without someone drastically loosening the type of `JSX.Element`.

\`\`\`
import \* as React from "react";async function Foo() { return \\;}let element = \;// \~\~\~// 'Foo' cannot be used as a JSX component.// Its return type 'Promise\' is not a valid JSX element.
\`\`\`
To provide libraries with a way to express this, TypeScript 5\.1 now looks up a type called `JSX.ElementType`.
`ElementType` specifies precisely what is valid to use as a tag in a JSX element.
So it might be typed today as something like

\`\`\`
namespace JSX { export type ElementType = // All the valid lowercase tags keyof IntrinsicAttributes // Function components (props: any) =\> Element // Class components new (props: any) =\> ElementClass; export interface IntrinsicAttributes extends /\*...\*/ {} export type Element = /\*...\*/; export type ElementClass = /\*...\*/;}
\`\`\`
We’d like to extend our thanks to [Sebastian Silbermann](https://github.com/eps1lon) who contributed [this change](https://github.com/microsoft/TypeScript/pull/51328)!

## Namespaced JSX Attributes

TypeScript now supports namespaced attribute names when using JSX.

\`\`\`
import \* as React from "react";// Both of these are equivalent:const x = \;const y = \;interface FooProps { "a:b": string;}function Foo(props: FooProps) { return \{props\["a:b"]}\;}
\`\`\`
Namespaced tag names are looked up in a similar way on `JSX.IntrinsicAttributes` when the first segment of the name is a lowercase name.

\`\`\`
// In some library's code or in an augmentation of that library:namespace JSX { interface IntrinsicElements { \["a:b"]: { prop: string }; }}// In our code:let x = \;
\`\`\`
[This contribution](https://github.com/microsoft/TypeScript/pull/53799) was provided thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk).

## `typeRoots` Are Consulted In Module Resolution

When TypeScript’s specified module lookup strategy is unable to resolve a path, it will now resolve packages relative to the specified `typeRoots`.

See [this pull request](https://github.com/microsoft/TypeScript/pull/51715) for more details.

## Move Declarations to Existing Files

In addition to moving declarations to new files, TypeScript now ships a preview feature for moving declarations to existing files as well.
You can try this functionality out in a recent version of Visual Studio Code.



Keep in mind that this feature is currently in preview, and we are seeking further feedback on it.



## Linked Cursors for JSX Tags

TypeScript now supports *linked editing* for JSX tag names.
Linked editing (occasionally called “mirrored cursors”) allows an editor to edit multiple locations at the same time automatically.



This new feature should work in both TypeScript and JavaScript files, and can be enabled in Visual Studio Code Insiders.
In Visual Studio Code, you can either edit the `Editor: Linked Editing` option in the Settings UI:



or configure `editor.linkedEditing` in your JSON settings file:

\`\`\`
{ // ... "editor.linkedEditing": true,}
\`\`\`
This feature will also be supported by Visual Studio 17\.7 Preview 1\.

You can take a look at [our implementation of linked editing](https://github.com/microsoft/TypeScript/pull/53284) here!

## Snippet Completions for `@param` JSDoc Tags

TypeScript now provides snippet completions when typing out a `@param` tag in both TypeScript and JavaScript files.
This can help cut down on some typing and jumping around text as you document your code or add JSDoc types in JavaScript.



You can [check out how this new feature was implemented on GitHub](https://github.com/microsoft/TypeScript/pull/53260).

## Optimizations

### Avoiding Unnecessary Type Instantiation

TypeScript 5\.1 now avoids performing type instantiation within object types that are known not to contain references to outer type parameters.
This has the potential to cut down on many unnecessary computations, and reduced the type\-checking time of [material\-ui’s docs directory](https://github.com/mui/material-ui/tree/b0351248fb396001a30330daac86d0e0794a0c1d/docs) by over 50%.

You can [see the changes involved for this change on GitHub](https://github.com/microsoft/TypeScript/pull/53246).

### Negative Case Checks for Union Literals

When checking if a source type is part of a union type, TypeScript will first do a fast look\-up using an internal type identifier for that source.
If that look\-up fails, then TypeScript checks for compatibility against every type within the union.

When relating a literal type to a union of purely literal types, TypeScript can now avoid that full walk against every other type in the union.
This assumption is safe because TypeScript always interns/caches literal types \- though there are some edge cases to handle relating to “fresh” literal types.

[This optimization](https://github.com/microsoft/TypeScript/pull/53192) was able to reduce the type\-checking time of [the code in this issue](https://github.com/microsoft/TypeScript/issues/53191) from about 45 seconds to about 0\.4 seconds.

### Reduced Calls into Scanner for JSDoc Parsing

When older versions of TypeScript parsed out a JSDoc comment, they would use the scanner/tokenizer to break the comment into fine\-grained tokens and piece the contents back together.
This could be helpful for normalizing comment text, so that multiple spaces would just collapse into one;
but it was extremely “chatty” and meant the parser and scanner would jump back and forth very often, adding overhead to JSDoc parsing.

TypeScript 5\.1 has moved more logic around breaking down JSDoc comments into the scanner/tokenizer.
The scanner now returns larger chunks of content directly to the parser to do as it needs.

[These changes](https://github.com/microsoft/TypeScript/pull/53081) have brought down the parse time of several 10Mb mostly\-prose\-comment JavaScript files by about half.
For a more realistic example, our performance suite’s snapshot of [xstate](https://github.com/statelyai/xstate) dropped about 300ms of parse time, making it faster to load and analyze.

## Breaking Changes

### ES2020 and Node.js 14\.17 as Minimum Runtime Requirements

TypeScript 5\.1 now ships JavaScript functionality that was introduced in ECMAScript 2020\.
As a result, at minimum TypeScript must be run in a reasonably modern runtime.
For most users, this means TypeScript now only runs on Node.js 14\.17 and later.

If you try running TypeScript 5\.1 under an older version of Node.js such as Node 10 or 12, you may see an error like the following from running either `tsc.js` or `tsserver.js`:

\`\`\`
node\_modules/typescript/lib/tsserver.js:2406 for (let i = startIndex ?? 0; i \=14\.17' },npm WARN EBADENGINE current: { node: 'v12\.22\.12', npm: '8\.19\.2' }npm WARN EBADENGINE }
\`\`\`
from Yarn:

\`\`\`
error typescript@5\.1\.1\-rc: The engine "node" is incompatible with this module. Expected version "\>=14\.17". Got "12\.22\.12"error Found incompatible module.
\`\`\`

[See more information around this change here](https://github.com/microsoft/TypeScript/pull/53291).

### Explicit `typeRoots` Disables Upward Walks for `node_modules/@types`

Previously, when the `typeRoots` option was specified in a `tsconfig.json` but resolution to any `typeRoots` directories had failed, TypeScript would still continue walking up parent directories, trying to resolve packages within each parent’s `node_modules/@types` folder.

This behavior could prompt excessive look\-ups and has been disabled in TypeScript 5\.1\.
As a result, you may begin to see errors like the following based on entries in your `tsconfig.json`’s `types` option or `/// ` directives

\`\`\`
error TS2688: Cannot find type definition file for 'node'.error TS2688: Cannot find type definition file for 'mocha'.error TS2688: Cannot find type definition file for 'jasmine'.error TS2688: Cannot find type definition file for 'chai\-http'.error TS2688: Cannot find type definition file for 'webpack\-env"'.
\`\`\`
The solution is typically to add specific entries for `node_modules/@types` to your `typeRoots`:

\`\`\`
{ "compilerOptions": { "types": \[ "node", "mocha" ], "typeRoots": \[ // Keep whatever you had around before. "./some\-custom\-types/", // You might need your local 'node\_modules/@types'. "./node\_modules/@types", // You might also need to specify a shared 'node\_modules/@types' // if you're using a "monorepo" layout. "../../node\_modules/@types", ] }}
\`\`\`
More information is available [on the original change on our issue tracker](https://github.com/microsoft/TypeScript/pull/51715).

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 5.1.md) ❤

Contributors to this page:  
NBTLLLast updated: Jan 02, 2025  



## TypeScript: Documentation - TypeScript 5.5

[Read the full article](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html)

Was this page helpful?

# TypeScript 5\.5

## Inferred Type Predicates

*This section was written by [Dan Vanderkam](https://github.com/danvk), who [implemented this feature in TypeScript 5\.5](https://github.com/microsoft/TypeScript/pull/57465). Thanks Dan!*

TypeScript’s control flow analysis does a great job of tracking how the type of a variable changes as it moves through your code:

\`\`\`
interface Bird { commonName: string; scientificName: string; sing(): void;}// Maps country names \-\> national bird.// Not all nations have official birds (looking at you, Canada!)declare const nationalBirds: Map\;function makeNationalBirdCall(country: string) { const bird = nationalBirds.get(country); // bird has a declared type of Bird \| undefined if (bird) { bird.sing(); // bird has type Bird inside the if statement } else { // bird has type undefined here. }}
\`\`\`
By making you handle the `undefined` case, TypeScript pushes you to write more robust code.

In the past, this sort of type refinement was more difficult to apply to arrays. This would have been an error in all previous versions of TypeScript:

\`\`\`
function makeBirdCalls(countries: string\[]) { // birds: (Bird \| undefined)\[] const birds = countries .map(country =\> nationalBirds.get(country)) .filter(bird =\> bird !== undefined); for (const bird of birds) { bird.sing(); // error: 'bird' is possibly 'undefined'. }}
\`\`\`
This code is perfectly fine: we’ve filtered all the `undefined` values out of the list.
But TypeScript hasn’t been able to follow along.

With TypeScript 5\.5, the type checker is fine with this code:

\`\`\`
function makeBirdCalls(countries: string\[]) { // birds: Bird\[] const birds = countries .map(country =\> nationalBirds.get(country)) .filter(bird =\> bird !== undefined); for (const bird of birds) { bird.sing(); // ok! }}
\`\`\`
Note the more precise type for `birds`.

This works because TypeScript now infers a [type predicate](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates) for the `filter` function.
You can see what’s going on more clearly by pulling it out into a standalone function:

\`\`\`
// function isBirdReal(bird: Bird \| undefined): bird is Birdfunction isBirdReal(bird: Bird \| undefined) { return bird !== undefined;}
\`\`\`
`bird is Bird` is the type predicate.
It means that, if the function returns `true`, then it’s a `Bird` (if the function returns `false` then it’s `undefined`).
The type declarations for `Array.prototype.filter` know about type predicates, so the net result is that you get a more precise type and the code passes the type checker.

TypeScript will infer that a function returns a type predicate if these conditions hold:

1. The function does not have an explicit return type or type predicate annotation.
2. The function has a single `return` statement and no implicit returns.
3. The function does not mutate its parameter.
4. The function returns a `boolean` expression that’s tied to a refinement on the parameter.

Generally this works how you’d expect.
Here’s a few more examples of inferred type predicates:

\`\`\`
// const isNumber: (x: unknown) =\> x is numberconst isNumber = (x: unknown) =\> typeof x === 'number';// const isNonNullish: \(x: T) =\> x is NonNullable\const isNonNullish = \(x: T) =\> x != null;
\`\`\`
Previously, TypeScript would have just inferred that these functions return `boolean`.
It now infers signatures with type predicates like `x is number` or `x is NonNullable`.

Type predicates have “if and only if” semantics.
If a function returns `x is T`, then it means that:

1. If the function returns `true` then `x` has the type `T`.
2. If the function returns `false` then `x` does *not* have type `T`.

If you’re expecting a type predicate to be inferred but it’s not, then you may be running afoul of the second rule. This often comes up with “truthiness” checks:

\`\`\`
function getClassroomAverage(students: string\[], allScores: Map\) { const studentScores = students .map(student =\> allScores.get(student)) .filter(score =\> !!score); return studentScores.reduce((a, b) =\> a \+ b) / studentScores.length; // \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~ // error: Object is possibly 'undefined'.}
\`\`\`
TypeScript did not infer a type predicate for `score => !!score`, and rightly so: if this returns `true` then `score` is a `number`.
But if it returns `false`, then `score` could be either `undefined` or a `number` (specifically, `0`).
This is a real bug: if any student got a zero on the test, then filtering out their score will skew the average upwards.
Fewer will be above average and more will be sad!

As with the first example, it’s better to explicitly filter out `undefined` values:

\`\`\`
function getClassroomAverage(students: string\[], allScores: Map\) { const studentScores = students .map(student =\> allScores.get(student)) .filter(score =\> score !== undefined); return studentScores.reduce((a, b) =\> a \+ b) / studentScores.length; // ok!}
\`\`\`
A truthiness check *will* infer a type predicate for object types, where there’s no ambiguity.
Remember that functions must return a `boolean` to be a candidate for an inferred type predicate: `x => !!x` might infer a type predicate, but `x => x` definitely won’t.

Explicit type predicates continue to work exactly as before.
TypeScript will not check whether it would infer the same type predicate.
Explicit type predicates (“is”) are no safer than a type assertion (“as”).

It’s possible that this feature will break existing code if TypeScript now infers a more precise type than you want. For example:

\`\`\`
// Previously, nums: (number \| null)\[]// Now, nums: number\[]const nums = \[1, 2, 3, null, 5].filter(x =\> x !== null);nums.push(null); // ok in TS 5\.4, error in TS 5\.5
\`\`\`
The fix is to tell TypeScript the type that you want using an explicit type annotation:

\`\`\`
const nums: (number \| null)\[] = \[1, 2, 3, null, 5].filter(x =\> x !== null);nums.push(null); // ok in all versions
\`\`\`
For more information, check out the [implementing pull request](https://github.com/microsoft/TypeScript/pull/57465) and [Dan’s blog post about implementing this feature](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/).

## Control Flow Narrowing for Constant Indexed Accesses

TypeScript is now able to narrow expressions of the form `obj[key]` when both `obj` and `key` are effectively constant.

\`\`\`
function f1(obj: Record\, key: string) { if (typeof obj\[key] === "string") { // Now okay, previously was error obj\[key].toUpperCase(); }}
\`\`\`
In the above, neither `obj` nor `key` are ever mutated, so TypeScript can narrow the type of `obj[key]` to `string` after the `typeof` check.
For more information, [see the implementing pull request here](https://github.com/microsoft/TypeScript/pull/57847).

## The JSDoc `@import` Tag

Today, if you want to import something only for type\-checking in a JavaScript file, it is cumbersome.
JavaScript developers can’t simply import a type named `SomeType` if it’s not there at runtime.

\`\`\`
// ./some\-module.d.tsexport interface SomeType { // ...}// ./index.jsimport { SomeType } from "./some\-module"; // ❌ runtime error!/\*\* \* @param {SomeType} myValue \*/function doSomething(myValue) { // ...}
\`\`\`
`SomeType` won’t exist at runtime, so the import will fail.
Developers can instead use a namespace import instead.

\`\`\`
import \* as someModule from "./some\-module";/\*\* \* @param {someModule.SomeType} myValue \*/function doSomething(myValue) { // ...}
\`\`\`
But `./some-module` is still imported at runtime \- which might also not be desirable.

To avoid this, developers typically had to use `import(...)` types in JSDoc comments.

\`\`\`
/\*\* \* @param {import("./some\-module").SomeType} myValue \*/function doSomething(myValue) { // ...}
\`\`\`
If you wanted to reuse the same type in multiple places, you could use a `typedef` to avoid repeating the import.

\`\`\`
/\*\* \* @typedef {import("./some\-module").SomeType} SomeType \*//\*\* \* @param {SomeType} myValue \*/function doSomething(myValue) { // ...}
\`\`\`
This helps with local uses of `SomeType`, but it gets repetitive for many imports and can be a bit verbose.

That’s why TypeScript now supports a new `@import` comment tag that has the same syntax as ECMAScript imports.

\`\`\`
/\*\* @import { SomeType } from "some\-module" \*//\*\* \* @param {SomeType} myValue \*/function doSomething(myValue) { // ...}
\`\`\`
Here, we used named imports.
We could also have written our import as a namespace import.

\`\`\`
/\*\* @import \* as someModule from "some\-module" \*//\*\* \* @param {someModule.SomeType} myValue \*/function doSomething(myValue) { // ...}
\`\`\`
Because these are just JSDoc comments, they don’t affect runtime behavior at all.

We would like to extend a big thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who contributed [this change](https://github.com/microsoft/TypeScript/pull/57207)!

## Regular Expression Syntax Checking

Until now, TypeScript has typically skipped over most regular expressions in code.
This is because regular expressions technically have an extensible grammar and TypeScript never made any effort to compile regular expressions to earlier versions of JavaScript.
Still, this meant that lots of common problems would go undiscovered in regular expressions, and they would either turn into errors at runtime, or silently fail.

But TypeScript now does basic syntax checking on regular expressions!

\`\`\`
let myRegex = /@robot(\\s\+(please\|immediately)))? do some task/;// \~// error!// Unexpected ')'. Did you mean to escape it with backslash?
\`\`\`
This is a simple example, but this checking can catch a lot of common mistakes.
In fact, TypeScript’s checking goes slightly beyond syntactic checks.
For instance, TypeScript can now catch issues around backreferences that don’t exist.

\`\`\`
let myRegex = /@typedef \\{import\\((.\+)\\)\\.(\[a\-zA\-Z\_]\+)\\} \\3/u;// \~// error!// This backreference refers to a group that does not exist.// There are only 2 capturing groups in this regular expression.
\`\`\`
The same applies to named capturing groups.

\`\`\`
let myRegex = /@typedef \\{import\\((?\.\+)\\)\\.(?\\[a\-zA\-Z\_]\+)\\} \\k\/;// \~\~\~\~\~\~\~\~\~\~\~// error!// There is no capturing group named 'namedImport' in this regular expression.
\`\`\`
TypeScript’s checking is now also aware of when certain RegExp features are used when newer than your target version of ECMAScript.
For example, if we use named capturing groups like the above in an ES5 target, we’ll get an error.

\`\`\`
let myRegex = /@typedef \\{import\\((?\.\+)\\)\\.(?\\[a\-zA\-Z\_]\+)\\} \\k\/;// \~\~\~\~\~\~\~\~\~\~\~\~ \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~// error!// Named capturing groups are only available when targeting 'ES2018' or later.
\`\`\`
The same is true for certain regular expression flags as well.

Note that TypeScript’s regular expression support is limited to regular expression *literals*.
If you try calling `new RegExp` with a string literal, TypeScript will not check the provided string.

We would like to thank [GitHub user graphemecluster](https://github.com/graphemecluster/) who iterated a ton with us [to get this feature into TypeScript](https://github.com/microsoft/TypeScript/pull/55600).

## Support for New ECMAScript `Set` Methods

TypeScript 5\.5 declares [new proposed methods for the ECMAScript `Set` type](https://github.com/tc39/proposal-set-methods).

Some of these methods, like `union`, `intersection`, `difference`, and `symmetricDifference`, take another `Set` and return a new `Set` as the result.
The other methods, `isSubsetOf`, `isSupersetOf`, and `isDisjointFrom`, take another `Set` and return a `boolean`.
None of these methods mutate the original `Set`s.

Here’s a quick example of how you might use these methods and how they behave:

\`\`\`
let fruits = new Set(\["apples", "bananas", "pears", "oranges"]);let applesAndBananas = new Set(\["apples", "bananas"]);let applesAndOranges = new Set(\["apples", "oranges"]);let oranges = new Set(\["oranges"]);let emptySet = new Set();////// union////// Set(4\) {'apples', 'bananas', 'pears', 'oranges'}console.log(fruits.union(oranges));// Set(3\) {'apples', 'bananas', 'oranges'}console.log(applesAndBananas.union(oranges));////// intersection////// Set(2\) {'apples', 'bananas'}console.log(fruits.intersection(applesAndBananas));// Set(0\) {}console.log(applesAndBananas.intersection(oranges));// Set(1\) {'apples'}console.log(applesAndBananas.intersection(applesAndOranges));////// difference////// Set(3\) {'apples', 'bananas', 'pears'}console.log(fruits.difference(oranges));// Set(2\) {'pears', 'oranges'}console.log(fruits.difference(applesAndBananas));// Set(1\) {'bananas'}console.log(applesAndBananas.difference(applesAndOranges));////// symmetricDifference////// Set(2\) {'bananas', 'oranges'}console.log(applesAndBananas.symmetricDifference(applesAndOranges)); // no apples////// isDisjointFrom////// trueconsole.log(applesAndBananas.isDisjointFrom(oranges));// falseconsole.log(applesAndBananas.isDisjointFrom(applesAndOranges));// trueconsole.log(fruits.isDisjointFrom(emptySet));// trueconsole.log(emptySet.isDisjointFrom(emptySet));////// isSubsetOf////// trueconsole.log(applesAndBananas.isSubsetOf(fruits));// falseconsole.log(fruits.isSubsetOf(applesAndBananas));// falseconsole.log(applesAndBananas.isSubsetOf(oranges));// trueconsole.log(fruits.isSubsetOf(fruits));// trueconsole.log(emptySet.isSubsetOf(fruits));////// isSupersetOf////// trueconsole.log(fruits.isSupersetOf(applesAndBananas));// falseconsole.log(applesAndBananas.isSupersetOf(fruits));// falseconsole.log(applesAndBananas.isSupersetOf(oranges));// trueconsole.log(fruits.isSupersetOf(fruits));// falseconsole.log(emptySet.isSupersetOf(fruits));
\`\`\`
We’d like to thank [Kevin Gibbons](https://github.com/bakkot) who not only co\-championed the feature in ECMAScript, but [also provided the declarations for `Set`, `ReadonlySet`, and `ReadonlySetLike` in TypeScript](https://github.com/microsoft/TypeScript/pull/57230)!

## Isolated Declarations

*This section was co\-authored by [Rob Palmer](https://github.com/robpalme) who supported the design of isolated declarations.*

Declaration files (a.k.a. `.d.ts` files) describe the shape of existing libraries and modules to TypeScript.
This lightweight description includes the library’s type signatures and excludes implementation details such as the function bodies.
They are published so that TypeScript can efficiently check your usage of a library without needing to analyse the library itself.
Whilst it is possible to handwrite declaration files, if you are authoring typed code, it’s much safer and simpler to let TypeScript generate them automatically from source files using `--declaration`.

The TypeScript compiler and its APIs have always had the job of generating declaration files;
however, there are some use\-cases where you might want to use other tools, or where the traditional build process doesn’t scale.

### Use\-case: Faster Declaration Emit Tools

Imagine if you wanted to create a faster tool to generate declaration files, perhaps as part of a publishing service or a new bundler.
Whilst there is a thriving ecosystem of blazing fast tools that can turn TypeScript into JavaScript, the same is not true for turning TypeScript into declaration files.
The reason is that TypeScript’s inference allows us to write code without explicitly declaring types, meaning declaration emit can be complex.

Let’s consider a simple example of a function that adds two imported variables.

\`\`\`
// util.tsexport let one = "1";export let two = "2";// add.tsimport { one, two } from "./util";export function add() { return one \+ two; }
\`\`\`
Even if the only thing we want to do is generate `add.d.ts`, TypeScript needs to crawl into another imported file (`util.ts`), infer that the type of `one` and `two` are strings, and then calculate that the `+` operator on two strings will lead to a `string` return type.

\`\`\`
// add.d.tsexport declare function add(): string;
\`\`\`
While this inference is important for the developer experience, it means that tools that want to generate declaration files would need to replicate parts of the type\-checker including inference and the ability to resolve module specifiers to follow the imports.

### Use\-case: Parallel Declaration Emit and Parallel Checking

Imagine if you had a monorepo containing many projects and a multi\-core CPU that just wished it could help you check your code faster.
Wouldn’t it be great if we could check all those projects at the same time by running each project on a different core?

Unfortunately we don’t have the freedom to do all the work in parallel.
The reason is that we have to build those projects in dependency order, because each project is checking against the declaration files of their dependencies.
So we must build the dependency first to generate the declaration files.
TypeScript’s project references feature works the same way, building the set of projects in “topological” dependency order.

As an example, if we have two projects called `backend` and `frontend`, and they both depend on a project called `core`, TypeScript can’t start type\-checking either `frontend` or `backend` until `core` has been built and its declaration files have been generated.



In the above graph, you can see that we have a bottleneck.
Whilst we can build `frontend` and `backend` in parallel, we need to first wait for `core` to finish building before either can start.

How could we improve upon this?
Well, if a fast tool could generate all those declaration files for `core` *in parallel*, TypeScript then could immediately follow that by type\-checking `core`, `frontend`, and `backend` also *in parallel*.

### Solution: Explicit Types!

The common requirement in both use\-cases is that we need a cross\-file type\-checker to generate declaration files.
Which is a lot to ask from the tooling community.

As a more complex example, if we want a declaration file for the following code…

\`\`\`
import { add } from "./add";const x = add();export function foo() { return x;}
\`\`\`
…we would need to generate a signature for `foo`.
Well that requires looking at the implementation of `foo`.
`foo` just returns `x`, so getting the type of `x` requires looking at the implementation of `add`.
But that might require looking at the implementation of `add`’s dependencies, and so on.
What we’re seeing here is that generating declaration files requires a whole lot of logic to figure out the types of different places that might not even be local to the current file.

Still, for developers looking for fast iteration time and fully parallel builds, there is another way of thinking about this problem.
A declaration file only requires the types of the public API of a module \- in other words, the types of the things that are exported.
If, controversially, developers are willing to explicitly write out the types of the things they export, tools could generate declaration files without needing to look at the implementation of the module \- and without reimplementing a full type\-checker.

This is where the new `--isolatedDeclarations` option comes in.
`--isolatedDeclarations` reports errors when a module can’t be reliably transformed without a type\-checker.
More plainly, it makes TypeScript report errors if you have a file that isn’t sufficiently annotated on its exports.

That means in the above example, we would see an error like the following:

\`\`\`
export function foo() {// \~\~\~// error! Function must have an explicit// return type annotation with \-\-isolatedDeclarations. return x;}
\`\`\`
### Why are errors desirable?

Because it means that TypeScript can

1. Tell us up\-front whether other tools will have issues with generating declaration files
2. Provide a quick fix to help add these missing annotations.

This mode doesn’t require annotations *everywhere* though.
For locals, these can be ignored, since they don’t affect the public API.
For example, the following code would **not** produce an error:

\`\`\`
import { add } from "./add";const x = add("1", "2"); // no error on 'x', it's not exported.export function foo(): string { return x;}
\`\`\`
There are also certain expressions where the type is “trivial” to calculate.

\`\`\`
// No error on 'x'.// It's trivial to calculate the type is 'number'export let x = 10;// No error on 'y'.// We can get the type from the return expression.export function y() { return 20;}// No error on 'z'.// The type assertion makes it clear what the type is.export function z() { return Math.max(x, y()) as number;}
\`\`\`
### Using `isolatedDeclarations`

`isolatedDeclarations` requires that either the `declaration` or `composite` flags are also set.

Note that `isolatedDeclarations` does not change how TypeScript performs emit \- just how it reports errors.
Importantly, and similar to `isolatedModules`, enabling the feature in TypeScript won’t immediately bring about the potential benefits discussed here.
So please be patient and look forward to future developments in this space.
Keeping tool authors in mind, we should also recognize that today, not all of TypeScript’s declaration emit can be easily replicated by other tools wanting to use it as a guide.
That’s something we’re actively working on improving.

On top of this, isolated declarations are still a new feature, and we’re actively working on improving the experience.
Some scenarios, like using computed property declarations in classes and object literals, are not *yet* supported under `isolatedDeclarations`.
Keep an eye on this space, and feel free to provide us with feedback.

We also feel it is worth calling out that `isolatedDeclarations` should be adopted on a case\-by\-case basis.
There are some developer ergonomics that are lost when using `isolatedDeclarations`, and thus it may not be the right choice if your setup is not leveraging the two scenarios mentioned earlier.
For others, the work on `isolatedDeclarations` has already uncovered many optimizations and opportunities to unlock different parallel build strategies.
In the meantime, if you’re willing to make the trade\-offs, we believe `isolatedDeclarations` can be a powerful tool to speed up your build process as external tooling becomes more widely available.

For more information, read up on the [Isolated Declarations: State of the Feature](https://github.com/microsoft/TypeScript/issues/58944) discussion on the TypeScript issue tracker.

### Credit

Work on `isolatedDeclarations` has been a long\-time collaborative effort between the TypeScript team and the infrastructure and tooling teams within Bloomberg and Google.
Individuals like Hana Joo from Google who implemented [the quick fix for isolated declaration errors](https://github.com/microsoft/TypeScript/pull/58260) (more on that soon), as well as Ashley Claymore, Jan Kühle, Lisa Velden, Rob Palmer, and Thomas Chetwin have been involved in discussion, specification, and implementation for many months.
But we feel it is specifically worth calling out the tremendous amount of work provided by [Titian Cernicova\-Dragomir](https://github.com/dragomirtitian) from Bloomberg.
Titian has been instrumental in driving the implementation of `isolatedDeclarations` and has been a contributor to the TypeScript project for years prior.

While the feature involved many changes, you can see [the core work for Isolated Declarations here](https://github.com/microsoft/TypeScript/pull/58201).

## The `${configDir}` Template Variable for Configuration Files

It’s common in many codebases to reuse a shared `tsconfig.json` file that acts as a “base” for other configuration files.
This is done by using the `extends` field in a `tsconfig.json` file.

\`\`\`
{ "extends": "../../tsconfig.base.json", "compilerOptions": { "outDir": "./dist" }}
\`\`\`
One of the issues with this is that all paths in the `tsconfig.json` file are relative to the location of the file itself.
This means that if you have a shared `tsconfig.base.json` file that is used by multiple projects, relative paths often won’t be useful in the derived projects.
For example, imagine the following `tsconfig.base.json`:

\`\`\`
{ "compilerOptions": { "typeRoots": \[ "./node\_modules/@types" "./custom\-types" ], "outDir": "dist" }}
\`\`\`
If author’s intent was that every `tsconfig.json` that extends this file should

1. output to a `dist` directory relative to the derived `tsconfig.json` , and
2. have a `custom-types` directory relative to the derived `tsconfig.json`,

then this would not work.
The `typeRoots` paths would be relative to the location of the shared `tsconfig.base.json` file, not the project that extends it.
Each project that extends this shared file would need to declare its own `outDir` and `typeRoots` with identical contents.
This could be frustrating and hard to keep in sync between projects, and while the example above is using `typeRoots`, this is a common problem for `paths` and other options.

To solve this, TypeScript 5\.5 introduces a new template variable `${configDir}`.
When `${configDir}` is written in certain path fields of a `tsconfig.json` or `jsconfig.json` files, this variable is substituted with the containing directory of the configuration file in a given compilation.
This means that the above `tsconfig.base.json` could be rewritten as:

\`\`\`
{ "compilerOptions": { "typeRoots": \[ "${configDir}/node\_modules/@types" "${configDir}/custom\-types" ], "outDir": "${configDir}/dist" }}
\`\`\`
Now, when a project extends this file, the paths will be relative to the derived `tsconfig.json`, not the shared `tsconfig.base.json` file.
This makes it easier to share configuration files across projects and ensures that the configuration files are more portable.

If you intend to make a `tsconfig.json` file extendable, consider if a `./` should instead be written with `${configDir}`.

For more information, see [the proposal issue](https://github.com/microsoft/TypeScript/issues/57485) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/58042).

## Consulting `package.json` Dependencies for Declaration File Generation

Previously, TypeScript would often issue an error message like

\`\`\`
The inferred type of "X" cannot be named without a reference to "Y". This is likely not portable. A type annotation is necessary.
\`\`\`
This was often due to TypeScript’s declaration file generation finding itself in the contents of files that were never explicitly imported in a program.
Generating an import to such a file could be risky if the path ended up being relative.
Still, for codebases with explicit dependencies in the `dependencies` (or `peerDependencies` and `optionalDependencies`) of a `package.json`, generating such an import should be safe under certain resolution modes.
So in TypeScript 5\.5, we’re more lenient when that’s the case, and many occurrences of this error should disappear.

[See this pull request](https://github.com/microsoft/TypeScript/issues/42873) for more details on the change.

## Editor and Watch\-Mode Reliability Improvements

TypeScript has either added some new functionality or fixed existing logic that makes `--watch` mode and TypeScript’s editor integration feel more reliable.
That should hopefully translate to fewer TSServer/editor restarts.

### Correctly Refresh Editor Errors in Configuration Files

TypeScript can generate errors for `tsconfig.json` files;
however, those errors are actually generated from loading a project, and editors typically don’t directly request those errors for `tsconfig.json` files.
While this sounds like a technical detail, it means that when all errors issued in a `tsconfig.json` are fixed, TypeScript doesn’t issue a new fresh empty set of errors, and users are left with stale errors unless they reload their editor.

TypeScript 5\.5 now intentionally issues an event to clear these out.
[See more here](https://github.com/microsoft/TypeScript/pull/58120).

### Better Handling for Deletes Followed by Immediate Writes

Instead of overwriting files, some tools will opt to delete them and then create new files from scratch.
This is the case when running `npm ci`, for instance.

While this can be efficient for those tools, it can be problematic for TypeScript’s editor scenarios where deleting a watched might dispose of it and all of its transitive dependencies.
Deleting and creating a file in quick succession could lead to TypeScript tearing down an entire project and then rebuilding it from scratch.

TypeScript 5\.5 now has a more nuanced approach by keeping parts of a deleted project around until it picks up on a new creation event.
This should make operations like `npm ci` work a lot better with TypeScript.
See [more information on the approach here](https://github.com/microsoft/TypeScript/pull/57492).

### Symlinks are Tracked in Failed Resolutions

When TypeScript fails to resolve a module, it will still need to watch for any failed lookup paths in case the module is added later.
Previously this was not done for symlinked directories, which could cause reliability issues in monorepo\-like scenarios when a build occurred in one project but was not witnessed in the other.
This should be fixed in TypeScript 5\.5, and means you won’t need to restart your editor as often.

[See more information here](https://github.com/microsoft/TypeScript/pull/58139).

### Project References Contribute to Auto\-Imports

Auto\-imports no longer requires at least one explicit import to dependent projects in a project reference setup.
Instead, auto\-import completions should just work across anything you’ve listed in the `references` field of your `tsconfig.json`.

[See more on the implementing pull request](https://github.com/microsoft/TypeScript/pull/55955).

## Performance and Size Optimizations

### Monomorphized Objects in Language Service and Public API

In TypeScript 5\.0, we ensured that our [`Node`](https://github.com/microsoft/TypeScript/pull/51682) and [`Symbol`](https://github.com/microsoft/TypeScript/pull/51880) objects had a consistent set of properties with a consistent initialization order.
Doing so helps reduce polymorphism in different operations, which allows runtimes to fetch properties more quickly.

By making this change, we witnessed impressive speed wins in the compiler;
however, most of these changes were performed on internal allocators for our data structures.
The language service, along with TypeScript’s public API, uses a different set of allocators for certain objects.
This allowed the TypeScript compiler to be a bit leaner, as data used only for the language service would never be used in the compiler.

In TypeScript 5\.5, the same monomorphization work has been done for the language service and public API.
What this means is that your editor experience, and any build tools that use the TypeScript API, will get a decent amount faster.
In fact, in our benchmarks, we’ve seen a **5\-8% speedup in build times** when using the public TypeScript API’s allocators, and **language service operations getting 10\-20% faster**.
While this does imply an increase in memory, we believe that tradeoff is worth it and hope to find ways to reduce that memory overhead.
Things should feel a lot snappier now.

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/58045).

### Monomorphized Control Flow Nodes

In TypeScript 5\.5, nodes of the control flow graph have been monomorphized so that they always hold a consistent shape.
By doing so, check times will often be reduced by about 1%.

[See this change here](https://github.com/microsoft/TypeScript/pull/57977).

### Optimizations on our Control Flow Graph

In many cases, control flow analysis will traverse nodes that don’t provide any new information.
We observed that in the absence of any early termination or effects in the antecedents (or “dominators”) of certain nodes meant that those nodes could always be skipped over.
As such, TypeScript now constructs its control flow graphs to take advantage of this by linking to an earlier node that *does* provide interesting information for control flow analysis.
This yields a flatter control flow graph, which can be more efficient to traverse.
This optimization has yielded modest gains, but with up to 2% reductions in build time on certain codebases.

You can [read more here](https://github.com/microsoft/TypeScript/pull/58013).

### Skipped Checking in `transpileModule` and `transpileDeclaration`

TypeScript’s `transpileModule` API can be used for compiling a single TypeScript file’s contents into JavaScript.
Similarly, the `transpileDeclaration` API (see below) can be used to generate a declaration file for a single TypeScript file.
One of the issues with these APIs is that TypeScript internally would perform a full type\-checking pass over the entire contents of the file before emitting the output.
This was necessary to collect certain information which would later be used for the emit phase.

In TypeScript 5\.5, we’ve found a way to avoid performing a full check, only lazily collecting this information as necessary, and `transpileModule` and `transpileDeclaration` both enable this functionality by default.
As a result, tools that integrate with these APIs, like [ts\-loader](https://www.npmjs.com/package/ts-loader) with `transpileOnly` and [ts\-jest](https://www.npmjs.com/package/ts-jest), should see a noticeable speedup.
In our testing, [we generally witness around a 2x speed\-up in build time using `transpileModule`](https://github.com/microsoft/TypeScript/pull/58364#issuecomment-2138580690).

### TypeScript Package Size Reduction

Further leveraging [our transition to modules in 5\.0](https://devblogs.microsoft.com/typescript/typescripts-migration-to-modules/), we’ve significantly reduced TypeScript’s overall package size [by making `tsserver.js` and `typingsInstaller.js` import from a common API library instead of having each of them produce standalone bundles](https://github.com/microsoft/TypeScript/pull/55326).

This reduces TypeScript’s size on disk from 30\.2 MB to 20\.4 MB, and reduces its packed size from 5\.5 MB to 3\.7 MB!

### Node Reuse in Declaration Emit

As part of the work to enable `isolatedDeclarations`, we’ve substantially improved how often TypeScript can directly copy your input source code when producing declaration files.

For example, let’s say you wrote

\`\`\`
export const strBool: string \| boolean = "hello";export const boolStr: boolean \| string = "world";
\`\`\`
Note that the union types are equivalent, but the order of the union is different.
When emitting the declaration file, TypeScript has two equivalent output possibilities.

The first is to use a consistent canonical representation for each type:

\`\`\`
export const strBool: string \| boolean;export const boolStr: string \| boolean;
\`\`\`
The second is to re\-use the type annotations exactly as written:

\`\`\`
export const strBool: string \| boolean;export const boolStr: boolean \| string;
\`\`\`
The second approach is generally preferable for a few reasons:

* Many equivalent representations still encode some level of intent that is better to preserve in the declaration file
* Producing a fresh representation of a type can be somewhat expensive, so avoiding is better
* User\-written types are usually shorter than generated type representations

In 5\.5, we’ve greatly improved the number of places where TypeScript can correctly identify places where it’s safe and correct to print back types exactly as they were written in the input file.
Many of these cases are invisible performance improvements \- TypeScript would generate fresh sets of syntax nodes and serialize them into a string.
Instead, TypeScript can now operate over the original syntax nodes directly, which is much cheaper and faster.

### Caching Contextual Types from Discriminated Unions

When TypeScript asks for the contextual type of an expression like an object literal, it will often encounter a union type.
In those cases, TypeScript tries to filter out members of the union based on known properties with well known values (i.e. discriminant properties).
This work can be fairly expensive, especially if you end up with an object consisting of many many properties.
In TypeScript 5\.5, [much of the computation is cached once so that TypeScript doesn’t need to recompute it for every property in the object literal](https://github.com/microsoft/TypeScript/pull/58372).
Performing this optimization shaved 250ms off of compiling the TypeScript compiler itself.

## Easier API Consumption from ECMAScript Modules

Previously, if you were writing an ECMAScript module in Node.js, named imports were not available from the `typescript` package.

\`\`\`
import { createSourceFile } from "typescript"; // ❌ errorimport \* as ts from "typescript";ts.createSourceFile // ❌ undefined???ts.default.createSourceFile // ✅ works \- but ugh!
\`\`\`
This is because [cjs\-module\-lexer](https://github.com/nodejs/cjs-module-lexer) did not recognize the pattern of TypeScript’s generated CommonJS code.
This has been fixed, and users can now use named imports from the TypeScript npm package with ECMAScript modules in Node.js.

\`\`\`
import { createSourceFile } from "typescript"; // ✅ works now!import \* as ts from "typescript";ts.createSourceFile // ✅ works now!
\`\`\`
For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/57133).

## The `transpileDeclaration` API

TypeScript’s API exposes a function called `transpileModule`.
It’s intended to make it easy to compile a single file of TypeScript code.
Because it doesn’t have access to an entire *program*, the caveat is that it may not produce the right output if the code violates any errors under the `isolatedModules` option.

In TypeScript 5\.5, we’ve added a new similar API called `transpileDeclaration`.
This API is similar to `transpileModule`, but it’s specifically designed to generate a single *declaration file* based on some input source text.
Just like `transpileModule`, it doesn’t have access to a full program, and a similar caveat applies: it only generates an accurate declaration file if the input code is free of errors under the new `isolatedDeclarations` option.

If desired, this function can be used to parallelize declaration emit across all files under `isolatedDeclarations` mode.

For more information, [see the implementation here](https://github.com/microsoft/TypeScript/pull/58261).

## Notable Behavioral Changes

This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### Disabling Features Deprecated in TypeScript 5\.0

TypeScript 5\.0 deprecated the following options and behaviors:

* `charset`
* `target: ES3`
* `importsNotUsedAsValues`
* `noImplicitUseStrict`
* `noStrictGenericChecks`
* `keyofStringsOnly`
* `suppressExcessPropertyErrors`
* `suppressImplicitAnyIndexErrors`
* `out`
* `preserveValueImports`
* `prepend` in project references
* implicitly OS\-specific `newLine`

To continue using the deprecated options above, developers using TypeScript 5\.0 and other more recent versions have had to specify a new option called `ignoreDeprecations` with the value `"5.0"`.

In TypeScript 5\.5, these options no longer have any effect.
To help with a smooth upgrade path, you may still specify them in your tsconfig, but these will be an error to specify in TypeScript 6\.0\.
See also the [Flag Deprecation Plan](https://github.com/microsoft/TypeScript/issues/51000) which outlines our deprecation strategy.

[More information around these deprecation plans is available on GitHub](https://github.com/microsoft/TypeScript/issues/51909), which contains suggestions in how to best adapt your codebase.

### `lib.d.ts` Changes

Types generated for the DOM may have an impact on type\-checking your codebase.
For more information, [see the DOM updates for TypeScript 5\.5](https://github.com/microsoft/TypeScript/pull/58211).

### Stricter Parsing for Decorators

Since TypeScript originally introduced support for decorators, the specified grammar for the proposal has been tightened up.
TypeScript is now stricter about what forms it allows.
While rare, existing decorators may need to be parenthesized to avoid errors.

\`\`\`
class DecoratorProvider { decorate(...args: any\[]) { }}class D extends DecoratorProvider { m() { class C { @super.decorate // ❌ error method1() { } @(super.decorate) // ✅ okay method2() { } } }}
\`\`\`
See [more information on the change here](https://github.com/microsoft/TypeScript/pull/57749).

### `undefined` is No Longer a Definable Type Name

TypeScript has always disallowed type alias names that conflict with built\-in types:

\`\`\`
// Illegaltype null = any;// Illegaltype number = any;// Illegaltype object = any;// Illegaltype any = any;
\`\`\`
Due to a bug, this logic didn’t also apply to the built\-in type `undefined`.
In 5\.5, this is now correctly identified as an error:

\`\`\`
// Now also illegaltype undefined = any;
\`\`\`
Bare references to type aliases named `undefined` never actually worked in the first place.
You could define them, but you couldn’t use them as an unqualified type name.

\`\`\`
export type undefined = string;export const m: undefined = "";// ^// Errors in 5\.4 and earlier \- the local definition of 'undefined' was not even consulted.
\`\`\`
For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/57575).

### Simplified Reference Directive Declaration Emit

When producing a declaration file, TypeScript would synthesize a reference directive when it believed one was required.
For example, all Node.js modules are declared ambiently, so cannot be loaded by module resolution alone.
A file like:

\`\`\`
import path from "path";export const myPath = path.parse(\_\_filename);
\`\`\`
Would emit a declaration file like:

\`\`\`
/// \import path from "path";export declare const myPath: path.ParsedPath;
\`\`\`
Even though the reference directive never appeared in the original source.

Similarly, TypeScript also *removed* reference directives that it did not believe needed to be a part of the output.
For example, let’s imagine we had a reference directive to `jest`;
however, imagine the reference directive isn’t necessary to generate the declaration file.
TypeScript would simply drop it.
So in the following example:

\`\`\`
/// \import path from "path";export const myPath = path.parse(\_\_filename);
\`\`\`
TypeScript would still emit:

\`\`\`
/// \import path from "path";export declare const myPath: path.ParsedPath;
\`\`\`
In the course of working on `isolatedDeclarations`, we realized that this logic was untenable for anyone attempting to implement a declaration emitter without type checking or using more than a single file’s context.
This behavior is also hard to understand from a user’s perspective; whether or not a reference directive appeared in the emitted file seems inconsistent and difficult to predict unless you understand exactly what’s going on during typechecking.
To prevent declaration emit from being different when `isolatedDeclarations` was enabled, we knew that our emit needed to change.

Through [experimentation](https://github.com/microsoft/TypeScript/pull/57569), we found that nearly all cases where TypeScript synthesized reference directives were just to pull in `node` or `react`.
These are cases where the expectation is that a downstream user already references those types through tsconfig.json `"types"` or library imports, so no longer synthesizing these reference directives would be unlikely to break anyone.
It’s worth noting that this is already how it works for `lib.d.ts`; TypeScript doesn’t synthesize a reference to `lib="es2015"` when a module exports a `WeakMap`, instead assuming that a downstream user will have included that as part of their environment.

For reference directives that had been written by library authors (not synthesized), [further experimentation](https://github.com/microsoft/TypeScript/pull/57656) showed that nearly all were removed, never showing up in the output.
Most reference directives that were preserved were broken and likely not intended to be preserved.

Given those results, we decided to greatly simplfy reference directives in declaration emit in TypeScript 5\.5\.
A more consistent strategy will help library authors and consumers have better control of their declaration files.

Reference directives are no longer synthesized.
User\-written reference directives are no longer preserved, unless annotated with a new `preserve="true"` attribute.
Concretely, an input file like:

\`\`\`
/// \/// \import path from "path";export const myPath = path.parse(\_\_filename);
\`\`\`
will emit:

\`\`\`
/// \import path from "path";export declare const myPath: path.ParsedPath;
\`\`\`
Adding `preserve="true"` is backwards compatible with older versions of TypeScript as unknown attributes are ignored.

This change also improved performance; in our benchmarks, the emit stage saw a 1\-4% improvement in projects with declaration emit enabled.

The TypeScript docs are an open source project. Help us improve these pages [by sending a Pull Request](https://github.com/microsoft/TypeScript-Website/blob/v2/packages/documentation/copy/en/release-notes/TypeScript 5.5.md) ❤

Contributors to this page:  
NDRLast updated: Jan 02, 2025  



