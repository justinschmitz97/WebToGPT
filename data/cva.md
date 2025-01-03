<<<<< https://cva.style/ >>>>>

--- cva: https://cva.style/ ---

# Class Variance Authority

CSS-in-TS libraries such as [Stitches (opens in a new tab)](https://stitches.dev/docs/variants) and [Vanilla Extract (opens in a new tab)](https://vanilla-extract.style/documentation/api/style-variants/) are **fantastic** options for building type-safe UI components; taking away all the worries of class names and StyleSheet composition.

…but CSS-in-TS (or CSS-in-JS) isn't for everyone.

You may need full control over your StyleSheet output. Your job might require you to use a framework such as Tailwind CSS. You might just prefer writing your own CSS.

Creating variants with the "traditional" CSS approach can become an arduous task; manually matching classes to props and manually adding types.

`cva` aims to take those pain points away, allowing you to focus on the more fun aspects of UI development.

## Sponsors

**Want to support this project?**

`cva` is a privately-maintained **free** open-source project.

[**Become a sponsor** (opens in a new tab)](https://polar.sh/cva) to contribute towards development efforts financially.

## Acknowledgements

- [**Stitches** (opens in a new tab)](https://stitches.dev/) ([WorkOS (opens in a new tab)](https://workos.com))

  Huge thanks to the WorkOS team for pioneering the `variants` API movement – your open-source contributions are immensely appreciated

- [**clb** (opens in a new tab)](https://github.com/crswll/clb) ([Bill Criswell (opens in a new tab)](https://github.com/crswll))

  This project originally started out with the intention of merging into the wonderful [`clb` (opens in a new tab)](https://github.com/crswll/clb) library, but after some discussion with Bill, we felt it was best to go down the route of a separate project.

  I'm so grateful to Bill for sharing his work publicly and for getting me excited about building a type-safe variants API for classes. If you have a moment, please go and [star the project on GitHub (opens in a new tab)](https://github.com/crswll/clb). Thank you Bill!

- [**clsx** (opens in a new tab)](https://github.com/lukeed/clsx) ([Luke Edwards (opens in a new tab)](https://github.com/lukeed))

  Previously, this project surfaced a custom `cx` utility for flattening classes, but it lacked the ability to handle variadic arguments or objects. [clsx (opens in a new tab)](https://github.com/lukeed/clsx) provided those extra features with quite literally zero increase to the bundle size – a no-brainer to switch!

- [**Vanilla Extract** (opens in a new tab)](http://vanilla-extract.style) ([Seek (opens in a new tab)](https://github.com/seek-oss))

## Downloads

- [Wallpaper](/assets/img/wallpaper-4k.png)

## License

[Apache-2.0 License (opens in a new tab)](https://github.com/joe-bell/cva/blob/main/LICENSE) © [Joe Bell (opens in a new tab)](https://joebell.studio)

--- cva: https://cva.style/docs ---

# Class Variance Authority

CSS-in-TS libraries such as [Stitches (opens in a new tab)](https://stitches.dev/docs/variants) and [Vanilla Extract (opens in a new tab)](https://vanilla-extract.style/documentation/api/style-variants/) are **fantastic** options for building type-safe UI components; taking away all the worries of class names and StyleSheet composition.

…but CSS-in-TS (or CSS-in-JS) isn't for everyone.

You may need full control over your StyleSheet output. Your job might require you to use a framework such as Tailwind CSS. You might just prefer writing your own CSS.

Creating variants with the "traditional" CSS approach can become an arduous task; manually matching classes to props and manually adding types.

`cva` aims to take those pain points away, allowing you to focus on the more fun aspects of UI development.

## Sponsors

**Want to support this project?**

`cva` is a privately-maintained **free** open-source project.

[**Become a sponsor** (opens in a new tab)](https://polar.sh/cva) to contribute towards development efforts financially.

## Acknowledgements

- [**Stitches** (opens in a new tab)](https://stitches.dev/) ([WorkOS (opens in a new tab)](https://workos.com))

  Huge thanks to the WorkOS team for pioneering the `variants` API movement – your open-source contributions are immensely appreciated

- [**clb** (opens in a new tab)](https://github.com/crswll/clb) ([Bill Criswell (opens in a new tab)](https://github.com/crswll))

  This project originally started out with the intention of merging into the wonderful [`clb` (opens in a new tab)](https://github.com/crswll/clb) library, but after some discussion with Bill, we felt it was best to go down the route of a separate project.

  I'm so grateful to Bill for sharing his work publicly and for getting me excited about building a type-safe variants API for classes. If you have a moment, please go and [star the project on GitHub (opens in a new tab)](https://github.com/crswll/clb). Thank you Bill!

- [**clsx** (opens in a new tab)](https://github.com/lukeed/clsx) ([Luke Edwards (opens in a new tab)](https://github.com/lukeed))

  Previously, this project surfaced a custom `cx` utility for flattening classes, but it lacked the ability to handle variadic arguments or objects. [clsx (opens in a new tab)](https://github.com/lukeed/clsx) provided those extra features with quite literally zero increase to the bundle size – a no-brainer to switch!

- [**Vanilla Extract** (opens in a new tab)](http://vanilla-extract.style) ([Seek (opens in a new tab)](https://github.com/seek-oss))

## Downloads

- [Wallpaper](/assets/img/wallpaper-4k.png)

## License

[Apache-2.0 License (opens in a new tab)](https://github.com/joe-bell/cva/blob/main/LICENSE) © [Joe Bell (opens in a new tab)](https://joebell.studio)

--- API Reference | cva: https://cva.style/docs/api-reference ---

# API Reference

## `cva`

Builds a `cva` component

```
const component = cva("base", options);
```

### Parameters

1. `base`: the base class name (`string`, `string[]` or other [`clsx` value (opens in a new tab)](https://github.com/lukeed/clsx#input))
2. `options` _(optional)_
   - `variants`: your variants schema
   - `compoundVariants`: variants based on a combination of previously defined variants
   - `defaultVariants`: set default values for previously defined variants

     _note: these default values can be removed completely by setting the variant as `null`_

### Returns

A `cva` component function

## `cx`

Concatenates class names (an alias of [`clsx` (opens in a new tab)](https://github.com/lukeed/clsx))

```
const className = cx(classes);
```

### Parameters

- `classes`: array of classes to be concatenated ([see `clsx` usage (opens in a new tab)](https://github.com/lukeed/clsx#input))

### Returns

`string`

--- Other Use Cases | cva: https://cva.style/docs/examples/other-use-cases ---

# Other Use Cases

Although primarily designed for handling class names, at its core, `cva` is really just a fancy way of managing a string…

## Dynamic Text Content

```
const greeter = cva("Good morning!", {
variants: {
isLoggedIn: {
true: "Here's a secret only logged in users can see",
false: "Log in to find out more…",
},
},
defaultVariants: {
isLoggedIn: "false",
},
});
greeter();
// => "Good morning! Log in to find out more…"
greeter({ isLoggedIn: "true" });
// => "Good morning! Here's a secret only logged in users can see"
```

--- React with CSS Modules | cva: https://cva.style/docs/examples/react/css-modules ---

# React with CSS Modules

[View on GitHub ↗](https://github.com/joe-bell/cva/tree/main/examples/latest/react-with-css-modules/src/components/button/button.tsx)

--- React with Tailwind CSS | cva: https://cva.style/docs/examples/react/tailwind-css ---

# React with Tailwind CSS

[View on GitHub ↗](https://github.com/joe-bell/cva/tree/main/examples/latest/react-with-tailwindcss/src/components/button/button.tsx)

--- FAQs | cva: https://cva.style/docs/faqs ---

# FAQs

## Why Don't You Provide a `styled` API?

Long story short: it's unnecessary.

`cva` encourages you to think of components as traditional CSS classes:

- Less JavaScript is better
- They're framework agnostic; truly reusable
- Polymorphism is free; just apply the class to your preferred HTML element
- Less opinionated; you're free to build components with `cva` however you'd like

See the ["Polymorphism"](/docs/getting-started/polymorphism) documentation for further recommendations.

## How Can I Create [Responsive Variants like Stitches.js (opens in a new tab)](https://stitches.dev/docs/responsive-styles#responsive-variants)?

You can't.

`cva` doesn't know about how you choose to apply CSS classes, and it doesn't want to.

We recommend either:

- Showing/hiding elements with different variants, based on your preferred breakpoint.

Example: With Tailwind```
export const Example = () => (
<>

Hidden until sm

Hidden after sm

);

```

* Create a bespoke variant that changes based on the breakpoint.

  *e.g. `button({ intent: "primaryUntilMd" })`*

This is something I've been thinking about since the project's inception, and I've gone back and forth many times on the idea of building it. It's a large undertaking and brings all the complexity of supporting many different build tools and frameworks.

In my experience, "responsive variants" are typically rare, and hiding/showing different elements is usually good enough to get by.

To be frank, I'm probably not going to build/maintain a solution unless someone periodically gives me a thick wad of cash to do so, and even then I'd probably rather spend my free time living my life.



```
