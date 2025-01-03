# https://react.dev/blog

## Introducing react.dev – React

[Read the full article](https://react.dev/blog/2023/03/16/introducing-react-dev)

[Blog](/blog)# Introducing react.dev

March 16, 2023 by [Dan Abramov](https://twitter.com/dan_abramov) and [Rachel Nabors](https://twitter.com/rachelnabors)

---

Today we are thrilled to launch [react.dev](https://react.dev), the new home for React and its documentation. In this post, we would like to give you a tour of the new site.

---

## tl;dr

* The new React site ([react.dev](https://react.dev)) teaches modern React with function components and Hooks.
* We’ve included diagrams, illustrations, challenges, and over 600 new interactive examples.
* The previous React documentation site has now moved to [legacy.reactjs.org](https://legacy.reactjs.org).

## New site, new domain, new homepage

First, a little bit of housekeeping.

To celebrate the launch of the new docs and, more importantly, to clearly separate the old and the new content, we’ve moved to the shorter [react.dev](https://react.dev) domain. The old [reactjs.org](https://reactjs.org) domain will now redirect here.

The old React docs are now archived at [legacy.reactjs.org](https://legacy.reactjs.org). All existing links to the old content will automatically redirect there to avoid “breaking the web”, but the legacy site will not get many more updates.

Believe it or not, React will soon be ten years old. In JavaScript years, it’s like a whole century! We’ve [refreshed the React homepage](https://react.dev) to reflect why we think React is a great way to create user interfaces today, and updated the getting started guides to more prominently mention modern React\-based frameworks.

If you haven’t seen the new homepage yet, check it out!

## Going all\-in on modern React with Hooks

When we released React Hooks in 2018, the Hooks docs assumed the reader is familiar with class components. This helped the community adopt Hooks very swiftly, but after a while the old docs failed to serve the new readers. New readers had to learn React twice: once with class components and then once again with Hooks.

**The new docs teach React with Hooks from the beginning.** The docs are divided in two main sections:

* **[Learn React](/learn)** is a self\-paced course that teaches React from scratch.
* **[API Reference](/reference)** provides the details and usage examples for every React API.

Let’s have a closer look at what you can find in each section.

### Note

There are still a few rare class component use cases that do not yet have a Hook\-based equivalent. Class components remain supported, and are documented in the [Legacy API](/reference/react/legacy) section of the new site.

## Quick start

The Learn section begins with the [Quick Start](/learn) page. It is a short introductory tour of React. It introduces the syntax for concepts like components, props, and state, but doesn’t go into much detail on how to use them.

If you like to learn by doing, we recommend checking out the [Tic\-Tac\-Toe Tutorial](/learn/tutorial-tic-tac-toe) next. It walks you through building a little game with React, while teaching the skills you’ll use every day. Here’s what you’ll build:

App.jsApp.js Reset[Fork](https://codesandbox.io/api/v1/sandboxes/define?undefined&environment=create-react-app "Open in CodeSandbox")\`\`\`
import { useState } from 'react';

function Square({ value, onSquareClick }) {
 return (
 \
 {value}
 \
 );
}

function Board({ xIsNext, squares, onPlay }) {
 function handleClick(i) {
 if (calculateWinner(squares) \|\| squares\[i]) {
 return;
 }
 const nextSquares = squares.slice();
 if (xIsNext) {
 nextSquares\[i] = 'X';
 } else {
 nextSquares\[i] = 'O';
 }
 onPlay(nextSquares);
 }

 const winner = calculateWinner(squares);
 let status;
 if (winner) {
 status = 'Winner: ' \+ winner;
 } else {
 status = 'Next player: ' \+ (xIsNext ? 'X' : 'O');
 }

 return (
 \
 \{status}\
 \
 \ handleClick(0\)} /\>
 \ handleClick(1\)} /\>
 \ handleClick(2\)} /\>
 \
 \
 \ handleClick(3\)} /\>
 \ handleClick(4\)} /\>
 \ handleClick(5\)} /\>
 \
 \
 \ handleClick(6\)} /\>
 \ handleClick(7\)} /\>
 \ handleClick(8\)} /\>
 \
 \
 );
}

export default function Game() {
 const \[history, setHistory] = useState(\[Array(9\).fill(null)]);
 const \[currentMove, setCurrentMove] = useState(0\);
 const xIsNext = currentMove % 2 === 0;
 const currentSquares = history\[currentMove];

 function handlePlay(nextSquares) {
 const nextHistory = \[...history.slice(0, currentMove \+ 1\), nextSquares];
 setHistory(nextHistory);
 setCurrentMove(nextHistory.length \- 1\);
 }

 function jumpTo(nextMove) {
 setCurrentMove(nextMove);
 }

 const moves = history.map((squares, move) =\> {
 let description;
 if (move \> 0\) {
 description = 'Go to move \#' \+ move;
 } else {
 description = 'Go to game start';
 }
 return (
 \
 \ jumpTo(move)}\>{description}\
 \
 );
 });

 return (
 \
 \
 \
 \
 \
 \{moves}\
 \
 \
 );
}

function calculateWinner(squares) {
 const lines = \[
 \[0, 1, 2],
 \[3, 4, 5],
 \[6, 7, 8],
 \[0, 3, 6],
 \[1, 4, 7],
 \[2, 5, 8],
 \[0, 4, 8],
 \[2, 4, 6],
 ];
 for (let i = 0; i \
 {name} {isPacked \&\& '✅'}
 \
 );
}

export default function PackingList() {
 return (
 \
 \Sally Ride's Packing List\
 \
 \
 \
 \
 \
 \
 );
}

\`\`\`Show more Show solutionNext Challenge
Notice the “Show solution” button in the left bottom corner. It’s handy if you want to check yourself!

### Build an intuition with diagrams and illustrations

When we couldn’t figure out how to explain something with code and words alone, we’ve added diagrams that help provide some intuition. For example, here is one of the diagrams from [Preserving and Resetting State](/learn/preserving-and-resetting-state):



When `section` changes to `div`, the `section` is deleted and the new `div` is added

You’ll also see some illustrations throughout the docs—here’s one of the [browser painting the screen](/learn/render-and-commit#epilogue-browser-paint):

Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)

We’ve confirmed with the browser vendors that this depiction is 100% scientifically accurate.

## A new, detailed API Reference

In the [API Reference](/reference/react), every React API now has a dedicated page. This includes all kinds of APIs:

* Built\-in Hooks like [`useState`](/reference/react/useState).
* Built\-in components like [``](/reference/react/Suspense).
* Built\-in browser components like [``](/reference/react-dom/components/input).
* Framework\-oriented APIs like [`renderToPipeableStream`](/reference/react-dom/server/renderToReadableStream).
* Other React APIs like [`memo`](/reference/react/memo).

You’ll notice that every API page is split into at least two segments: *Reference* and *Usage*.

[Reference](/reference/react/useState#reference) describes the formal API signature by listing its arguments and return values. It’s concise, but it can feel a bit abstract if you’re not familiar with that API. It describes what an API does, but not how to use it.

[Usage](/reference/react/useState#usage) shows why and how you would use this API in practice, like a colleague or a friend might explain. It shows the **canonical scenarios for how each API was meant to be used by the React team.** We’ve added color\-coded snippets, examples of using different APIs together, and recipes that you can copy and paste from:

#### Basic useState examples

1. Counter (number) 2. Text field (string) 3. Checkbox (boolean) 4. Form (two variables) #### Example 1 of 4: Counter (number)

In this example, the `count` state variable holds a number. Clicking the button increments it.

App.jsApp.js Reset[Fork](https://codesandbox.io/api/v1/sandboxes/define?undefined&environment=create-react-app "Open in CodeSandbox")\`\`\`
import { useState } from 'react';

export default function Counter() {
 const \[count, setCount] = useState(0\);

 function handleClick() {
 setCount(count \+ 1\);
 }

 return (
 \
 You pressed me {count} times
 \
 );
}

\`\`\`Next Example
Some API pages also include [Troubleshooting](/reference/react/useEffect#troubleshooting) (for common problems) and [Alternatives](/reference/react-dom/findDOMNode#alternatives) (for deprecated APIs).

We hope that this approach will make the API reference useful not only as a way to look up an argument, but as a way to see all the different things you can do with any given API—and how it connects to the other ones.

## What’s next?

That’s a wrap for our little tour! Have a look around the new website, see what you like or don’t like, and keep the feedback coming in our [issue tracker](https://github.com/reactjs/react.dev/issues).

We acknowledge this project has taken a long time to ship. We wanted to maintain a high quality bar that the React community deserves. While writing these docs and creating all of the examples, we found mistakes in some of our own explanations, bugs in React, and even gaps in the React design that we are now working to address. We hope that the new documentation will help us hold React itself to a higher bar in the future.

We’ve heard many of your requests to expand the content and functionality of the website, for example:

* Providing a TypeScript version for all examples;
* Creating the updated performance, testing, and accessibility guides;
* Documenting React Server Components independently from the frameworks that support them;
* Working with our international community to get the new docs translated;
* Adding missing features to the new website (for example, RSS for this blog).

Now that [react.dev](https://react.dev/) is out, we will be able to shift our focus from “catching up” with the third\-party React educational resources to adding new information and further improving our new website.

We think there’s never been a better time to learn React.

## Who worked on this?

On the React team, [Rachel Nabors](https://twitter.com/rachelnabors/) led the project (and provided the illustrations), and [Dan Abramov](https://twitter.com/dan_abramov) designed the curriculum. They co\-authored most of the content together as well.

Of course, no project this large happens in isolation. We have a lot of people to thank!

[Sylwia Vargas](https://twitter.com/SylwiaVargas) overhauled our examples to go beyond “foo/bar/baz” and kittens, and feature scientists, artists and cities from around the world. [Maggie Appleton](https://twitter.com/Mappletons) turned our doodles into a clear diagram system.

Thanks to [David McCabe](https://twitter.com/mcc_abe), [Sophie Alpert](https://twitter.com/sophiebits), [Rick Hanlon](https://twitter.com/rickhanlonii), [Andrew Clark](https://twitter.com/acdlite), and [Matt Carroll](https://twitter.com/mattcarrollcode) for additional writing contributions. We’d also like to thank [Natalia Tepluhina](https://twitter.com/n_tepluhina) and [Sebastian Markbåge](https://twitter.com/sebmarkbage) for their ideas and feedback.

Thanks to [Dan Lebowitz](https://twitter.com/lebo) for the site design and [Razvan Gradinar](https://dribbble.com/GradinarRazvan) for the sandbox design.

On the development front, thanks to [Jared Palmer](https://twitter.com/jaredpalmer) for prototype development. Thanks to [Dane Grant](https://twitter.com/danecando) and [Dustin Goodman](https://twitter.com/dustinsgoodman) from [ThisDotLabs](https://www.thisdot.co/) for their support on UI development. Thanks to [Ives van Hoorne](https://twitter.com/CompuIves), [Alex Moldovan](https://twitter.com/alexnmoldovan), [Jasper De Moor](https://twitter.com/JasperDeMoor), and [Danilo Woznica](https://twitter.com/danilowoz) from [CodeSandbox](https://codesandbox.io/) for their work with sandbox integration. Thanks to [Rick Hanlon](https://twitter.com/rickhanlonii) for spot development and design work, finessing our colors and finer details. Thanks to [Harish Kumar](https://www.strek.in/) and [Luna Ruan](https://twitter.com/lunaruan) for adding new features to the site and helping maintain it.

Huge thanks to the folks who volunteered their time to participate in the alpha and beta testing program. Your enthusiasm and invaluable feedback helped us shape these docs. A special shout out to our beta tester, [Debbie O’Brien](https://twitter.com/debs_obrien), who gave a talk about her experience using the React docs at React Conf 2021\.

Finally, thanks to the React community for being the inspiration behind this effort. You are the reason we do this, and we hope that the new docs will help you use React to build any user interface that you want.

[PreviousReact Labs: What We've Been Working On – March 2023](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023)[NextReact Labs: What We've Been Working On – June 2022](/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022)

---



## React Labs: What We've Been Working On – March 2023 – React

[Read the full article](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023)

[Blog](/blog)# React Labs: What We've Been Working On – March 2023

March 22, 2023 by [Joseph Savona](https://twitter.com/en_JS), [Josh Story](https://twitter.com/joshcstory), [Lauren Tan](https://twitter.com/potetotes), [Mengdi Chen](https://twitter.com/mengdi_en), [Samuel Susla](https://twitter.com/SamuelSusla), [Sathya Gunasekaran](https://twitter.com/_gsathya), [Sebastian Markbåge](https://twitter.com/sebmarkbage), and [Andrew Clark](https://twitter.com/acdlite)

---

In React Labs posts, we write about projects in active research and development. We’ve made significant progress on them since our [last update](/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022), and we’d like to share what we learned.

---

## React Server Components

React Server Components (or RSC) is a new application architecture designed by the React team.

We’ve first shared our research on RSC in an [introductory talk](/blog/2020/12/21/data-fetching-with-react-server-components) and an [RFC](https://github.com/reactjs/rfcs/pull/188). To recap them, we are introducing a new kind of component—Server Components—that run ahead of time and are excluded from your JavaScript bundle. Server Components can run during the build, letting you read from the filesystem or fetch static content. They can also run on the server, letting you access your data layer without having to build an API. You can pass data by props from Server Components to the interactive Client Components in the browser.

RSC combines the simple “request/response” mental model of server\-centric Multi\-Page Apps with the seamless interactivity of client\-centric Single\-Page Apps, giving you the best of both worlds.

Since our last update, we have merged the [React Server Components RFC](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md) to ratify the proposal. We resolved outstanding issues with the [React Server Module Conventions](https://github.com/reactjs/rfcs/blob/main/text/0227-server-module-conventions.md) proposal, and reached consensus with our partners to go with the `"use client"` convention. These documents also act as specification for what an RSC\-compatible implementation should support.

The biggest change is that we introduced [`async` / `await`](https://github.com/reactjs/rfcs/pull/229) as the primary way to do data fetching from Server Components. We also plan to support data loading from the client by introducing a new Hook called `use` that unwraps Promises. Although we can’t support `async / await` in arbitrary components in client\-only apps, we plan to add support for it when you structure your client\-only app similar to how RSC apps are structured.

Now that we have data fetching pretty well sorted, we’re exploring the other direction: sending data from the client to the server, so that you can execute database mutations and implement forms. We’re doing this by letting you pass Server Action functions across the server/client boundary, which the client can then call, providing seamless RPC. Server Actions also give you progressively enhanced forms before JavaScript loads.

React Server Components has shipped in [Next.js App Router](/learn/start-a-new-react-project#nextjs-app-router). This showcases a deep integration of a router that really buys into RSC as a primitive, but it’s not the only way to build a RSC\-compatible router and framework. There’s a clear separation for features provided by the RSC spec and implementation. React Server Components is meant as a spec for components that work across compatible React frameworks.

We generally recommend using an existing framework, but if you need to build your own custom framework, it is possible. Building your own RSC\-compatible framework is not as easy as we’d like it to be, mainly due to the deep bundler integration needed. The current generation of bundlers are great for use on the client, but they weren’t designed with first\-class support for splitting a single module graph between the server and the client. This is why we’re now partnering directly with bundler developers to get the primitives for RSC built\-in.

## Asset Loading

[Suspense](/reference/react/Suspense) lets you specify what to display on the screen while the data or code for your components is still being loaded. This lets your users progressively see more content while the page is loading as well as during the router navigations that load more data and code. However, from the user’s perspective, data loading and rendering do not tell the whole story when considering whether new content is ready. By default, browsers load stylesheets, fonts, and images independently, which can lead to UI jumps and consecutive layout shifts.

We’re working to fully integrate Suspense with the loading lifecycle of stylesheets, fonts, and images, so that React takes them into account to determine whether the content is ready to be displayed. Without any change to the way you author your React components, updates will behave in a more coherent and pleasing manner. As an optimization, we will also provide a manual way to preload assets like fonts directly from components.

We are currently implementing these features and will have more to share soon.

## Document Metadata

Different pages and screens in your app may have different metadata like the `` tag, description, and other `` tags specific to this screen. From the maintenance perspective, it’s more scalable to keep this information close to the React component for that page or screen. However, the HTML tags for this metadata need to be in the document `` which is typically rendered in a component at the very root of your app.

Today, people solve this problem with one of the two techniques.

One technique is to render a special third\-party component that moves ``, ``, and other tags inside it into the document ``. This works for major browsers but there are many clients which do not run client\-side JavaScript, such as Open Graph parsers, and so this technique is not universally suitable.

Another technique is to server\-render the page in two parts. First, the main content is rendered and all such tags are collected. Then, the `` is rendered with these tags. Finally, the `` and the main content are sent to the browser. This approach works, but it prevents you from taking advantage of the [React 18’s Streaming Server Renderer](/reference/react-dom/server/renderToReadableStream) because you’d have to wait for all content to render before sending the ``.

This is why we’re adding built\-in support for rendering ``, ``, and metadata `` tags anywhere in your component tree out of the box. It would work the same way in all environments, including fully client\-side code, SSR, and in the future, RSC. We will share more details about this soon.

## React Optimizing Compiler

Since our previous update we’ve been actively iterating on the design of [React Forget](/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022#react-compiler), an optimizing compiler for React. We’ve previously talked about it as an “auto\-memoizing compiler”, and that is true in some sense. But building the compiler has helped us understand React’s programming model even more deeply. A better way to understand React Forget is as an automatic *reactivity* compiler.

The core idea of React is that developers define their UI as a function of the current state. You work with plain JavaScript values — numbers, strings, arrays, objects — and use standard JavaScript idioms — if/else, for, etc — to describe your component logic. The mental model is that React will re\-render whenever the application state changes. We believe this simple mental model and keeping close to JavaScript semantics is an important principle in React’s programming model.

The catch is that React can sometimes be *too* reactive: it can re\-render too much. For example, in JavaScript we don’t have cheap ways to compare if two objects or arrays are equivalent (having the same keys and values), so creating a new object or array on each render may cause React to do more work than it strictly needs to. This means developers have to explicitly memoize components so as to not over\-react to changes.

Our goal with React Forget is to ensure that React apps have just the right amount of reactivity by default: that apps re\-render only when state values *meaningfully* change. From an implementation perspective this means automatically memoizing, but we believe that the reactivity framing is a better way to understand React and Forget. One way to think about this is that React currently re\-renders when object identity changes. With Forget, React re\-renders when the semantic value changes — but without incurring the runtime cost of deep comparisons.

In terms of concrete progress, since our last update we have substantially iterated on the design of the compiler to align with this automatic reactivity approach and to incorporate feedback from using the compiler internally. After some significant refactors to the compiler starting late last year, we’ve now begun using the compiler in production in limited areas at Meta. We plan to open\-source it once we’ve proved it in production.

Finally, a lot of people have expressed interest in how the compiler works. We’re looking forward to sharing a lot more details when we prove the compiler and open\-source it. But there are a few bits we can share now:

The core of the compiler is almost completely decoupled from Babel, and the core compiler API is (roughly) old AST in, new AST out (while retaining source location data). Under the hood we use a custom code representation and transformation pipeline in order to do low\-level semantic analysis. However, the primary public interface to the compiler will be via Babel and other build system plugins. For ease of testing we currently have a Babel plugin which is a very thin wrapper that calls the compiler to generate a new version of each function and swap it in.

As we refactored the compiler over the last few months, we wanted to focus on refining the core compilation model to ensure we could handle complexities such as conditionals, loops, reassignment, and mutation. However, JavaScript has a lot of ways to express each of those features: if/else, ternaries, for, for\-in, for\-of, etc. Trying to support the full language up\-front would have delayed the point where we could validate the core model. Instead, we started with a small but representative subset of the language: let/const, if/else, for loops, objects, arrays, primitives, function calls, and a few other features. As we gained confidence in the core model and refined our internal abstractions, we expanded the supported language subset. We’re also explicit about syntax we don’t yet support, logging diagnostics and skipping compilation for unsupported input. We have utilities to try the compiler on Meta’s codebases and see what unsupported features are most common so we can prioritize those next. We’ll continue incrementally expanding towards supporting the whole language.

Making plain JavaScript in React components reactive requires a compiler with a deep understanding of semantics so that it can understand exactly what the code is doing. By taking this approach, we’re creating a system for reactivity within JavaScript that lets you write product code of any complexity with the full expressivity of the language, instead of being limited to a domain specific language.

## Offscreen Rendering

Offscreen rendering is an upcoming capability in React for rendering screens in the background without additional performance overhead. You can think of it as a version of the [`content-visibility` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility) that works not only for DOM elements but React components, too. During our research, we’ve discovered a variety of use cases:

* A router can prerender screens in the background so that when a user navigates to them, they’re instantly available.
* A tab switching component can preserve the state of hidden tabs, so the user can switch between them without losing their progress.
* A virtualized list component can prerender additional rows above and below the visible window.
* When opening a modal or popup, the rest of the app can be put into “background” mode so that events and updates are disabled for everything except the modal.

Most React developers will not interact with React’s offscreen APIs directly. Instead, offscreen rendering will be integrated into things like routers and UI libraries, and then developers who use those libraries will automatically benefit without additional work.

The idea is that you should be able to render any React tree offscreen without changing the way you write your components. When a component is rendered offscreen, it does not actually *mount* until the component becomes visible — its effects are not fired. For example, if a component uses `useEffect` to log analytics when it appears for the first time, prerendering won’t mess up the accuracy of those analytics. Similarly, when a component goes offscreen, its effects are unmounted, too. A key feature of offscreen rendering is that you can toggle the visibility of a component without losing its state.

Since our last update, we’ve tested an experimental version of prerendering internally at Meta in our React Native apps on Android and iOS, with positive performance results. We’ve also improved how offscreen rendering works with Suspense — suspending inside an offscreen tree will not trigger Suspense fallbacks. Our remaining work involves finalizing the primitives that are exposed to library developers. We expect to publish an RFC later this year, alongside an experimental API for testing and feedback.

## Transition Tracing

The Transition Tracing API lets you detect when [React Transitions](/reference/react/useTransition) become slower and investigate why they may be slow. Following our last update, we have completed the initial design of the API and published an [RFC](https://github.com/reactjs/rfcs/pull/238). The basic capabilities have also been implemented. The project is currently on hold. We welcome feedback on the RFC and look forward to resuming its development to provide a better performance measurement tool for React. This will be particularly useful with routers built on top of React Transitions, like the [Next.js App Router](/learn/start-a-new-react-project#nextjs-app-router).

---

In addition to this update, our team has made recent guest appearances on community podcasts and livestreams to speak more on our work and answer questions.

* [Dan Abramov](https://twitter.com/dan_abramov) and [Joe Savona](https://twitter.com/en_JS) were interviewed by [Kent C. Dodds on his YouTube channel](https://www.youtube.com/watch?v=h7tur48JSaw), where they discussed concerns around React Server Components.
* [Dan Abramov](https://twitter.com/dan_abramov) and [Joe Savona](https://twitter.com/en_JS) were guests on the [JSParty podcast](https://jsparty.fm/267) and shared their thoughts about the future of React.

Thanks to [Andrew Clark](https://twitter.com/acdlite), [Dan Abramov](https://twitter.com/dan_abramov), [Dave McCabe](https://twitter.com/mcc_abe), [Luna Wei](https://twitter.com/lunaleaps), [Matt Carroll](https://twitter.com/mattcarrollcode), [Sean Keegan](https://twitter.com/DevRelSean), [Sebastian Silbermann](https://twitter.com/sebsilbermann), [Seth Webster](https://twitter.com/sethwebster), and [Sophie Alpert](https://twitter.com/sophiebits) for reviewing this post.

Thanks for reading, and see you in the next update!

[PreviousReact Canaries: Enabling Incremental Feature Rollout Outside Meta](/blog/2023/05/03/react-canaries)[NextIntroducing react.dev](/blog/2023/03/16/introducing-react-dev)

---



## React Canaries: Enabling Incremental Feature Rollout Outside Meta – React

[Read the full article](https://react.dev/blog/2023/05/03/react-canaries)

[Blog](/blog)# React Canaries: Enabling Incremental Feature Rollout Outside Meta

May 3, 2023 by [Dan Abramov](https://twitter.com/dan_abramov), [Sophie Alpert](https://twitter.com/sophiebits), [Rick Hanlon](https://twitter.com/rickhanlonii), [Sebastian Markbåge](https://twitter.com/sebmarkbage), and [Andrew Clark](https://twitter.com/acdlite)

---

We’d like to offer the React community an option to adopt individual new features as soon as their design is close to final, before they’re released in a stable version—similar to how Meta has long used bleeding\-edge versions of React internally. We are introducing a new officially supported [Canary release channel](/community/versioning-policy#canary-channel). It lets curated setups like frameworks decouple adoption of individual React features from the React release schedule.

---

## tl;dr

* We’re introducing an officially supported [Canary release channel](/community/versioning-policy#canary-channel) for React. Since it’s officially supported, if any regressions land, we’ll treat them with a similar urgency to bugs in stable releases.
* Canaries let you start using individual new React features before they land in the semver\-stable releases.
* Unlike the [Experimental](/community/versioning-policy#experimental-channel) channel, React Canaries only include features that we reasonably believe to be ready for adoption. We encourage frameworks to consider bundling pinned Canary React releases.
* We will announce breaking changes and new features on our blog as they land in Canary releases.
* **As always, React continues to follow semver for every Stable release.**

## How React features are usually developed

Typically, every React feature has gone through the same stages:

1. We develop an initial version and prefix it with `experimental_` or `unstable_`. The feature is only available in the `experimental` release channel. At this point, the feature is expected to change significantly.
2. We find a team at Meta willing to help us test this feature and provide feedback on it. This leads to a round of changes. As the feature becomes more stable, we work with more teams at Meta to try it out.
3. Eventually, we feel confident in the design. We remove the prefix from the API name, and make the feature available on the `main` branch by default, which most Meta products use. At this point, any team at Meta can use this feature.
4. As we build confidence in the direction, we also post an RFC for the new feature. At this point we know the design works for a broad set of cases, but we might make some last minute adjustments.
5. When we are close to cutting an open source release, we write documentation for the feature and finally release the feature in a stable React release.

This playbook works well for most features we’ve released so far. However, there can be a significant gap between when the feature is generally ready to use (step 3\) and when it is released in open source (step 5\).

**We’d like to offer the React community an option to follow the same approach as Meta, and adopt individual new features earlier (as they become available) without having to wait for the next release cycle of React.**

As always, all React features will eventually make it into a Stable release.

## Can we just do more minor releases?

Generally, we *do* use minor releases for introducing new features.

However, this isn’t always possible. Sometimes, new features are interconnected with *other* new features which have not yet been fully completed and that we’re still actively iterating on. We can’t release them separately because their implementations are related. We can’t version them separately because they affect the same packages (for example, `react` and `react-dom`). And we need to keep the ability to iterate on the pieces that aren’t ready without a flurry of major version releases, which semver would require us to do.

At Meta, we’ve solved this problem by building React from the `main` branch, and manually updating it to a specific pinned commit every week. This is also the approach that React Native releases have been following for the last several years. Every *stable* release of React Native is pinned to a specific commit from the `main` branch of the React repository. This lets React Native include important bugfixes and incrementally adopt new React features at the framework level without getting coupled to the global React release schedule.

We would like to make this workflow available to other frameworks and curated setups. For example, it lets a framework *on top of* React include a React\-related breaking change *before* this breaking change gets included into a stable React release. This is particularly useful because some breaking changes only affect framework integrations. This lets a framework release such a change in its own minor version without breaking semver.

Rolling releases with the Canaries channel will allow us to have a tighter feedback loop and ensure that new features get comprehensive testing in the community. This workflow is closer to how TC39, the JavaScript standards committee, [handles changes in numbered stages](https://tc39.es/process-document/). New React features may be available in frameworks built on React before they are in a React stable release, just as new JavaScript features ship in browsers before they are officially ratified as part of the specification.

## Why not use experimental releases instead?

Although you *can* technically use [Experimental releases](/community/versioning-policy#canary-channel), we recommend against using them in production because experimental APIs can undergo significant breaking changes on their way to stabilization (or can even be removed entirely). While Canaries can also contain mistakes (as with any release), going forward we plan to announce any significant breaking changes in Canaries on our blog. Canaries are the closest to the code Meta runs internally, so you can generally expect them to be relatively stable. However, you *do* need to keep the version pinned and manually scan the GitHub commit log when updating between the pinned commits.

**We expect that most people using React outside a curated setup (like a framework) will want to continue using the Stable releases.** However, if you’re building a framework, you might want to consider bundling a Canary version of React pinned to a particular commit, and update it at your own pace. The benefit of that is that it lets you ship individual completed React features and bugfixes earlier for your users and at your own release schedule, similar to how React Native has been doing it for the last few years. The downside is that you would take on additional responsibility to review which React commits are being pulled in and communicate to your users which React changes are included with your releases.

If you’re a framework author and want to try this approach, please get in touch with us.

## Announcing breaking changes and new features early

Canary releases represent our best guess of what will go into the next stable React release at any given time.

Traditionally, we’ve only announced breaking changes at the *end* of the release cycle (when doing a major release). Now that Canary releases are an officially supported way to consume React, we plan to shift towards announcing breaking changes and significant new features *as they land* in Canaries. For example, if we merge a breaking change that will go out in a Canary, we will write a post about it on the React blog, including codemods and migration instructions if necessary. Then, if you’re a framework author cutting a major release that updates the pinned React canary to include that change, you can link to our blog post from your release notes. Finally, when a stable major version of React is ready, we will link to those already published blog posts, which we hope will help our team make progress faster.

We plan to document APIs as they land in Canaries—even if these APIs are not yet available outside of them. APIs that are only available in Canaries will be marked with a special note on the corresponding pages. This will include APIs like [`use`](https://github.com/reactjs/rfcs/pull/229), and some others (like `cache` and `createServerContext`) which we’ll send RFCs for.

## Canaries must be pinned

If you decide to adopt the Canary workflow for your app or framework, make sure you always pin the *exact* version of the Canary you’re using. Since Canaries are pre\-releases, they may still include breaking changes.

## Example: React Server Components

As we [announced in March](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components), the React Server Components conventions have been finalized, and we do not expect significant breaking changes related to their user\-facing API contract. However, we can’t release support for React Server Components in a stable version of React yet because we are still working on several intertwined framework\-only features (such as [asset loading](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#asset-loading)) and expect more breaking changes there.

This means that React Server Components are ready to be adopted by frameworks. However, until the next major React release, the only way for a framework to adopt them is to ship a pinned Canary version of React. (To avoid bundling two copies of React, frameworks that wish to do this would need to enforce resolution of `react` and `react-dom` to the pinned Canary they ship with their framework, and explain that to their users. As an example, this is what Next.js App Router does.)

## Testing libraries against both Stable and Canary versions

We do not expect library authors to test every single Canary release since it would be prohibitively difficult. However, just as when we [originally introduced the different React pre\-release channels three years ago](https://legacy.reactjs.org/blog/2019/10/22/react-release-channels.html), we encourage libraries to run tests against *both* the latest Stable and latest Canary versions. If you see a change in behavior that wasn’t announced, please file a bug in the React repository so that we can help diagnose it. We expect that as this practice becomes widely adopted, it will reduce the amount of effort necessary to upgrade libraries to new major versions of React, since accidental regressions would be found as they land.

### Note

Strictly speaking, Canary is not a *new* release channel—it used to be called Next. However, we’ve decided to rename it to avoid confusion with Next.js. We’re announcing it as a *new* release channel to communicate the new expectations, such as Canaries being an officially supported way to use React.

## Stable releases work like before

We are not introducing any changes to stable React releases.

[PreviousReact Labs: What We've Been Working On – February 2024](/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024)[NextReact Labs: What We've Been Working On – March 2023](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023)

---



## React Labs: What We've Been Working On – February 2024 – React

[Read the full article](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024)

[Blog](/blog)# React Labs: What We've Been Working On – February 2024

February 15, 2024 by [Joseph Savona](https://twitter.com/en_JS), [Ricky Hanlon](https://twitter.com/rickhanlonii), [Andrew Clark](https://twitter.com/acdlite), [Matt Carroll](https://twitter.com/mattcarrollcode), and [Dan Abramov](https://twitter.com/dan_abramov).

---

In React Labs posts, we write about projects in active research and development. We’ve made significant progress since our [last update](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023), and we’d like to share our progress.

### Note

React Conf 2024 is scheduled for May 15–16 in Henderson, Nevada! If you’re interested in attending React Conf in person, you can [sign up for the ticket lottery](https://forms.reform.app/bLaLeE/react-conf-2024-ticket-lottery/1aRQLK) until February 28th.

For more info on tickets, free streaming, sponsoring, and more, see [the React Conf website](https://conf.react.dev).

---

## React Compiler

React Compiler is no longer a research project: the compiler now powers instagram.com in production, and we are working to ship the compiler across additional surfaces at Meta and to prepare the first open source release.

As discussed in our [previous post](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-optimizing-compiler), React can *sometimes* re\-render too much when state changes. Since the early days of React our solution for such cases has been manual memoization. In our current APIs, this means applying the [`useMemo`](/reference/react/useMemo), [`useCallback`](/reference/react/useCallback), and [`memo`](/reference/react/memo) APIs to manually tune how much React re\-renders on state changes. But manual memoization is a compromise. It clutters up our code, is easy to get wrong, and requires extra work to keep up to date.

Manual memoization is a reasonable compromise, but we weren’t satisfied. Our vision is for React to *automatically* re\-render just the right parts of the UI when state changes, *without compromising on React’s core mental model*. We believe that React’s approach — UI as a simple function of state, with standard JavaScript values and idioms — is a key part of why React has been approachable for so many developers. That’s why we’ve invested in building an optimizing compiler for React.

JavaScript is a notoriously challenging language to optimize, thanks to its loose rules and dynamic nature. React Compiler is able to compile code safely by modeling both the rules of JavaScript *and* the “rules of React”. For example, React components must be idempotent — returning the same value given the same inputs — and can’t mutate props or state values. These rules limit what developers can do and help to carve out a safe space for the compiler to optimize.

Of course, we understand that developers sometimes bend the rules a bit, and our goal is to make React Compiler work out of the box on as much code as possible. The compiler attempts to detect when code doesn’t strictly follow React’s rules and will either compile the code where safe or skip compilation if it isn’t safe. We’re testing against Meta’s large and varied codebase in order to help validate this approach.

For developers who are curious about making sure their code follows React’s rules, we recommend [enabling Strict Mode](/reference/react/StrictMode) and [configuring React’s ESLint plugin](/learn/editor-setup#linting). These tools can help to catch subtle bugs in your React code, improving the quality of your applications today, and future\-proofs your applications for upcoming features such as React Compiler. We are also working on consolidated documentation of the rules of React and updates to our ESLint plugin to help teams understand and apply these rules to create more robust apps.

To see the compiler in action, you can check out our [talk from last fall](https://www.youtube.com/watch?v=qOQClO3g8-Y). At the time of the talk, we had early experimental data from trying React Compiler on one page of instagram.com. Since then, we shipped the compiler to production across instagram.com. We’ve also expanded our team to accelerate the rollout to additional surfaces at Meta and to open source. We’re excited about the path ahead and will have more to share in the coming months.

## Actions

We [previously shared](/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components) that we were exploring solutions for sending data from the client to the server with Server Actions, so that you can execute database mutations and implement forms. During development of Server Actions, we extended these APIs to support data handling in client\-only applications as well.

We refer to this broader collection of features as simply “Actions”. Actions allow you to pass a function to DOM elements such as [``](/reference/react-dom/components/form):

\`\`\`
\ \ \Search\\
\`\`\`
The `action` function can operate synchronously or asynchronously. You can define them on the client side using standard JavaScript or on the server with the [`'use server'`](/reference/rsc/use-server) directive. When using an action, React will manage the life cycle of the data submission for you, providing hooks like [`useFormStatus`](/reference/react-dom/hooks/useFormStatus), and [`useActionState`](/reference/react/useActionState) to access the current state and response of the form action.

By default, Actions are submitted within a [transition](/reference/react/useTransition), keeping the current page interactive while the action is processing. Since Actions support async functions, we’ve also added the ability to use `async/await` in transitions. This allows you to show pending UI with the `isPending` state of a transition when an async request like `fetch` starts, and show the pending UI all the way through the update being applied.

Alongside Actions, we’re introducing a feature named [`useOptimistic`](/reference/react/useOptimistic) for managing optimistic state updates. With this hook, you can apply temporary updates that are automatically reverted once the final state commits. For Actions, this allows you to optimistically set the final state of the data on the client, assuming the submission is successful, and revert to the value for data received from the server. It works using regular `async`/`await`, so it works the same whether you’re using `fetch` on the client, or a Server Action from the server.

Library authors can implement custom `action={fn}` props in their own components with `useTransition`. Our intent is for libraries to adopt the Actions pattern when designing their component APIs, to provide a consistent experience for React developers. For example, if your library provides a `` component, consider also exposing a `` API, too.

While we initially focused on Server Actions for client\-server data transfer, our philosophy for React is to provide the same programming model across all platforms and environments. When possible, if we introduce a feature on the client, we aim to make it also work on the server, and vice versa. This philosophy allows us to create a single set of APIs that work no matter where your app runs, making it easier to upgrade to different environments later.

Actions are now available in the Canary channel and will ship in the next release of React.

## New Features in React Canary

We introduced [React Canaries](/blog/2023/05/03/react-canaries) as an option to adopt individual new stable features as soon as their design is close to final, before they’re released in a stable semver version.

Canaries are a change to the way we develop React. Previously, features would be researched and built privately inside of Meta, so users would only see the final polished product when released to Stable. With Canaries, we’re building in public with the help of the community to finalize features we share in the React Labs blog series. This means you hear about new features sooner, as they’re being finalized instead of after they’re complete.

React Server Components, Asset Loading, Document Metadata, and Actions have all landed in the React Canary, and we’ve added docs for these features on react.dev:

* **Directives**: [`"use client"`](/reference/rsc/use-client) and [`"use server"`](/reference/rsc/use-server) are bundler features designed for full\-stack React frameworks. They mark the “split points” between the two environments: `"use client"` instructs the bundler to generate a `` tag (like [Astro Islands](https://docs.astro.build/en/concepts/islands/#creating-an-island)), while `"use server"` tells the bundler to generate a POST endpoint (like [tRPC Mutations](https://trpc.io/docs/concepts)). Together, they let you write reusable components that compose client\-side interactivity with the related server\-side logic.
* **Document Metadata**: we added built\-in support for rendering [``](/reference/react-dom/components/title), [``](/reference/react-dom/components/meta), and metadata [``](/reference/react-dom/components/link) tags anywhere in your component tree. These work the same way in all environments, including fully client\-side code, SSR, and RSC. This provides built\-in support for features pioneered by libraries like [React Helmet](https://github.com/nfl/react-helmet).
* **Asset Loading**: we integrated Suspense with the loading lifecycle of resources such as stylesheets, fonts, and scripts so that React takes them into account to determine whether the content in elements like [``](/reference/react-dom/components/style), [``](/reference/react-dom/components/link), and [``](/reference/react-dom/components/script) are ready to be displayed. We’ve also added new [Resource Loading APIs](/reference/react-dom#resource-preloading-apis) like `preload` and `preinit` to provide greater control for when a resource should load and initialize.
* **Actions**: As shared above, we’ve added Actions to manage sending data from the client to the server. You can add `action` to elements like [``](/reference/react-dom/components/form), access the status with [`useFormStatus`](/reference/react-dom/hooks/useFormStatus), handle the result with [`useActionState`](/reference/react/useActionState), and optimistically update the UI with [`useOptimistic`](/reference/react/useOptimistic).

Since all of these features work together, it’s difficult to release them in the Stable channel individually. Releasing Actions without the complementary hooks for accessing form states would limit the practical usability of Actions. Introducing React Server Components without integrating Server Actions would complicate modifying data on the server.

Before we can release a set of features to the Stable channel, we need to ensure they work cohesively and developers have everything they need to use them in production. React Canaries allow us to develop these features individually, and release the stable APIs incrementally until the entire feature set is complete.

The current set of features in React Canary are complete and ready to release.

## The Next Major Version of React

After a couple of years of iteration, `react@canary` is now ready to ship to `react@latest`. The new features mentioned above are compatible with any environment your app runs in, providing everything needed for production use. Since Asset Loading and Document Metadata may be a breaking change for some apps, the next version of React will be a major version: **React 19**.

There’s still more to be done to prepare for release. In React 19, we’re also adding long\-requested improvements which require breaking changes like support for Web Components. Our focus now is to land these changes, prepare for release, finalize docs for new features, and publish announcements for what’s included.

We’ll share more information about everything React 19 includes, how to adopt the new client features, and how to build support for React Server Components in the coming months.

## Offscreen (renamed to Activity).

Since our last update, we’ve renamed a capability we’re researching from “Offscreen” to “Activity”. The name “Offscreen” implied that it only applied to parts of the app that were not visible, but while researching the feature we realized that it’s possible for parts of the app to be visible and inactive, such as content behind a modal. The new name more closely reflects the behavior of marking certain parts of the app “active” or “inactive”.

Activity is still under research and our remaining work is to finalize the primitives that are exposed to library developers. We’ve deprioritized this area while we focus on shipping features that are more complete.

---

In addition to this update, our team has presented at conferences and made appearances on podcasts to speak more on our work and answer questions.

* [Sathya Gunasekaran](/community/team#sathya-gunasekaran) spoke about the React Compiler at the [React India](https://www.youtube.com/watch?v=kjOacmVsLSE) conference
* [Dan Abramov](/community/team#dan-abramov) gave a talk at [RemixConf](https://www.youtube.com/watch?v=zMf_xeGPn6s) titled “React from Another Dimension” which explores an alternative history of how React Server Components and Actions could have been created
* [Dan Abramov](/community/team#dan-abramov) was interviewed on [the Changelog’s JS Party podcast](https://changelog.com/jsparty/311) about React Server Components
* [Matt Carroll](/community/team#matt-carroll) was interviewed on the [Front\-End Fire podcast](https://www.buzzsprout.com/2226499/14462424-interview-the-two-reacts-with-rachel-nabors-evan-bacon-and-matt-carroll) where he discussed [The Two Reacts](https://overreacted.io/the-two-reacts/)

Thanks [Lauren Tan](https://twitter.com/potetotes), [Sophie Alpert](https://twitter.com/sophiebits), [Jason Bonta](https://threads.net/someextent), [Eli White](https://twitter.com/Eli_White), and [Sathya Gunasekaran](https://twitter.com/_gsathya) for reviewing this post.

Thanks for reading, and [see you at React Conf](https://conf.react.dev/)!

[PreviousReact 19 RC Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide)[NextReact Canaries: Enabling Incremental Feature Rollout Outside Meta](/blog/2023/05/03/react-canaries)

---



## React v19 – React

[Read the full article](https://react.dev/blog/2024/04/25/react-19)

[Blog](/blog)# React v19

December 05, 2024 by [The React Team](/community/team)

---

### Note

### React 19 is now stable!

Additions since this post was originally shared with the React 19 RC in April:

* **Pre\-warming for suspended trees**: see [Improvements to Suspense](/blog/2024/04/25/react-19-upgrade-guide#improvements-to-suspense).
* **React DOM static APIs**: see [New React DOM Static APIs](#new-react-dom-static-apis).

*The date for this post has been updated to reflect the stable release date.*

React v19 is now available on npm!

In our [React 19 Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide), we shared step\-by\-step instructions for upgrading your app to React 19\. In this post, we’ll give an overview of the new features in React 19, and how you can adopt them.

* [What’s new in React 19](#whats-new-in-react-19)
* [Improvements in React 19](#improvements-in-react-19)
* [How to upgrade](#how-to-upgrade)

For a list of breaking changes, see the [Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide).

---

## What’s new in React 19

### Actions

A common use case in React apps is to perform a data mutation and then update state in response. For example, when a user submits a form to change their name, you will make an API request, and then handle the response. In the past, you would need to handle pending states, errors, optimistic updates, and sequential requests manually.

For example, you could handle the pending and error state in `useState`:

\`\`\`
// Before Actionsfunction UpdateName({}) { const \[name, setName] = useState(""); const \[error, setError] = useState(null); const \[isPending, setIsPending] = useState(false); const handleSubmit = async () =\> { setIsPending(true); const error = await updateName(name); setIsPending(false); if (error) { setError(error); return; } redirect("/path"); }; return ( \ \ setName(event.target.value)} /\> \ Update \ {error \&\& \{error}\} \ );}
\`\`\`
In React 19, we’re adding support for using async functions in transitions to handle pending states, errors, forms, and optimistic updates automatically.

For example, you can use `useTransition` to handle the pending state for you:

\`\`\`
// Using pending state from Actionsfunction UpdateName({}) { const \[name, setName] = useState(""); const \[error, setError] = useState(null); const \[isPending, startTransition] = useTransition(); const handleSubmit = () =\> { startTransition(async () =\> { const error = await updateName(name); if (error) { setError(error); return; } redirect("/path"); }) }; return ( \ \ setName(event.target.value)} /\> \ Update \ {error \&\& \{error}\} \ );}
\`\`\`
The async transition will immediately set the `isPending` state to true, make the async request(s), and switch `isPending` to false after any transitions. This allows you to keep the current UI responsive and interactive while the data is changing.

### Note

#### By convention, functions that use async transitions are called “Actions”.

Actions automatically manage submitting data for you:

* **Pending state**: Actions provide a pending state that starts at the beginning of a request and automatically resets when the final state update is committed.
* **Optimistic updates**: Actions support the new [`useOptimistic`](#new-hook-optimistic-updates) hook so you can show users instant feedback while the requests are submitting.
* **Error handling**: Actions provide error handling so you can display Error Boundaries when a request fails, and revert optimistic updates to their original value automatically.
* **Forms**: `` elements now support passing functions to the `action` and `formAction` props. Passing functions to the `action` props use Actions by default and reset the form automatically after submission.

Building on top of Actions, React 19 introduces [`useOptimistic`](#new-hook-optimistic-updates) to manage optimistic updates, and a new hook [`React.useActionState`](#new-hook-useactionstate) to handle common cases for Actions. In `react-dom` we’re adding [`` Actions](#form-actions) to manage forms automatically and [`useFormStatus`](#new-hook-useformstatus) to support the common cases for Actions in forms.

In React 19, the above example can be simplified to:

\`\`\`
// Using \ Actions and useActionStatefunction ChangeName({ name, setName }) { const \[error, submitAction, isPending] = useActionState( async (previousState, formData) =\> { const error = await updateName(formData.get("name")); if (error) { return error; } redirect("/path"); return null; }, null, ); return ( \ \ \Update\ {error \&\& \{error}\} \ );}
\`\`\`
In the next section, we’ll break down each of the new Action features in React 19\.

### New hook: `useActionState`

To make the common cases easier for Actions, we’ve added a new hook called `useActionState`:

\`\`\`
const \[error, submitAction, isPending] = useActionState( async (previousState, newName) =\> { const error = await updateName(newName); if (error) { // You can return any result of the action. // Here, we return only the error. return error; } // handle success return null; }, null,);
\`\`\`
`useActionState` accepts a function (the “Action”), and returns a wrapped Action to call. This works because Actions compose. When the wrapped Action is called, `useActionState` will return the last result of the Action as `data`, and the pending state of the Action as `pending`.

### Note

`React.useActionState` was previously called `ReactDOM.useFormState` in the Canary releases, but we’ve renamed it and deprecated `useFormState`.

See [\#28491](https://github.com/facebook/react/pull/28491) for more info.

For more information, see the docs for [`useActionState`](/reference/react/useActionState).

### React DOM: `` Actions

Actions are also integrated with React 19’s new `` features for `react-dom`. We’ve added support for passing functions as the `action` and `formAction` props of ``, ``, and `` elements to automatically submit forms with Actions:

\`\`\`
\
\`\`\`
When a `` Action succeeds, React will automatically reset the form for uncontrolled components. If you need to reset the `` manually, you can call the new `requestFormReset` React DOM API.

For more information, see the `react-dom` docs for [``](/reference/react-dom/components/form), [``](/reference/react-dom/components/input), and ``.

### React DOM: New hook: `useFormStatus`

In design systems, it’s common to write design components that need access to information about the `` they’re in, without drilling props down to the component. This can be done via Context, but to make the common case easier, we’ve added a new hook `useFormStatus`:

\`\`\`
import {useFormStatus} from 'react\-dom';function DesignButton() { const {pending} = useFormStatus(); return \}
\`\`\`
`useFormStatus` reads the status of the parent `` as if the form was a Context provider.

For more information, see the `react-dom` docs for [`useFormStatus`](/reference/react-dom/hooks/useFormStatus).

### New hook: `useOptimistic`

Another common UI pattern when performing a data mutation is to show the final state optimistically while the async request is underway. In React 19, we’re adding a new hook called `useOptimistic` to make this easier:

\`\`\`
function ChangeName({currentName, onUpdateName}) { const \[optimisticName, setOptimisticName] = useOptimistic(currentName); const submitAction = async formData =\> { const newName = formData.get("name"); setOptimisticName(newName); const updatedName = await updateName(newName); onUpdateName(updatedName); }; return ( \ \Your name is: {optimisticName}\ \ \Change Name:\ \ \ \ );}
\`\`\`
The `useOptimistic` hook will immediately render the `optimisticName` while the `updateName` request is in progress. When the update finishes or errors, React will automatically switch back to the `currentName` value.

For more information, see the docs for [`useOptimistic`](/reference/react/useOptimistic).

### New API: `use`

In React 19 we’re introducing a new API to read resources in render: `use`.

For example, you can read a promise with `use`, and React will Suspend until the promise resolves:

\`\`\`
import {use} from 'react';function Comments({commentsPromise}) { // \`use\` will suspend until the promise resolves. const comments = use(commentsPromise); return comments.map(comment =\> \{comment}\);}function Page({commentsPromise}) { // When \`use\` suspends in Comments, // this Suspense boundary will be shown. return ( \Loading...\}\> \ \ )}
\`\`\`
### Note

#### `use` does not support promises created in render.

If you try to pass a promise created in render to `use`, React will warn:

ConsoleA component was suspended by an uncached promise. Creating promises inside a Client Component or hook is not yet supported, except via a Suspense\-compatible library or framework.To fix, you need to pass a promise from a suspense powered library or framework that supports caching for promises. In the future we plan to ship features to make it easier to cache promises in render.

You can also read context with `use`, allowing you to read Context conditionally such as after early returns:

\`\`\`
import {use} from 'react';import ThemeContext from './ThemeContext'function Heading({children}) { if (children == null) { return null; } // This would not work with useContext // because of the early return. const theme = use(ThemeContext); return ( \ {children} \ );}
\`\`\`
The `use` API can only be called in render, similar to hooks. Unlike hooks, `use` can be called conditionally. In the future we plan to support more ways to consume resources in render with `use`.

For more information, see the docs for [`use`](/reference/react/use).

## New React DOM Static APIs

We’ve added two new APIs to `react-dom/static` for static site generation:

* [`prerender`](/reference/react-dom/static/prerender)
* [`prerenderToNodeStream`](/reference/react-dom/static/prerenderToNodeStream)

These new APIs improve on `renderToString` by waiting for data to load for static HTML generation. They are designed to work with streaming environments like Node.js Streams and Web Streams. For example, in a Web Stream environment, you can prerender a React tree to static HTML with `prerender`:

\`\`\`
import { prerender } from 'react\-dom/static';async function handler(request) { const {prelude} = await prerender(\, { bootstrapScripts: \['/main.js'] }); return new Response(prelude, { headers: { 'content\-type': 'text/html' }, });}
\`\`\`
Prerender APIs will wait for all data to load before returning the static HTML stream. Streams can be converted to strings, or sent with a streaming response. They do not support streaming content as it loads, which is supported by the existing [React DOM server rendering APIs](/reference/react-dom/server).

For more information, see [React DOM Static APIs](/reference/react-dom/static).

## React Server Components

### Server Components

Server Components are a new option that allows rendering components ahead of time, before bundling, in an environment separate from your client application or SSR server. This separate environment is the “server” in React Server Components. Server Components can run once at build time on your CI server, or they can be run for each request using a web server.

React 19 includes all of the React Server Components features included from the Canary channel. This means libraries that ship with Server Components can now target React 19 as a peer dependency with a `react-server` [export condition](https://github.com/reactjs/rfcs/blob/main/text/0227-server-module-conventions.md#react-server-conditional-exports) for use in frameworks that support the [Full\-stack React Architecture](/learn/start-a-new-react-project#which-features-make-up-the-react-teams-full-stack-architecture-vision).

### Note

#### How do I build support for Server Components?

While React Server Components in React 19 are stable and will not break between minor versions, the underlying APIs used to implement a React Server Components bundler or framework do not follow semver and may break between minors in React 19\.x.

To support React Server Components as a bundler or framework, we recommend pinning to a specific React version, or using the Canary release. We will continue working with bundlers and frameworks to stabilize the APIs used to implement React Server Components in the future.

For more, see the docs for [React Server Components](/reference/rsc/server-components).

### Server Actions

Server Actions allow Client Components to call async functions executed on the server.

When a Server Action is defined with the `"use server"` directive, your framework will automatically create a reference to the server function, and pass that reference to the Client Component. When that function is called on the client, React will send a request to the server to execute the function, and return the result.

### Note

#### There is no directive for Server Components.

A common misunderstanding is that Server Components are denoted by `"use server"`, but there is no directive for Server Components. The `"use server"` directive is used for Server Actions.

For more info, see the docs for [Directives](/reference/rsc/directives).

Server Actions can be created in Server Components and passed as props to Client Components, or they can be imported and used in Client Components.

For more, see the docs for [React Server Actions](/reference/rsc/server-actions).

## Improvements in React 19

### `ref` as a prop

Starting in React 19, you can now access `ref` as a prop for function components:

\`\`\`
function MyInput({placeholder, ref}) { return \}//...\
\`\`\`
New function components will no longer need `forwardRef`, and we will be publishing a codemod to automatically update your components to use the new `ref` prop. In future versions we will deprecate and remove `forwardRef`.

### Note

`refs` passed to classes are not passed as props since they reference the component instance.

### Diffs for hydration errors

We also improved error reporting for hydration errors in `react-dom`. For example, instead of logging multiple errors in DEV without any information about the mismatch:

ConsoleWarning: Text content did not match. Server: “Server” Client: “Client”
 at span
 at AppWarning: An error occurred during hydration. The server HTML was replaced with client content in \.Warning: Text content did not match. Server: “Server” Client: “Client”
 at span
 at AppWarning: An error occurred during hydration. The server HTML was replaced with client content in \.Uncaught Error: Text content does not match server\-rendered HTML.
 at checkForUnmatchedText
 …
We now log a single message with a diff of the mismatch:

ConsoleUncaught Error: Hydration failed because the server rendered HTML didn’t match the client. As a result this tree will be regenerated on the client. This can happen if an SSR\-ed Client Component used:

\- A server/client branch `if (typeof window !== 'undefined')`.
\- Variable input such as `Date.now()` or `Math.random()` which changes each time it’s called.
\- Date formatting in a user’s locale which doesn’t match the server.
\- External changing data without sending a snapshot of it along with the HTML.
\- Invalid HTML tag nesting.

It can also happen if the client has a browser extension installed which messes with the HTML before React loaded.

[https://react.dev/link/hydration\-mismatch](https://react.dev/link/hydration-mismatch) 

 \
 \
\+ Client
\- Server

 at throwOnHydrationMismatch
 …
### `` as a provider

In React 19, you can render `` as a provider instead of ``:

\`\`\`
const ThemeContext = createContext('');function App({children}) { return ( \ {children} \ ); }
\`\`\`
New Context providers can use `` and we will be publishing a codemod to convert existing providers. In future versions we will deprecate ``.

### Cleanup functions for refs

We now support returning a cleanup function from `ref` callbacks:

\`\`\`
\ { // ref created // NEW: return a cleanup function to reset // the ref when element is removed from DOM. return () =\> { // ref cleanup }; }}/\>
\`\`\`
When the component unmounts, React will call the cleanup function returned from the `ref` callback. This works for DOM refs, refs to class components, and `useImperativeHandle`.

### Note

Previously, React would call `ref` functions with `null` when unmounting the component. If your `ref` returns a cleanup function, React will now skip this step.

In future versions, we will deprecate calling refs with `null` when unmounting components.

Due to the introduction of ref cleanup functions, returning anything else from a `ref` callback will now be rejected by TypeScript. The fix is usually to stop using implicit returns, for example:

\`\`\`
\- \ (instance = current)} /\>\+ \ {instance = current}} /\>
\`\`\`
The original code returned the instance of the `HTMLDivElement` and TypeScript wouldn’t know if this was *supposed* to be a cleanup function or if you didn’t want to return a cleanup function.

You can codemod this pattern with [`no-implicit-ref-callback-return`](https://github.com/eps1lon/types-react-codemod/#no-implicit-ref-callback-return).

### `useDeferredValue` initial value

We’ve added an `initialValue` option to `useDeferredValue`:

\`\`\`
function Search({deferredValue}) { // On initial render the value is ''. // Then a re\-render is scheduled with the deferredValue. const value = useDeferredValue(deferredValue, ''); return ( \ );}
\`\`\`
When initialValue is provided, `useDeferredValue` will return it as `value` for the initial render of the component, and schedules a re\-render in the background with the deferredValue returned.

For more, see [`useDeferredValue`](/reference/react/useDeferredValue).

### Support for Document Metadata

In HTML, document metadata tags like ``, ``, and `` are reserved for placement in the `` section of the document. In React, the component that decides what metadata is appropriate for the app may be very far from the place where you render the `` or React does not render the `` at all. In the past, these elements would need to be inserted manually in an effect, or by libraries like [`react-helmet`](https://github.com/nfl/react-helmet), and required careful handling when server rendering a React application.

In React 19, we’re adding support for rendering document metadata tags in components natively:

\`\`\`
function BlogPost({post}) { return ( \ \{post.title}\ \{post.title}\ \ \ \ \ Eee equals em\-see\-squared... \ \ );}
\`\`\`
When React renders this component, it will see the `` `` and `` tags, and automatically hoist them to the `` section of document. By supporting these metadata tags natively, we’re able to ensure they work with client\-only apps, streaming SSR, and Server Components.

### Note

#### You may still want a Metadata library

For simple use cases, rendering Document Metadata as tags may be suitable, but libraries can offer more powerful features like overriding generic metadata with specific metadata based on the current route. These features make it easier for frameworks and libraries like [`react-helmet`](https://github.com/nfl/react-helmet) to support metadata tags, rather than replace them.

For more info, see the docs for [``](/reference/react-dom/components/title), [``](/reference/react-dom/components/link), and [``](/reference/react-dom/components/meta).

### Support for stylesheets

Stylesheets, both externally linked (``) and inline (`...`), require careful positioning in the DOM due to style precedence rules. Building a stylesheet capability that allows for composability within components is hard, so users often end up either loading all of their styles far from the components that may depend on them, or they use a style library which encapsulates this complexity.

In React 19, we’re addressing this complexity and providing even deeper integration into Concurrent Rendering on the Client and Streaming Rendering on the Server with built in support for stylesheets. If you tell React the `precedence` of your stylesheet it will manage the insertion order of the stylesheet in the DOM and ensure that the stylesheet (if external) is loaded before revealing content that depends on those style rules.

\`\`\`
function ComponentOne() { return ( \ \ \ \ {...} \ \ )}function ComponentTwo() { return ( \ \{...}\ \ \ )}
\`\`\`
During Server Side Rendering React will include the stylesheet in the ``, which ensures that the browser will not paint until it has loaded. If the stylesheet is discovered late after we’ve already started streaming, React will ensure that the stylesheet is inserted into the `` on the client before revealing the content of a Suspense boundary that depends on that stylesheet.

During Client Side Rendering React will wait for newly rendered stylesheets to load before committing the render. If you render this component from multiple places within your application React will only include the stylesheet once in the document:

\`\`\`
function App() { return \ \ ... \ // won't lead to a duplicate stylesheet link in the DOM \}
\`\`\`
For users accustomed to loading stylesheets manually this is an opportunity to locate those stylesheets alongside the components that depend on them allowing for better local reasoning and an easier time ensuring you only load the stylesheets that you actually depend on.

Style libraries and style integrations with bundlers can also adopt this new capability so even if you don’t directly render your own stylesheets, you can still benefit as your tools are upgraded to use this feature.

For more details, read the docs for [``](/reference/react-dom/components/link) and [``](/reference/react-dom/components/style).

### Support for async scripts

In HTML normal scripts (``) and deferred scripts (``) load in document order which makes rendering these kinds of scripts deep within your component tree challenging. Async scripts (``) however will load in arbitrary order.

In React 19 we’ve included better support for async scripts by allowing you to render them anywhere in your component tree, inside the components that actually depend on the script, without having to manage relocating and deduplicating script instances.

\`\`\`
function MyComponent() { return ( \ \ Hello World \ )}function App() { \ \ \ ... \ // won't lead to duplicate script in the DOM \ \}
\`\`\`
In all rendering environments, async scripts will be deduplicated so that React will only load and execute the script once even if it is rendered by multiple different components.

In Server Side Rendering, async scripts will be included in the `` and prioritized behind more critical resources that block paint such as stylesheets, fonts, and image preloads.

For more details, read the docs for [``](/reference/react-dom/components/script).

### Support for preloading resources

During initial document load and on client side updates, telling the Browser about resources that it will likely need to load as early as possible can have a dramatic effect on page performance.

React 19 includes a number of new APIs for loading and preloading Browser resources to make it as easy as possible to build great experiences that aren’t held back by inefficient resource loading.

\`\`\`
import { prefetchDNS, preconnect, preload, preinit } from 'react\-dom'function MyComponent() { preinit('https://.../path/to/some/script.js', {as: 'script' }) // loads and executes this script eagerly preload('https://.../path/to/font.woff', { as: 'font' }) // preloads this font preload('https://.../path/to/stylesheet.css', { as: 'style' }) // preloads this stylesheet prefetchDNS('https://...') // when you may not actually request anything from this host preconnect('https://...') // when you will request something but aren't sure what}
\`\`\`
\`\`\`
\\ \ \ \ \ \ \ \\ \ \ ... \\
\`\`\`
These APIs can be used to optimize initial page loads by moving discovery of additional resources like fonts out of stylesheet loading. They can also make client updates faster by prefetching a list of resources used by an anticipated navigation and then eagerly preloading those resources on click or even on hover.

For more details see [Resource Preloading APIs](/reference/react-dom#resource-preloading-apis).

### Compatibility with third\-party scripts and extensions

We’ve improved hydration to account for third\-party scripts and browser extensions.

When hydrating, if an element that renders on the client doesn’t match the element found in the HTML from the server, React will force a client re\-render to fix up the content. Previously, if an element was inserted by third\-party scripts or browser extensions, it would trigger a mismatch error and client render.

In React 19, unexpected tags in the `` and `` will be skipped over, avoiding the mismatch errors. If React needs to re\-render the entire document due to an unrelated hydration mismatch, it will leave in place stylesheets inserted by third\-party scripts and browser extensions.

### Better error reporting

We improved error handling in React 19 to remove duplication and provide options for handling caught and uncaught errors. For example, when there’s an error in render caught by an Error Boundary, previously React would throw the error twice (once for the original error, then again after failing to automatically recover), and then call `console.error` with info about where the error occurred.

This resulted in three errors for every caught error:

ConsoleUncaught Error: hit
 at Throws
 at renderWithHooks
 …Uncaught Error: hit \<\-\- Duplicate
 at Throws
 at renderWithHooks
 …The above error occurred in the Throws component:
 at Throws
 at ErrorBoundary
 at App

React will try to recreate this component tree from scratch using the error boundary you provided, ErrorBoundary.
In React 19, we log a single error with all the error information included:

ConsoleError: hit
 at Throws
 at renderWithHooks
 …

The above error occurred in the Throws component:
 at Throws
 at ErrorBoundary
 at App

React will try to recreate this component tree from scratch using the error boundary you provided, ErrorBoundary.
 at ErrorBoundary
 at App
Additionally, we’ve added two new root options to complement `onRecoverableError`:

* `onCaughtError`: called when React catches an error in an Error Boundary.
* `onUncaughtError`: called when an error is thrown and not caught by an Error Boundary.
* `onRecoverableError`: called when an error is thrown and automatically recovered.

For more info and examples, see the docs for [`createRoot`](/reference/react-dom/client/createRoot) and [`hydrateRoot`](/reference/react-dom/client/hydrateRoot).

### Support for Custom Elements

React 19 adds full support for custom elements and passes all tests on [Custom Elements Everywhere](https://custom-elements-everywhere.com/).

In past versions, using Custom Elements in React has been difficult because React treated unrecognized props as attributes rather than properties. In React 19, we’ve added support for properties that works on the client and during SSR with the following strategy:

* **Server Side Rendering**: props passed to a custom element will render as attributes if their type is a primitive value like `string`, `number`, or the value is `true`. Props with non\-primitive types like `object`, `symbol`, `function`, or value `false` will be omitted.
* **Client Side Rendering**: props that match a property on the Custom Element instance will be assigned as properties, otherwise they will be assigned as attributes.

Thanks to [Joey Arhar](https://github.com/josepharhar) for driving the design and implementation of Custom Element support in React.

#### How to upgrade

See the [React 19 Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide) for step\-by\-step instructions and a full list of breaking and notable changes.

*Note: this post was originally published 04/25/2024 and has been updated to 12/05/2024 with the stable release.*

[PreviousBlog](/blog)[NextReact Compiler Beta Release and Roadmap](/blog/2024/10/21/react-compiler-beta-release)

---



## React 19 Upgrade Guide – React

[Read the full article](https://react.dev/blog/2024/04/25/react-19-upgrade-guide)

[Blog](/blog)# React 19 Upgrade Guide

April 25, 2024 by [Ricky Hanlon](https://twitter.com/rickhanlonii)

---

The improvements added to React 19 require some breaking changes, but we’ve worked to make the upgrade as smooth as possible, and we don’t expect the changes to impact most apps.

### Note

#### React 18\.3 has also been published

To help make the upgrade to React 19 easier, we’ve published a `react@18.3` release that is identical to 18\.2 but adds warnings for deprecated APIs and other changes that are needed for React 19\.

We recommend upgrading to React 18\.3 first to help identify any issues before upgrading to React 19\.

For a list of changes in 18\.3 see the [Release Notes](https://github.com/facebook/react/blob/main/CHANGELOG.md).

In this post, we will guide you through the steps for upgrading to React 19:

* [Installing](#installing)
* [Codemods](#codemods)
* [Breaking changes](#breaking-changes)
* [New deprecations](#new-deprecations)
* [Notable changes](#notable-changes)
* [TypeScript changes](#typescript-changes)
* [Changelog](#changelog)

If you’d like to help us test React 19, follow the steps in this upgrade guide and [report any issues](https://github.com/facebook/react/issues/new?assignees=&labels=React+19&projects=&template=19.md&title=%5BReact+19%5D) you encounter. For a list of new features added to React 19, see the [React 19 release post](/blog/2024/12/05/react-19).

---

## Installing

### Note

#### New JSX Transform is now required

We introduced a [new JSX transform](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) in 2020 to improve bundle size and use JSX without importing React. In React 19, we’re adding additional improvements like using ref as a prop and JSX speed improvements that require the new transform.

If the new transform is not enabled, you will see this warning:

ConsoleYour app (or one of its dependencies) is using an outdated JSX transform. Update to the modern JSX transform for faster performance: [https://react.dev/link/new\-jsx\-transform](https://react.dev/link/new-jsx-transform)We expect most apps will not be affected since the transform is enabled in most environments already. For manual instructions on how to upgrade, please see the [announcement post](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html).

To install the latest version of React and React DOM:

\`\`\`
npm install \-\-save\-exact react@^19\.0\.0 react\-dom@^19\.0\.0
\`\`\`
Or, if you’re using Yarn:

\`\`\`
yarn add \-\-exact react@^19\.0\.0 react\-dom@^19\.0\.0
\`\`\`
If you’re using TypeScript, you also need to update the types.

\`\`\`
npm install \-\-save\-exact @types/react@^19\.0\.0 @types/react\-dom@^19\.0\.0
\`\`\`
Or, if you’re using Yarn:

\`\`\`
yarn add \-\-exact @types/react@^19\.0\.0 @types/react\-dom@^19\.0\.0
\`\`\`
We’re also including a codemod for the most common replacements. See [TypeScript changes](#typescript-changes) below.

## Codemods

To help with the upgrade, we’ve worked with the team at [codemod.com](https://codemod.com) to publish codemods that will automatically update your code to many of the new APIs and patterns in React 19\.

All codemods are available in the [`react-codemod` repo](https://github.com/reactjs/react-codemod) and the Codemod team have joined in helping maintain the codemods. To run these codemods, we recommend using the `codemod` command instead of the `react-codemod` because it runs faster, handles more complex code migrations, and provides better support for TypeScript.

### Note

#### Run all React 19 codemods

Run all codemods listed in this guide with the React 19 `codemod` recipe:

\`\`\`
npx codemod@latest react/19/migration\-recipe
\`\`\`This will run the following codemods from `react-codemod`:

* [`replace-reactdom-render`](https://github.com/reactjs/react-codemod?tab=readme-ov-file#replace-reactdom-render)
* [`replace-string-ref`](https://github.com/reactjs/react-codemod?tab=readme-ov-file#replace-string-ref)
* [`replace-act-import`](https://github.com/reactjs/react-codemod?tab=readme-ov-file#replace-act-import)
* [`replace-use-form-state`](https://github.com/reactjs/react-codemod?tab=readme-ov-file#replace-use-form-state)
* [`prop-types-typescript`](https://codemod.com/registry/react-prop-types-typescript)

This does not include the TypeScript changes. See [TypeScript changes](#typescript-changes) below.

Changes that include a codemod include the command below.

For a list of all available codemods, see the [`react-codemod` repo](https://github.com/reactjs/react-codemod).

## Breaking changes

### Errors in render are not re\-thrown

In previous versions of React, errors thrown during render were caught and rethrown. In DEV, we would also log to `console.error`, resulting in duplicate error logs.

In React 19, we’ve [improved how errors are handled](/blog/2024/04/25/react-19#error-handling) to reduce duplication by not re\-throwing:

* **Uncaught Errors**: Errors that are not caught by an Error Boundary are reported to `window.reportError`.
* **Caught Errors**: Errors that are caught by an Error Boundary are reported to `console.error`.

This change should not impact most apps, but if your production error reporting relies on errors being re\-thrown, you may need to update your error handling. To support this, we’ve added new methods to `createRoot` and `hydrateRoot` for custom error handling:

\`\`\`
const root = createRoot(container, { onUncaughtError: (error, errorInfo) =\> { // ... log error report }, onCaughtError: (error, errorInfo) =\> { // ... log error report }});
\`\`\`
For more info, see the docs for [`createRoot`](https://react.dev/reference/react-dom/client/createRoot) and [`hydrateRoot`](https://react.dev/reference/react-dom/client/hydrateRoot).

### Removed deprecated React APIs

#### Removed: `propTypes` and `defaultProps` for functions

`PropTypes` were deprecated in [April 2017 (v15\.5\.0\)](https://legacy.reactjs.org/blog/2017/04/07/react-v15.5.0.html#new-deprecation-warnings).

In React 19, we’re removing the `propType` checks from the React package, and using them will be silently ignored. If you’re using `propTypes`, we recommend migrating to TypeScript or another type\-checking solution.

We’re also removing `defaultProps` from function components in place of ES6 default parameters. Class components will continue to support `defaultProps` since there is no ES6 alternative.

\`\`\`
// Beforeimport PropTypes from 'prop\-types';function Heading({text}) { return \{text}\;}Heading.propTypes = { text: PropTypes.string,};Heading.defaultProps = { text: 'Hello, world!',};
\`\`\`
\`\`\`
// Afterinterface Props { text?: string;}function Heading({text = 'Hello, world!'}: Props) { return \{text}\;}
\`\`\`
### Note

Codemod `propTypes` to TypeScript with:

\`\`\`
npx codemod@latest react/prop\-types\-typescript
\`\`\`
#### Removed: Legacy Context using `contextTypes` and `getChildContext`

Legacy Context was deprecated in [October 2018 (v16\.6\.0\)](https://legacy.reactjs.org/blog/2018/10/23/react-v-16-6.html).

Legacy Context was only available in class components using the APIs `contextTypes` and `getChildContext`, and was replaced with `contextType` due to subtle bugs that were easy to miss. In React 19, we’re removing Legacy Context to make React slightly smaller and faster.

If you’re still using Legacy Context in class components, you’ll need to migrate to the new `contextType` API:

\`\`\`
// Beforeimport PropTypes from 'prop\-types';class Parent extends React.Component { static childContextTypes = { foo: PropTypes.string.isRequired, }; getChildContext() { return { foo: 'bar' }; } render() { return \; }}class Child extends React.Component { static contextTypes = { foo: PropTypes.string.isRequired, }; render() { return \{this.context.foo}\; }}
\`\`\`
\`\`\`
// Afterconst FooContext = React.createContext();class Parent extends React.Component { render() { return ( \ \ \ ); }}class Child extends React.Component { static contextType = FooContext; render() { return \{this.context}\; }}
\`\`\`
#### Removed: string refs

String refs were deprecated in [March, 2018 (v16\.3\.0\)](https://legacy.reactjs.org/blog/2018/03/27/update-on-async-rendering.html).

Class components supported string refs before being replaced by ref callbacks due to [multiple downsides](https://github.com/facebook/react/issues/1373). In React 19, we’re removing string refs to make React simpler and easier to understand.

If you’re still using string refs in class components, you’ll need to migrate to ref callbacks:

\`\`\`
// Beforeclass MyComponent extends React.Component { componentDidMount() { this.refs.input.focus(); } render() { return \; }}
\`\`\`
\`\`\`
// Afterclass MyComponent extends React.Component { componentDidMount() { this.input.focus(); } render() { return \ this.input = input} /\>; }}
\`\`\`
### Note

Codemod string refs with `ref` callbacks:

\`\`\`
npx codemod@latest react/19/replace\-string\-ref
\`\`\`
#### Removed: Module pattern factories

Module pattern factories were deprecated in [August 2019 (v16\.9\.0\)](https://legacy.reactjs.org/blog/2019/08/08/react-v16.9.0.html#deprecating-module-pattern-factories).

This pattern was rarely used and supporting it causes React to be slightly larger and slower than necessary. In React 19, we’re removing support for module pattern factories, and you’ll need to migrate to regular functions:

\`\`\`
// Beforefunction FactoryComponent() { return { render() { return \; } }}
\`\`\`
\`\`\`
// Afterfunction FactoryComponent() { return \;}
\`\`\`
#### Removed: `React.createFactory`

`createFactory` was deprecated in [February 2020 (v16\.13\.0\)](https://legacy.reactjs.org/blog/2020/02/26/react-v16.13.0.html#deprecating-createfactory).

Using `createFactory` was common before broad support for JSX, but it’s rarely used today and can be replaced with JSX. In React 19, we’re removing `createFactory` and you’ll need to migrate to JSX:

\`\`\`
// Beforeimport { createFactory } from 'react';const button = createFactory('button');
\`\`\`
\`\`\`
// Afterconst button = \;
\`\`\`
#### Removed: `react-test-renderer/shallow`

In React 18, we updated `react-test-renderer/shallow` to re\-export [react\-shallow\-renderer](https://github.com/enzymejs/react-shallow-renderer). In React 19, we’re removing `react-test-render/shallow` to prefer installing the package directly:

\`\`\`
npm install react\-shallow\-renderer \-\-save\-dev
\`\`\`
\`\`\`
\- import ShallowRenderer from 'react\-test\-renderer/shallow';\+ import ShallowRenderer from 'react\-shallow\-renderer';
\`\`\`
### Note

##### Please reconsider shallow rendering

Shallow rendering depends on React internals and can block you from future upgrades. We recommend migrating your tests to [@testing\-library/react](https://testing-library.com/docs/react-testing-library/intro/) or [@testing\-library/react\-native](https://testing-library.com/docs/react-native-testing-library/intro).

### Removed deprecated React DOM APIs

#### Removed: `react-dom/test-utils`

We’ve moved `act` from `react-dom/test-utils` to the `react` package:

Console`ReactDOMTestUtils.act` is deprecated in favor of `React.act`. Import `act` from `react` instead of `react-dom/test-utils`. See [https://react.dev/warnings/react\-dom\-test\-utils](https://react.dev/warnings/react-dom-test-utils) for more info.
To fix this warning, you can import `act` from `react`:

\`\`\`
\- import {act} from 'react\-dom/test\-utils'\+ import {act} from 'react';
\`\`\`
All other `test-utils` functions have been removed. These utilities were uncommon, and made it too easy to depend on low level implementation details of your components and React. In React 19, these functions will error when called and their exports will be removed in a future version.

See the [warning page](https://react.dev/warnings/react-dom-test-utils) for alternatives.

### Note

Codemod `ReactDOMTestUtils.act` to `React.act`:

\`\`\`
npx codemod@latest react/19/replace\-act\-import
\`\`\`
#### Removed: `ReactDOM.render`

`ReactDOM.render` was deprecated in [March 2022 (v18\.0\.0\)](https://react.dev/blog/2022/03/08/react-18-upgrade-guide). In React 19, we’re removing `ReactDOM.render` and you’ll need to migrate to using [`ReactDOM.createRoot`](https://react.dev/reference/react-dom/client/createRoot):

\`\`\`
// Beforeimport {render} from 'react\-dom';render(\, document.getElementById('root'));// Afterimport {createRoot} from 'react\-dom/client';const root = createRoot(document.getElementById('root'));root.render(\);
\`\`\`
### Note

Codemod `ReactDOM.render` to `ReactDOMClient.createRoot`:

\`\`\`
npx codemod@latest react/19/replace\-reactdom\-render
\`\`\`
#### Removed: `ReactDOM.hydrate`

`ReactDOM.hydrate` was deprecated in [March 2022 (v18\.0\.0\)](https://react.dev/blog/2022/03/08/react-18-upgrade-guide). In React 19, we’re removing `ReactDOM.hydrate` you’ll need to migrate to using [`ReactDOM.hydrateRoot`](https://react.dev/reference/react-dom/client/hydrateRoot),

\`\`\`
// Beforeimport {hydrate} from 'react\-dom';hydrate(\, document.getElementById('root'));// Afterimport {hydrateRoot} from 'react\-dom/client';hydrateRoot(document.getElementById('root'), \);
\`\`\`
### Note

Codemod `ReactDOM.hydrate` to `ReactDOMClient.hydrateRoot`:

\`\`\`
npx codemod@latest react/19/replace\-reactdom\-render
\`\`\`
#### Removed: `unmountComponentAtNode`

`ReactDOM.unmountComponentAtNode` was deprecated in [March 2022 (v18\.0\.0\)](https://react.dev/blog/2022/03/08/react-18-upgrade-guide). In React 19, you’ll need to migrate to using `root.unmount()`.

\`\`\`
// BeforeunmountComponentAtNode(document.getElementById('root'));// Afterroot.unmount();
\`\`\`
For more see `root.unmount()` for [`createRoot`](https://react.dev/reference/react-dom/client/createRoot#root-unmount) and [`hydrateRoot`](https://react.dev/reference/react-dom/client/hydrateRoot#root-unmount).

### Note

Codemod `unmountComponentAtNode` to `root.unmount`:

\`\`\`
npx codemod@latest react/19/replace\-reactdom\-render
\`\`\`
#### Removed: `ReactDOM.findDOMNode`

`ReactDOM.findDOMNode` was [deprecated in October 2018 (v16\.6\.0\)](https://legacy.reactjs.org/blog/2018/10/23/react-v-16-6.html#deprecations-in-strictmode).

We’re removing `findDOMNode` because it was a legacy escape hatch that was slow to execute, fragile to refactoring, only returned the first child, and broke abstraction levels (see more [here](https://legacy.reactjs.org/docs/strict-mode.html#warning-about-deprecated-finddomnode-usage)). You can replace `ReactDOM.findDOMNode` with [DOM refs](/learn/manipulating-the-dom-with-refs):

\`\`\`
// Beforeimport {findDOMNode} from 'react\-dom';function AutoselectingInput() { useEffect(() =\> { const input = findDOMNode(this); input.select() }, \[]); return \;}
\`\`\`
\`\`\`
// Afterfunction AutoselectingInput() { const ref = useRef(null); useEffect(() =\> { ref.current.select(); }, \[]); return \}
\`\`\`
## New deprecations

### Deprecated: `element.ref`

React 19 supports [`ref` as a prop](/blog/2024/04/25/react-19#ref-as-a-prop), so we’re deprecating the `element.ref` in place of `element.props.ref`.

Accessing `element.ref` will warn:

ConsoleAccessing element.ref is no longer supported. ref is now a regular prop. It will be removed from the JSX Element type in a future release.
### Deprecated: `react-test-renderer`

We are deprecating `react-test-renderer` because it implements its own renderer environment that doesn’t match the environment users use, promotes testing implementation details, and relies on introspection of React’s internals.

The test renderer was created before there were more viable testing strategies available like [React Testing Library](https://testing-library.com), and we now recommend using a modern testing library instead.

In React 19, `react-test-renderer` logs a deprecation warning, and has switched to concurrent rendering. We recommend migrating your tests to [@testing\-library/react](https://testing-library.com/docs/react-testing-library/intro/) or [@testing\-library/react\-native](https://testing-library.com/docs/react-native-testing-library/intro) for a modern and well supported testing experience.

## Notable changes

### StrictMode changes

React 19 includes several fixes and improvements to Strict Mode.

When double rendering in Strict Mode in development, `useMemo` and `useCallback` will reuse the memoized results from the first render during the second render. Components that are already Strict Mode compatible should not notice a difference in behavior.

As with all Strict Mode behaviors, these features are designed to proactively surface bugs in your components during development so you can fix them before they are shipped to production. For example, during development, Strict Mode will double\-invoke ref callback functions on initial mount, to simulate what happens when a mounted component is replaced by a Suspense fallback.

### Improvements to Suspense

In React 19, when a component suspends, React will immediately commit the fallback of the nearest Suspense boundary without waiting for the entire sibling tree to render. After the fallback commits, React schedules another render for the suspended siblings to “pre\-warm” lazy requests in the rest of the tree:



Previously, when a component suspended, the suspended siblings were rendered and then the fallback was committed.



In React 19, when a component suspends, the fallback is committed and then the suspended siblings are rendered.

This change means Suspense fallbacks display faster, while still warming lazy requests in the suspended tree.

### UMD builds removed

UMD was widely used in the past as a convenient way to load React without a build step. Now, there are modern alternatives for loading modules as scripts in HTML documents. Starting with React 19, React will no longer produce UMD builds to reduce the complexity of its testing and release process.

To load React 19 with a script tag, we recommend using an ESM\-based CDN such as [esm.sh](https://esm.sh/).

\`\`\`
\ import React from "https://esm.sh/react@19/?dev" import ReactDOMClient from "https://esm.sh/react\-dom@19/client?dev" ...\
\`\`\`
### Libraries depending on React internals may block upgrades

This release includes changes to React internals that may impact libraries that ignore our pleas to not use internals like `SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED`. These changes are necessary to land improvements in React 19, and will not break libraries that follow our guidelines.

Based on our [Versioning Policy](https://react.dev/community/versioning-policy#what-counts-as-a-breaking-change), these updates are not listed as breaking changes, and we are not including docs for how to upgrade them. The recommendation is to remove any code that depends on internals.

To reflect the impact of using internals, we have renamed the `SECRET_INTERNALS` suffix to:

`_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE`

In the future we will more aggressively block accessing internals from React to discourage usage and ensure users are not blocked from upgrading.

## TypeScript changes

### Removed deprecated TypeScript types

We’ve cleaned up the TypeScript types based on the removed APIs in React 19\. Some of the removed have types been moved to more relevant packages, and others are no longer needed to describe React’s behavior.

### Note

We’ve published [`types-react-codemod`](https://github.com/eps1lon/types-react-codemod/) to migrate most type related breaking changes:

\`\`\`
npx types\-react\-codemod@latest preset\-19 ./path\-to\-app
\`\`\`If you have a lot of unsound access to `element.props`, you can run this additional codemod:

\`\`\`
npx types\-react\-codemod@latest react\-element\-default\-any\-props ./path\-to\-your\-react\-ts\-files
\`\`\`
Check out [`types-react-codemod`](https://github.com/eps1lon/types-react-codemod/) for a list of supported replacements. If you feel a codemod is missing, it can be tracked in the [list of missing React 19 codemods](https://github.com/eps1lon/types-react-codemod/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3A%22React+19%22+label%3Aenhancement).

### `ref` cleanups required

*This change is included in the `react-19` codemod preset as [`no-implicit-ref-callback-return`](https://github.com/eps1lon/types-react-codemod/#no-implicit-ref-callback-return) .*

Due to the introduction of ref cleanup functions, returning anything else from a ref callback will now be rejected by TypeScript. The fix is usually to stop using implicit returns:

\`\`\`
\- \ (instance = current)} /\>\+ \ {instance = current}} /\>
\`\`\`
The original code returned the instance of the `HTMLDivElement` and TypeScript wouldn’t know if this was supposed to be a cleanup function or not.

### `useRef` requires an argument

*This change is included in the `react-19` codemod preset as [`refobject-defaults`](https://github.com/eps1lon/types-react-codemod/#refobject-defaults).*

A long\-time complaint of how TypeScript and React work has been `useRef`. We’ve changed the types so that `useRef` now requires an argument. This significantly simplifies its type signature. It’ll now behave more like `createContext`.

\`\`\`
// @ts\-expect\-error: Expected 1 argument but saw noneuseRef();// PassesuseRef(undefined);// @ts\-expect\-error: Expected 1 argument but saw nonecreateContext();// PassescreateContext(undefined);
\`\`\`
This now also means that all refs are mutable. You’ll no longer hit the issue where you can’t mutate a ref because you initialised it with `null`:

\`\`\`
const ref = useRef\(null);// Cannot assign to 'current' because it is a read\-only propertyref.current = 1;
\`\`\`
`MutableRef` is now deprecated in favor of a single `RefObject` type which `useRef` will always return:

\`\`\`
interface RefObject\ { current: T}declare function useRef\: RefObject\
\`\`\`
`useRef` still has a convenience overload for `useRef(null)` that automatically returns `RefObject`. To ease migration due to the required argument for `useRef`, a convenience overload for `useRef(undefined)` was added that automatically returns `RefObject`.

Check out [\[RFC] Make all refs mutable](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/64772) for prior discussions about this change.

### Changes to the `ReactElement` TypeScript type

*This change is included in the [`react-element-default-any-props`](https://github.com/eps1lon/types-react-codemod#react-element-default-any-props) codemod.*

The `props` of React elements now default to `unknown` instead of `any` if the element is typed as `ReactElement`. This does not affect you if you pass a type argument to `ReactElement`:

\`\`\`
type Example2 = ReactElement\\["props"];// ^? { id: string }
\`\`\`
But if you relied on the default, you now have to handle `unknown`:

\`\`\`
type Example = ReactElement\["props"];// ^? Before, was 'any', now 'unknown'
\`\`\`
You should only need it if you have a lot of legacy code relying on unsound access of element props. Element introspection only exists as an escape hatch, and you should make it explicit that your props access is unsound via an explicit `any`.

### The JSX namespace in TypeScript

This change is included in the `react-19` codemod preset as [`scoped-jsx`](https://github.com/eps1lon/types-react-codemod#scoped-jsx)

A long\-time request is to remove the global `JSX` namespace from our types in favor of `React.JSX`. This helps prevent pollution of global types which prevents conflicts between different UI libraries that leverage JSX.

You’ll now need to wrap module augmentation of the JSX namespace in \`declare module ”…”:

\`\`\`
// global.d.ts\+ declare module "react" { namespace JSX { interface IntrinsicElements { "my\-element": { myElementProps: string; }; } }\+ }
\`\`\`
The exact module specifier depends on the JSX runtime you specified in the `compilerOptions` of your `tsconfig.json`:

* For `"jsx": "react-jsx"` it would be `react/jsx-runtime`.
* For `"jsx": "react-jsxdev"` it would be `react/jsx-dev-runtime`.
* For `"jsx": "react"` and `"jsx": "preserve"` it would be `react`.

### Better `useReducer` typings

`useReducer` now has improved type inference thanks to [@mfp22](https://github.com/mfp22).

However, this required a breaking change where `useReducer` doesn’t accept the full reducer type as a type parameter but instead either needs none (and rely on contextual typing) or needs both the state and action type.

The new best practice is *not* to pass type arguments to `useReducer`.

\`\`\`
\- useReducer\\>(reducer)\+ useReducer(reducer)
\`\`\`
This may not work in edge cases where you can explicitly type the state and action, by passing in the `Action` in a tuple:

\`\`\`
\- useReducer\\>(reducer)\+ useReducer\(reducer)
\`\`\`
If you define the reducer inline, we encourage to annotate the function parameters instead:

\`\`\`
\- useReducer\\>((state, action) =\> state)\+ useReducer((state: State, action: Action) =\> state)
\`\`\`
This is also what you’d also have to do if you move the reducer outside of the `useReducer` call:

\`\`\`
const reducer = (state: State, action: Action) =\> state;
\`\`\`
## Changelog

### Other breaking changes

* **react\-dom**: Error for javascript URLs in `src` and `href` [\#26507](https://github.com/facebook/react/pull/26507)
* **react\-dom**: Remove `errorInfo.digest` from `onRecoverableError` [\#28222](https://github.com/facebook/react/pull/28222)
* **react\-dom**: Remove `unstable_flushControlled` [\#26397](https://github.com/facebook/react/pull/26397)
* **react\-dom**: Remove `unstable_createEventHandle` [\#28271](https://github.com/facebook/react/pull/28271)
* **react\-dom**: Remove `unstable_renderSubtreeIntoContainer` [\#28271](https://github.com/facebook/react/pull/28271)
* **react\-dom**: Remove `unstable_runWithPriority` [\#28271](https://github.com/facebook/react/pull/28271)
* **react\-is**: Remove deprecated methods from `react-is` [28224](https://github.com/facebook/react/pull/28224)

### Other notable changes

* **react**: Batch sync, default and continuous lanes [\#25700](https://github.com/facebook/react/pull/25700)
* **react**: Don’t prerender siblings of suspended component [\#26380](https://github.com/facebook/react/pull/26380)
* **react**: Detect infinite update loops caused by render phase updates [\#26625](https://github.com/facebook/react/pull/26625)
* **react\-dom**: Transitions in popstate are now synchronous [\#26025](https://github.com/facebook/react/pull/26025)
* **react\-dom**: Remove layout effect warning during SSR [\#26395](https://github.com/facebook/react/pull/26395)
* **react\-dom**: Warn and don’t set empty string for src/href (except anchor tags) [\#28124](https://github.com/facebook/react/pull/28124)

For a full list of changes, please see the [Changelog](https://github.com/facebook/react/blob/main/CHANGELOG.md#1900-december-5-2024).

---

Thanks to [Andrew Clark](https://twitter.com/acdlite), [Eli White](https://twitter.com/Eli_White), [Jack Pope](https://github.com/jackpope), [Jan Kassens](https://github.com/kassens), [Josh Story](https://twitter.com/joshcstory), [Matt Carroll](https://twitter.com/mattcarrollcode), [Noah Lemen](https://twitter.com/noahlemen), [Sophie Alpert](https://twitter.com/sophiebits), and [Sebastian Silbermann](https://twitter.com/sebsilbermann) for reviewing and editing this post.

[PreviousReact 19 RC](/blog/2024/04/25/react-19)[NextReact Labs: What We've Been Working On – February 2024](/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024)

---



## React Conf 2024 Recap – React

[Read the full article](https://react.dev/blog/2024/05/22/react-conf-2024-recap)

[Blog](/blog)# React Conf 2024 Recap

May 22, 2024 by [Ricky Hanlon](https://twitter.com/rickhanlonii).

---

Last week we hosted React Conf 2024, a two\-day conference in Henderson, Nevada where 700\+ attendees gathered in\-person to discuss the latest in UI engineering. This was our first in\-person conference since 2019, and we were thrilled to be able to bring the community together again.

---

At React Conf 2024, we announced the [React 19 RC](/blog/2024/12/05/react-19), the [React Native New Architecture Beta](https://github.com/reactwg/react-native-new-architecture/discussions/189), and an experimental release of the [React Compiler](/learn/react-compiler). The community also took the stage to announce [React Router v7](https://remix.run/blog/merging-remix-and-react-router), [Universal Server Components](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=20765s) in Expo Router, React Server Components in [RedwoodJS](https://redwoodjs.com/blog/rsc-now-in-redwoodjs), and much more.

The entire [day 1](https://www.youtube.com/watch?v=T8TZQ6k4SLE) and [day 2](https://www.youtube.com/watch?v=0ckOUBiuxVY) streams are available online. In this post, we’ll summarize the talks and announcements from the event.

## Day 1

*[Watch the full day 1 stream here.](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=973s)*

To kick off day 1, Meta CTO [Andrew “Boz” Bosworth](https://www.threads.net/@boztank) shared a welcome message followed by an introduction by [Seth Webster](https://twitter.com/sethwebster), who manages the React Org at Meta, and our MC [Ashley Narcisse](https://twitter.com/_darkfadr).

In the day 1 keynote, [Joe Savona](https://twitter.com/en_JS) shared our goals and vision for React to make it easy for anyone to build great user experiences. [Lauren Tan](https://twitter.com/potetotes) followed with a State of React, where she shared that React was downloaded over 1 billion times in 2023, and that 37% of new developers learn to program with React. Finally, she highlighted the work of the React community to make React, React.

For more, check out these talks from the community later in the conference:

* [Vanilla React](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=5542s) by [Ryan Florence](https://twitter.com/ryanflorence)
* [React Rhythm \& Blues](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=12728s) by [Lee Robinson](https://twitter.com/leeerob)
* [RedwoodJS, now with React Server Components](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=26815s) by [Amy Dutton](https://twitter.com/selfteachme)
* [Introducing Universal React Server Components in Expo Router](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=20765s) by [Evan Bacon](https://twitter.com/Baconbrix)

Next in the keynote, [Josh Story](https://twitter.com/joshcstory) and [Andrew Clark](https://twitter.com/acdlite) shared new features coming in React 19, and announced the React 19 RC which is ready for testing in production. Check out all the features in the [React 19 release post](/blog/2024/12/05/react-19), and see these talks for deep dives on the new features:

* [What’s new in React 19](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=8880s) by [Lydia Hallie](https://twitter.com/lydiahallie)
* [React Unpacked: A Roadmap to React 19](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=10112s) by [Sam Selikoff](https://twitter.com/samselikoff)
* [React 19 Deep Dive: Coordinating HTML](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=24916s) by [Josh Story](https://twitter.com/joshcstory)
* [Enhancing Forms with React Server Components](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=25280s) by [Aurora Walberg Scharff](https://twitter.com/aurorascharff)
* [React for Two Computers](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=18825s) by [Dan Abramov](https://twitter.com/dan_abramov2)
* [And Now You Understand React Server Components](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=11256s) by [Kent C. Dodds](https://twitter.com/kentcdodds)

Finally, we ended the keynote with [Joe Savona](https://twitter.com/en_JS), [Sathya Gunasekaran](https://twitter.com/_gsathya), and [Mofei Zhang](https://twitter.com/zmofei) announcing that the React Compiler is now [Open Source](https://github.com/facebook/react/pull/29061), and sharing an experimental version of the React Compiler to try out.

For more information on using the Compiler and how it works, check out [the docs](/learn/react-compiler) and these talks:

* [Forget About Memo](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=12020s) by [Lauren Tan](https://twitter.com/potetotes)
* [React Compiler Deep Dive](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=9313s) by [Sathya Gunasekaran](https://twitter.com/_gsathya) and [Mofei Zhang](https://twitter.com/zmofei)

Watch the full day 1 keynote here:

## Day 2

*[Watch the full day 2 stream here.](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=1720s)*

To kick off day 2, [Seth Webster](https://twitter.com/sethwebster) shared a welcome message, followed by a Thank You from [Eli White](https://x.com/Eli_White) and an introduction by our Chief Vibes Officer [Ashley Narcisse](https://twitter.com/_darkfadr).

In the day 2 keynote, [Nicola Corti](https://twitter.com/cortinico) shared the State of React Native, including 78 million downloads in 2023\. He also highlighted apps using React Native including 2000\+ screens used inside of Meta; the product details page in Facebook Marketplace, which is visited more than 2 billion times per day; and part of the Microsoft Windows Start Menu and some features in almost every Microsoft Office product across mobile and desktop.

Nicola also highlighted all the work the community does to support React Native including libraries, frameworks, and multiple platforms. For more, check out these talks from the community:

* [Extending React Native beyond Mobile and Desktop Apps](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=5798s) by [Chris Traganos](https://twitter.com/chris_trag) and [Anisha Malde](https://twitter.com/anisha_malde)
* [Spatial computing with React](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=22525s) by [Michał Pierzchała](https://twitter.com/thymikee)

[Riccardo Cipolleschi](https://twitter.com/cipolleschir) continued the day 2 keynote by announcing that the React Native New Architecture is now in Beta and ready for apps to adopt in production. He shared new features and improvements in the new architecture, and shared the roadmap for the future of React Native. For more check out:

* [Cross Platform React](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=26569s) by [Olga Zinoveva](https://github.com/SlyCaptainFlint) and [Naman Goel](https://twitter.com/naman34)

Next in the keynote, Nicola announced that we are now recommending starting with a framework like Expo for all new apps created with React Native. With the change, he also announced a new React Native homepage and new Getting Started docs. You can view the new Getting Started guide in the [React Native docs](https://reactnative.dev/docs/next/environment-setup).

Finally, to end the keynote, [Kadi Kraman](https://twitter.com/kadikraman) shared the latest features and improvements in Expo, and how to get started developing with React Native using Expo.

Watch the full day 2 keynote here:

## Q\&A

The React and React Native teams also ended each day with a Q\&A session:

* [React Q\&A](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=27518s) hosted by [Michael Chan](https://twitter.com/chantastic)
* [React Native Q\&A](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=27935s) hosted by [Jamon Holmgren](https://twitter.com/jamonholmgren)

## And more…

We also heard talks on accessibility, error reporting, css, and more:

* [Demystifying accessibility in React apps](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=20655s) by [Kateryna Porshnieva](https://twitter.com/krambertech)
* [Pigment CSS, CSS in the server component age](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=21696s) by [Olivier Tassinari](https://twitter.com/olivtassinari)
* [Real\-time React Server Components](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=24070s) by [Sunil Pai](https://twitter.com/threepointone)
* [Let’s break React Rules](https://www.youtube.com/watch?v=T8TZQ6k4SLE&t=25862s) by [Charlotte Isambert](https://twitter.com/c_isambert)
* [Solve 100% of your errors](https://www.youtube.com/watch?v=0ckOUBiuxVY&t=19881s) by [Ryan Albrecht](https://github.com/ryan953)

## Thank you

Thank you to all the staff, speakers, and participants who made React Conf 2024 possible. There are too many to list, but we want to thank a few in particular.

Thank you to [Barbara Markiewicz](https://twitter.com/barbara_markie), the team at [Callstack](https://www.callstack.com/), and our React Team Developer Advocate [Matt Carroll](https://twitter.com/mattcarrollcode) for helping to plan the entire event; and to [Sunny Leggett](https://zeroslopeevents.com/about) and everyone from [Zero Slope](https://zeroslopeevents.com) for helping to organize the event.

Thank you [Ashley Narcisse](https://twitter.com/_darkfadr) for being our MC and Chief Vibes Officer; and to [Michael Chan](https://twitter.com/chantastic) and [Jamon Holmgren](https://twitter.com/jamonholmgren) for hosting the Q\&A sessions.

Thank you [Seth Webster](https://twitter.com/sethwebster) and [Eli White](https://x.com/Eli_White) for welcoming us each day and providing direction on structure and content; and to [Tom Occhino](https://twitter.com/tomocchino) for joining us with a special message during the after\-party.

Thank you [Ricky Hanlon](https://www.youtube.com/watch?v=FxTZL2U-uKg&t=1263s) for providing detailed feedback on talks, working on slide designs, and generally filling in the gaps to sweat the details.

Thank you [Callstack](https://www.callstack.com/) for building the conference website; and to [Kadi Kraman](https://twitter.com/kadikraman) and the [Expo](https://expo.dev/) team for building the conference mobile app.

Thank you to all the sponsors who made the event possible: [Remix](https://remix.run/), [Amazon](https://developer.amazon.com/apps-and-games?cmp=US_2024_05_3P_React-Conf-2024&ch=prtnr&chlast=prtnr&pub=ref&publast=ref&type=org&typelast=org), [MUI](https://mui.com/), [Sentry](https://sentry.io/for/react/?utm_source=sponsored-conf&utm_medium=sponsored-event&utm_campaign=frontend-fy25q2-evergreen&utm_content=logo-reactconf2024-learnmore), [Abbott](https://www.jobs.abbott/software), [Expo](https://expo.dev/), [RedwoodJS](https://redwoodjs.com/), and [Vercel](https://vercel.com).

Thank you to the AV Team for the visuals, stage, and sound; and to the Westin Hotel for hosting us.

Thank you to all the speakers who shared their knowledge and experiences with the community.

Finally, thank you to everyone who attended in person and online to show what makes React, React. React is more than a library, it is a community, and it was inspiring to see everyone come together to share and learn together.

See you next time!

[PreviousReact Compiler Beta Release and Roadmap](/blog/2024/10/21/react-compiler-beta-release)[NextReact 19 RC](/blog/2024/04/25/react-19)

---



## React Compiler Beta Release – React

[Read the full article](https://react.dev/blog/2024/10/21/react-compiler-beta-release)

[Blog](/blog)# React Compiler Beta Release

October 21, 2024 by [Lauren Tan](https://twitter.com/potetotes).

---

The React team is excited to share new updates:

1. We’re publishing React Compiler Beta today, so that early adopters and library maintainers can try it and provide feedback.
2. We’re officially supporting React Compiler for apps on React 17\+, through an optional `react-compiler-runtime` package.
3. We’re opening up public membership of the [React Compiler Working Group](https://github.com/reactwg/react-compiler) to prepare the community for gradual adoption of the compiler.

---

At [React Conf 2024](/blog/2024/05/22/react-conf-2024-recap), we announced the experimental release of React Compiler, a build\-time tool that optimizes your React app through automatic memoization. [You can find an introduction to React Compiler here](/learn/react-compiler).

Since the first release, we’ve fixed numerous bugs reported by the React community, received several high quality bug fixes and contributions[1](#user-content-fn-1) to the compiler, made the compiler more resilient to the broad diversity of JavaScript patterns, and have continued to roll out the compiler more widely at Meta.

In this post, we want to share what’s next for React Compiler.

## Try React Compiler Beta today

At [React India 2024](https://www.youtube.com/watch?v=qd5yk2gxbtg), we shared an update on React Compiler. Today, we are excited to announce a new Beta release of React Compiler and ESLint plugin. New betas are published to npm using the `@beta` tag.

To install React Compiler Beta:

 Terminal  Copynpm install \-D babel\-plugin\-react\-compiler@beta eslint\-plugin\-react\-compiler@beta
Or, if you’re using Yarn:

 Terminal  Copyyarn add \-D babel\-plugin\-react\-compiler@beta eslint\-plugin\-react\-compiler@beta
You can watch [Sathya Gunasekaran’s](https://twitter.com/_gsathya) talk at React India here:

## We recommend everyone use the React Compiler linter today

React Compiler’s ESLint plugin helps developers proactively identify and correct [Rules of React](/reference/rules) violations. **We strongly recommend everyone use the linter today**. The linter does not require that you have the compiler installed, so you can use it independently, even if you are not ready to try out the compiler.

To install the linter only:

 Terminal  Copynpm install \-D eslint\-plugin\-react\-compiler@beta
Or, if you’re using Yarn:

 Terminal  Copyyarn add \-D eslint\-plugin\-react\-compiler@beta
After installation you can enable the linter by [adding it to your ESLint config](/learn/react-compiler#installing-eslint-plugin-react-compiler). Using the linter helps identify Rules of React breakages, making it easier to adopt the compiler when it’s fully released.

## Backwards Compatibility

React Compiler produces code that depends on runtime APIs added in React 19, but we’ve since added support for the compiler to also work with React 17 and 18\. If you are not on React 19 yet, in the Beta release you can now try out React Compiler by specifying a minimum `target` in your compiler config, and adding `react-compiler-runtime` as a dependency. [You can find docs on this here](/learn/react-compiler#using-react-compiler-with-react-17-or-18).

## Using React Compiler in libraries

Our initial release was focused on identifying major issues with using the compiler in applications. We’ve gotten great feedback and have substantially improved the compiler since then. We’re now ready for broad feedback from the community, and for library authors to try out the compiler to improve performance and the developer experience of maintaining your library.

React Compiler can also be used to compile libraries. Because React Compiler needs to run on the original source code prior to any code transformations, it is not possible for an application’s build pipeline to compile the libraries they use. Hence, our recommendation is for library maintainers to independently compile and test their libraries with the compiler, and ship compiled code to npm.

Because your code is pre\-compiled, users of your library will not need to have the compiler enabled in order to benefit from the automatic memoization applied to your library. If your library targets apps not yet on React 19, specify a minimum `target` and add `react-compiler-runtime` as a direct dependency. The runtime package will use the correct implementation of APIs depending on the application’s version, and polyfill the missing APIs if necessary.

[You can find more docs on this here.](/learn/react-compiler#using-the-compiler-on-libraries)

## Opening up React Compiler Working Group to everyone

We previously announced the invite\-only [React Compiler Working Group](https://github.com/reactwg/react-compiler) at React Conf to provide feedback, ask questions, and collaborate on the compiler’s experimental release.

From today, together with the Beta release of React Compiler, we are opening up Working Group membership to everyone. The goal of the React Compiler Working Group is to prepare the ecosystem for a smooth, gradual adoption of React Compiler by existing applications and libraries. Please continue to file bug reports in the [React repo](https://github.com/facebook/react), but please leave feedback, ask questions, or share ideas in the [Working Group discussion forum](https://github.com/reactwg/react-compiler/discussions).

The core team will also use the discussions repo to share our research findings. As the Stable Release gets closer, any important information will also be posted on this forum.

## React Compiler at Meta

At [React Conf](/blog/2024/05/22/react-conf-2024-recap), we shared that our rollout of the compiler on Quest Store and Instagram were successful. Since then, we’ve deployed React Compiler across several more major web apps at Meta, including [Facebook](https://www.facebook.com) and [Threads](https://www.threads.net). That means if you’ve used any of these apps recently, you may have had your experience powered by the compiler. We were able to onboard these apps onto the compiler with few code changes required, in a monorepo with more than 100,000 React components.

We’ve seen notable performance improvements across all of these apps. As we’ve rolled out, we’re continuing to see results on the order of [the wins we shared previously at ReactConf](https://youtu.be/lyEKhv8-3n0?t=3223). These apps have already been heavily hand tuned and optimized by Meta engineers and React experts over the years, so even improvements on the order of a few percent are a huge win for us.

We also expected developer productivity wins from React Compiler. To measure this, we collaborated with our data science partners at Meta[2](#user-content-fn-2) to conduct a thorough statistical analysis of the impact of manual memoization on productivity. Before rolling out the compiler at Meta, we discovered that only about 8% of React pull requests used manual memoization and that these pull requests took 31\-46% longer to author[3](#user-content-fn-3). This confirmed our intuition that manual memoization introduces cognitive overhead, and we anticipate that React Compiler will lead to more efficient code authoring and review. Notably, React Compiler also ensures that *all* code is memoized by default, not just the (in our case) 8% where developers explicitly apply memoization.

## Roadmap to Stable

*This is not a final roadmap, and is subject to change.*

We intend to ship a Release Candidate of the compiler in the near future following the Beta release, when the majority of apps and libraries that follow the Rules of React have been proven to work well with the compiler. After a period of final feedback from the community, we plan on a Stable Release for the compiler. The Stable Release will mark the beginning of a new foundation for React, and all apps and libraries will be strongly recommended to use the compiler and ESLint plugin.

* ✅ Experimental: Released at React Conf 2024, primarily for feedback from early adopters.
* ✅ Public Beta: Available today, for feedback from the wider community.
* 🚧 Release Candidate (RC): React Compiler works for the majority of rule\-following apps and libraries without issue.
* 🚧 General Availability: After final feedback period from the community.

These releases also include the compiler’s ESLint plugin, which surfaces diagnostics statically analyzed by the compiler. We plan to combine the existing eslint\-plugin\-react\-hooks plugin with the compiler’s ESLint plugin, so only one plugin needs to be installed.

Post\-Stable, we plan to add more compiler optimizations and improvements. This includes both continual improvements to automatic memoization, and new optimizations altogether, with minimal to no change of product code. Upgrading to each new release of the compiler is aimed to be straightforward, and each upgrade will continue to improve performance and add better handling of diverse JavaScript and React patterns.

Throughout this process, we also plan to prototype an IDE extension for React. It is still very early in research, so we expect to be able to share more of our findings with you in a future React Labs blog post.

---

Thanks to [Sathya Gunasekaran](https://twitter.com/_gsathya), [Joe Savona](https://twitter.com/en_JS), [Ricky Hanlon](https://twitter.com/rickhanlonii), [Alex Taylor](https://github.com/alexmckenley), [Jason Bonta](https://twitter.com/someextent), and [Eli White](https://twitter.com/Eli_White) for reviewing and editing this post.

---

## Footnotes

1. Thanks [@nikeee](https://github.com/facebook/react/pulls?q=is%3Apr+author%3Anikeee), [@henryqdineen](https://github.com/facebook/react/pulls?q=is%3Apr+author%3Ahenryqdineen), [@TrickyPi](https://github.com/facebook/react/pulls?q=is%3Apr+author%3ATrickyPi), and several others for their contributions to the compiler. [↩](#user-content-fnref-1)
2. Thanks [Vaishali Garg](https://www.linkedin.com/in/vaishaligarg09) for leading this study on React Compiler at Meta, and for reviewing this post. [↩](#user-content-fnref-2)
3. After controlling on author tenure, diff length/complexity, and other potential confounding factors. [↩](#user-content-fnref-3)

[PreviousReact 19](/blog/2024/12/05/react-19)[NextReact Conf 2024 Recap](/blog/2024/05/22/react-conf-2024-recap)

---



## React v19 – React

[Read the full article](https://react.dev/blog/2024/12/05/react-19)

[Blog](/blog)# React v19

December 05, 2024 by [The React Team](/community/team)

---

### Note

### React 19 is now stable!

Additions since this post was originally shared with the React 19 RC in April:

* **Pre\-warming for suspended trees**: see [Improvements to Suspense](/blog/2024/04/25/react-19-upgrade-guide#improvements-to-suspense).
* **React DOM static APIs**: see [New React DOM Static APIs](#new-react-dom-static-apis).

*The date for this post has been updated to reflect the stable release date.*

React v19 is now available on npm!

In our [React 19 Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide), we shared step\-by\-step instructions for upgrading your app to React 19\. In this post, we’ll give an overview of the new features in React 19, and how you can adopt them.

* [What’s new in React 19](#whats-new-in-react-19)
* [Improvements in React 19](#improvements-in-react-19)
* [How to upgrade](#how-to-upgrade)

For a list of breaking changes, see the [Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide).

---

## What’s new in React 19

### Actions

A common use case in React apps is to perform a data mutation and then update state in response. For example, when a user submits a form to change their name, you will make an API request, and then handle the response. In the past, you would need to handle pending states, errors, optimistic updates, and sequential requests manually.

For example, you could handle the pending and error state in `useState`:

\`\`\`
// Before Actionsfunction UpdateName({}) { const \[name, setName] = useState(""); const \[error, setError] = useState(null); const \[isPending, setIsPending] = useState(false); const handleSubmit = async () =\> { setIsPending(true); const error = await updateName(name); setIsPending(false); if (error) { setError(error); return; } redirect("/path"); }; return ( \ \ setName(event.target.value)} /\> \ Update \ {error \&\& \{error}\} \ );}
\`\`\`
In React 19, we’re adding support for using async functions in transitions to handle pending states, errors, forms, and optimistic updates automatically.

For example, you can use `useTransition` to handle the pending state for you:

\`\`\`
// Using pending state from Actionsfunction UpdateName({}) { const \[name, setName] = useState(""); const \[error, setError] = useState(null); const \[isPending, startTransition] = useTransition(); const handleSubmit = () =\> { startTransition(async () =\> { const error = await updateName(name); if (error) { setError(error); return; } redirect("/path"); }) }; return ( \ \ setName(event.target.value)} /\> \ Update \ {error \&\& \{error}\} \ );}
\`\`\`
The async transition will immediately set the `isPending` state to true, make the async request(s), and switch `isPending` to false after any transitions. This allows you to keep the current UI responsive and interactive while the data is changing.

### Note

#### By convention, functions that use async transitions are called “Actions”.

Actions automatically manage submitting data for you:

* **Pending state**: Actions provide a pending state that starts at the beginning of a request and automatically resets when the final state update is committed.
* **Optimistic updates**: Actions support the new [`useOptimistic`](#new-hook-optimistic-updates) hook so you can show users instant feedback while the requests are submitting.
* **Error handling**: Actions provide error handling so you can display Error Boundaries when a request fails, and revert optimistic updates to their original value automatically.
* **Forms**: `` elements now support passing functions to the `action` and `formAction` props. Passing functions to the `action` props use Actions by default and reset the form automatically after submission.

Building on top of Actions, React 19 introduces [`useOptimistic`](#new-hook-optimistic-updates) to manage optimistic updates, and a new hook [`React.useActionState`](#new-hook-useactionstate) to handle common cases for Actions. In `react-dom` we’re adding [`` Actions](#form-actions) to manage forms automatically and [`useFormStatus`](#new-hook-useformstatus) to support the common cases for Actions in forms.

In React 19, the above example can be simplified to:

\`\`\`
// Using \ Actions and useActionStatefunction ChangeName({ name, setName }) { const \[error, submitAction, isPending] = useActionState( async (previousState, formData) =\> { const error = await updateName(formData.get("name")); if (error) { return error; } redirect("/path"); return null; }, null, ); return ( \ \ \Update\ {error \&\& \{error}\} \ );}
\`\`\`
In the next section, we’ll break down each of the new Action features in React 19\.

### New hook: `useActionState`

To make the common cases easier for Actions, we’ve added a new hook called `useActionState`:

\`\`\`
const \[error, submitAction, isPending] = useActionState( async (previousState, newName) =\> { const error = await updateName(newName); if (error) { // You can return any result of the action. // Here, we return only the error. return error; } // handle success return null; }, null,);
\`\`\`
`useActionState` accepts a function (the “Action”), and returns a wrapped Action to call. This works because Actions compose. When the wrapped Action is called, `useActionState` will return the last result of the Action as `data`, and the pending state of the Action as `pending`.

### Note

`React.useActionState` was previously called `ReactDOM.useFormState` in the Canary releases, but we’ve renamed it and deprecated `useFormState`.

See [\#28491](https://github.com/facebook/react/pull/28491) for more info.

For more information, see the docs for [`useActionState`](/reference/react/useActionState).

### React DOM: `` Actions

Actions are also integrated with React 19’s new `` features for `react-dom`. We’ve added support for passing functions as the `action` and `formAction` props of ``, ``, and `` elements to automatically submit forms with Actions:

\`\`\`
\
\`\`\`
When a `` Action succeeds, React will automatically reset the form for uncontrolled components. If you need to reset the `` manually, you can call the new `requestFormReset` React DOM API.

For more information, see the `react-dom` docs for [``](/reference/react-dom/components/form), [``](/reference/react-dom/components/input), and ``.

### React DOM: New hook: `useFormStatus`

In design systems, it’s common to write design components that need access to information about the `` they’re in, without drilling props down to the component. This can be done via Context, but to make the common case easier, we’ve added a new hook `useFormStatus`:

\`\`\`
import {useFormStatus} from 'react\-dom';function DesignButton() { const {pending} = useFormStatus(); return \}
\`\`\`
`useFormStatus` reads the status of the parent `` as if the form was a Context provider.

For more information, see the `react-dom` docs for [`useFormStatus`](/reference/react-dom/hooks/useFormStatus).

### New hook: `useOptimistic`

Another common UI pattern when performing a data mutation is to show the final state optimistically while the async request is underway. In React 19, we’re adding a new hook called `useOptimistic` to make this easier:

\`\`\`
function ChangeName({currentName, onUpdateName}) { const \[optimisticName, setOptimisticName] = useOptimistic(currentName); const submitAction = async formData =\> { const newName = formData.get("name"); setOptimisticName(newName); const updatedName = await updateName(newName); onUpdateName(updatedName); }; return ( \ \Your name is: {optimisticName}\ \ \Change Name:\ \ \ \ );}
\`\`\`
The `useOptimistic` hook will immediately render the `optimisticName` while the `updateName` request is in progress. When the update finishes or errors, React will automatically switch back to the `currentName` value.

For more information, see the docs for [`useOptimistic`](/reference/react/useOptimistic).

### New API: `use`

In React 19 we’re introducing a new API to read resources in render: `use`.

For example, you can read a promise with `use`, and React will Suspend until the promise resolves:

\`\`\`
import {use} from 'react';function Comments({commentsPromise}) { // \`use\` will suspend until the promise resolves. const comments = use(commentsPromise); return comments.map(comment =\> \{comment}\);}function Page({commentsPromise}) { // When \`use\` suspends in Comments, // this Suspense boundary will be shown. return ( \Loading...\}\> \ \ )}
\`\`\`
### Note

#### `use` does not support promises created in render.

If you try to pass a promise created in render to `use`, React will warn:

ConsoleA component was suspended by an uncached promise. Creating promises inside a Client Component or hook is not yet supported, except via a Suspense\-compatible library or framework.To fix, you need to pass a promise from a suspense powered library or framework that supports caching for promises. In the future we plan to ship features to make it easier to cache promises in render.

You can also read context with `use`, allowing you to read Context conditionally such as after early returns:

\`\`\`
import {use} from 'react';import ThemeContext from './ThemeContext'function Heading({children}) { if (children == null) { return null; } // This would not work with useContext // because of the early return. const theme = use(ThemeContext); return ( \ {children} \ );}
\`\`\`
The `use` API can only be called in render, similar to hooks. Unlike hooks, `use` can be called conditionally. In the future we plan to support more ways to consume resources in render with `use`.

For more information, see the docs for [`use`](/reference/react/use).

## New React DOM Static APIs

We’ve added two new APIs to `react-dom/static` for static site generation:

* [`prerender`](/reference/react-dom/static/prerender)
* [`prerenderToNodeStream`](/reference/react-dom/static/prerenderToNodeStream)

These new APIs improve on `renderToString` by waiting for data to load for static HTML generation. They are designed to work with streaming environments like Node.js Streams and Web Streams. For example, in a Web Stream environment, you can prerender a React tree to static HTML with `prerender`:

\`\`\`
import { prerender } from 'react\-dom/static';async function handler(request) { const {prelude} = await prerender(\, { bootstrapScripts: \['/main.js'] }); return new Response(prelude, { headers: { 'content\-type': 'text/html' }, });}
\`\`\`
Prerender APIs will wait for all data to load before returning the static HTML stream. Streams can be converted to strings, or sent with a streaming response. They do not support streaming content as it loads, which is supported by the existing [React DOM server rendering APIs](/reference/react-dom/server).

For more information, see [React DOM Static APIs](/reference/react-dom/static).

## React Server Components

### Server Components

Server Components are a new option that allows rendering components ahead of time, before bundling, in an environment separate from your client application or SSR server. This separate environment is the “server” in React Server Components. Server Components can run once at build time on your CI server, or they can be run for each request using a web server.

React 19 includes all of the React Server Components features included from the Canary channel. This means libraries that ship with Server Components can now target React 19 as a peer dependency with a `react-server` [export condition](https://github.com/reactjs/rfcs/blob/main/text/0227-server-module-conventions.md#react-server-conditional-exports) for use in frameworks that support the [Full\-stack React Architecture](/learn/start-a-new-react-project#which-features-make-up-the-react-teams-full-stack-architecture-vision).

### Note

#### How do I build support for Server Components?

While React Server Components in React 19 are stable and will not break between minor versions, the underlying APIs used to implement a React Server Components bundler or framework do not follow semver and may break between minors in React 19\.x.

To support React Server Components as a bundler or framework, we recommend pinning to a specific React version, or using the Canary release. We will continue working with bundlers and frameworks to stabilize the APIs used to implement React Server Components in the future.

For more, see the docs for [React Server Components](/reference/rsc/server-components).

### Server Actions

Server Actions allow Client Components to call async functions executed on the server.

When a Server Action is defined with the `"use server"` directive, your framework will automatically create a reference to the server function, and pass that reference to the Client Component. When that function is called on the client, React will send a request to the server to execute the function, and return the result.

### Note

#### There is no directive for Server Components.

A common misunderstanding is that Server Components are denoted by `"use server"`, but there is no directive for Server Components. The `"use server"` directive is used for Server Actions.

For more info, see the docs for [Directives](/reference/rsc/directives).

Server Actions can be created in Server Components and passed as props to Client Components, or they can be imported and used in Client Components.

For more, see the docs for [React Server Actions](/reference/rsc/server-actions).

## Improvements in React 19

### `ref` as a prop

Starting in React 19, you can now access `ref` as a prop for function components:

\`\`\`
function MyInput({placeholder, ref}) { return \}//...\
\`\`\`
New function components will no longer need `forwardRef`, and we will be publishing a codemod to automatically update your components to use the new `ref` prop. In future versions we will deprecate and remove `forwardRef`.

### Note

`refs` passed to classes are not passed as props since they reference the component instance.

### Diffs for hydration errors

We also improved error reporting for hydration errors in `react-dom`. For example, instead of logging multiple errors in DEV without any information about the mismatch:

ConsoleWarning: Text content did not match. Server: “Server” Client: “Client”
 at span
 at AppWarning: An error occurred during hydration. The server HTML was replaced with client content in \.Warning: Text content did not match. Server: “Server” Client: “Client”
 at span
 at AppWarning: An error occurred during hydration. The server HTML was replaced with client content in \.Uncaught Error: Text content does not match server\-rendered HTML.
 at checkForUnmatchedText
 …
We now log a single message with a diff of the mismatch:

ConsoleUncaught Error: Hydration failed because the server rendered HTML didn’t match the client. As a result this tree will be regenerated on the client. This can happen if an SSR\-ed Client Component used:

\- A server/client branch `if (typeof window !== 'undefined')`.
\- Variable input such as `Date.now()` or `Math.random()` which changes each time it’s called.
\- Date formatting in a user’s locale which doesn’t match the server.
\- External changing data without sending a snapshot of it along with the HTML.
\- Invalid HTML tag nesting.

It can also happen if the client has a browser extension installed which messes with the HTML before React loaded.

[https://react.dev/link/hydration\-mismatch](https://react.dev/link/hydration-mismatch) 

 \
 \
\+ Client
\- Server

 at throwOnHydrationMismatch
 …
### `` as a provider

In React 19, you can render `` as a provider instead of ``:

\`\`\`
const ThemeContext = createContext('');function App({children}) { return ( \ {children} \ ); }
\`\`\`
New Context providers can use `` and we will be publishing a codemod to convert existing providers. In future versions we will deprecate ``.

### Cleanup functions for refs

We now support returning a cleanup function from `ref` callbacks:

\`\`\`
\ { // ref created // NEW: return a cleanup function to reset // the ref when element is removed from DOM. return () =\> { // ref cleanup }; }}/\>
\`\`\`
When the component unmounts, React will call the cleanup function returned from the `ref` callback. This works for DOM refs, refs to class components, and `useImperativeHandle`.

### Note

Previously, React would call `ref` functions with `null` when unmounting the component. If your `ref` returns a cleanup function, React will now skip this step.

In future versions, we will deprecate calling refs with `null` when unmounting components.

Due to the introduction of ref cleanup functions, returning anything else from a `ref` callback will now be rejected by TypeScript. The fix is usually to stop using implicit returns, for example:

\`\`\`
\- \ (instance = current)} /\>\+ \ {instance = current}} /\>
\`\`\`
The original code returned the instance of the `HTMLDivElement` and TypeScript wouldn’t know if this was *supposed* to be a cleanup function or if you didn’t want to return a cleanup function.

You can codemod this pattern with [`no-implicit-ref-callback-return`](https://github.com/eps1lon/types-react-codemod/#no-implicit-ref-callback-return).

### `useDeferredValue` initial value

We’ve added an `initialValue` option to `useDeferredValue`:

\`\`\`
function Search({deferredValue}) { // On initial render the value is ''. // Then a re\-render is scheduled with the deferredValue. const value = useDeferredValue(deferredValue, ''); return ( \ );}
\`\`\`
When initialValue is provided, `useDeferredValue` will return it as `value` for the initial render of the component, and schedules a re\-render in the background with the deferredValue returned.

For more, see [`useDeferredValue`](/reference/react/useDeferredValue).

### Support for Document Metadata

In HTML, document metadata tags like ``, ``, and `` are reserved for placement in the `` section of the document. In React, the component that decides what metadata is appropriate for the app may be very far from the place where you render the `` or React does not render the `` at all. In the past, these elements would need to be inserted manually in an effect, or by libraries like [`react-helmet`](https://github.com/nfl/react-helmet), and required careful handling when server rendering a React application.

In React 19, we’re adding support for rendering document metadata tags in components natively:

\`\`\`
function BlogPost({post}) { return ( \ \{post.title}\ \{post.title}\ \ \ \ \ Eee equals em\-see\-squared... \ \ );}
\`\`\`
When React renders this component, it will see the `` `` and `` tags, and automatically hoist them to the `` section of document. By supporting these metadata tags natively, we’re able to ensure they work with client\-only apps, streaming SSR, and Server Components.

### Note

#### You may still want a Metadata library

For simple use cases, rendering Document Metadata as tags may be suitable, but libraries can offer more powerful features like overriding generic metadata with specific metadata based on the current route. These features make it easier for frameworks and libraries like [`react-helmet`](https://github.com/nfl/react-helmet) to support metadata tags, rather than replace them.

For more info, see the docs for [``](/reference/react-dom/components/title), [``](/reference/react-dom/components/link), and [``](/reference/react-dom/components/meta).

### Support for stylesheets

Stylesheets, both externally linked (``) and inline (`...`), require careful positioning in the DOM due to style precedence rules. Building a stylesheet capability that allows for composability within components is hard, so users often end up either loading all of their styles far from the components that may depend on them, or they use a style library which encapsulates this complexity.

In React 19, we’re addressing this complexity and providing even deeper integration into Concurrent Rendering on the Client and Streaming Rendering on the Server with built in support for stylesheets. If you tell React the `precedence` of your stylesheet it will manage the insertion order of the stylesheet in the DOM and ensure that the stylesheet (if external) is loaded before revealing content that depends on those style rules.

\`\`\`
function ComponentOne() { return ( \ \ \ \ {...} \ \ )}function ComponentTwo() { return ( \ \{...}\ \ \ )}
\`\`\`
During Server Side Rendering React will include the stylesheet in the ``, which ensures that the browser will not paint until it has loaded. If the stylesheet is discovered late after we’ve already started streaming, React will ensure that the stylesheet is inserted into the `` on the client before revealing the content of a Suspense boundary that depends on that stylesheet.

During Client Side Rendering React will wait for newly rendered stylesheets to load before committing the render. If you render this component from multiple places within your application React will only include the stylesheet once in the document:

\`\`\`
function App() { return \ \ ... \ // won't lead to a duplicate stylesheet link in the DOM \}
\`\`\`
For users accustomed to loading stylesheets manually this is an opportunity to locate those stylesheets alongside the components that depend on them allowing for better local reasoning and an easier time ensuring you only load the stylesheets that you actually depend on.

Style libraries and style integrations with bundlers can also adopt this new capability so even if you don’t directly render your own stylesheets, you can still benefit as your tools are upgraded to use this feature.

For more details, read the docs for [``](/reference/react-dom/components/link) and [``](/reference/react-dom/components/style).

### Support for async scripts

In HTML normal scripts (``) and deferred scripts (``) load in document order which makes rendering these kinds of scripts deep within your component tree challenging. Async scripts (``) however will load in arbitrary order.

In React 19 we’ve included better support for async scripts by allowing you to render them anywhere in your component tree, inside the components that actually depend on the script, without having to manage relocating and deduplicating script instances.

\`\`\`
function MyComponent() { return ( \ \ Hello World \ )}function App() { \ \ \ ... \ // won't lead to duplicate script in the DOM \ \}
\`\`\`
In all rendering environments, async scripts will be deduplicated so that React will only load and execute the script once even if it is rendered by multiple different components.

In Server Side Rendering, async scripts will be included in the `` and prioritized behind more critical resources that block paint such as stylesheets, fonts, and image preloads.

For more details, read the docs for [``](/reference/react-dom/components/script).

### Support for preloading resources

During initial document load and on client side updates, telling the Browser about resources that it will likely need to load as early as possible can have a dramatic effect on page performance.

React 19 includes a number of new APIs for loading and preloading Browser resources to make it as easy as possible to build great experiences that aren’t held back by inefficient resource loading.

\`\`\`
import { prefetchDNS, preconnect, preload, preinit } from 'react\-dom'function MyComponent() { preinit('https://.../path/to/some/script.js', {as: 'script' }) // loads and executes this script eagerly preload('https://.../path/to/font.woff', { as: 'font' }) // preloads this font preload('https://.../path/to/stylesheet.css', { as: 'style' }) // preloads this stylesheet prefetchDNS('https://...') // when you may not actually request anything from this host preconnect('https://...') // when you will request something but aren't sure what}
\`\`\`
\`\`\`
\\ \ \ \ \ \ \ \\ \ \ ... \\
\`\`\`
These APIs can be used to optimize initial page loads by moving discovery of additional resources like fonts out of stylesheet loading. They can also make client updates faster by prefetching a list of resources used by an anticipated navigation and then eagerly preloading those resources on click or even on hover.

For more details see [Resource Preloading APIs](/reference/react-dom#resource-preloading-apis).

### Compatibility with third\-party scripts and extensions

We’ve improved hydration to account for third\-party scripts and browser extensions.

When hydrating, if an element that renders on the client doesn’t match the element found in the HTML from the server, React will force a client re\-render to fix up the content. Previously, if an element was inserted by third\-party scripts or browser extensions, it would trigger a mismatch error and client render.

In React 19, unexpected tags in the `` and `` will be skipped over, avoiding the mismatch errors. If React needs to re\-render the entire document due to an unrelated hydration mismatch, it will leave in place stylesheets inserted by third\-party scripts and browser extensions.

### Better error reporting

We improved error handling in React 19 to remove duplication and provide options for handling caught and uncaught errors. For example, when there’s an error in render caught by an Error Boundary, previously React would throw the error twice (once for the original error, then again after failing to automatically recover), and then call `console.error` with info about where the error occurred.

This resulted in three errors for every caught error:

ConsoleUncaught Error: hit
 at Throws
 at renderWithHooks
 …Uncaught Error: hit \<\-\- Duplicate
 at Throws
 at renderWithHooks
 …The above error occurred in the Throws component:
 at Throws
 at ErrorBoundary
 at App

React will try to recreate this component tree from scratch using the error boundary you provided, ErrorBoundary.
In React 19, we log a single error with all the error information included:

ConsoleError: hit
 at Throws
 at renderWithHooks
 …

The above error occurred in the Throws component:
 at Throws
 at ErrorBoundary
 at App

React will try to recreate this component tree from scratch using the error boundary you provided, ErrorBoundary.
 at ErrorBoundary
 at App
Additionally, we’ve added two new root options to complement `onRecoverableError`:

* `onCaughtError`: called when React catches an error in an Error Boundary.
* `onUncaughtError`: called when an error is thrown and not caught by an Error Boundary.
* `onRecoverableError`: called when an error is thrown and automatically recovered.

For more info and examples, see the docs for [`createRoot`](/reference/react-dom/client/createRoot) and [`hydrateRoot`](/reference/react-dom/client/hydrateRoot).

### Support for Custom Elements

React 19 adds full support for custom elements and passes all tests on [Custom Elements Everywhere](https://custom-elements-everywhere.com/).

In past versions, using Custom Elements in React has been difficult because React treated unrecognized props as attributes rather than properties. In React 19, we’ve added support for properties that works on the client and during SSR with the following strategy:

* **Server Side Rendering**: props passed to a custom element will render as attributes if their type is a primitive value like `string`, `number`, or the value is `true`. Props with non\-primitive types like `object`, `symbol`, `function`, or value `false` will be omitted.
* **Client Side Rendering**: props that match a property on the Custom Element instance will be assigned as properties, otherwise they will be assigned as attributes.

Thanks to [Joey Arhar](https://github.com/josepharhar) for driving the design and implementation of Custom Element support in React.

#### How to upgrade

See the [React 19 Upgrade Guide](/blog/2024/04/25/react-19-upgrade-guide) for step\-by\-step instructions and a full list of breaking and notable changes.

*Note: this post was originally published 04/25/2024 and has been updated to 12/05/2024 with the stable release.*

[PreviousBlog](/blog)[NextReact Compiler Beta Release and Roadmap](/blog/2024/10/21/react-compiler-beta-release)

---



