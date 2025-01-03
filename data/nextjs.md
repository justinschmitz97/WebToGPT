# https://nextjs.org/

## Directives: use cache | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/directives/use-cache)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Directives](/docs/app/api-reference/directives)use cache# use cache

This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](/docs/app/building-your-application/upgrading/canary), and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The `use cache` directive designates a component and/or a function to be cached. It can be used at the top of a file to indicate that all exports in the file are cacheable, or inline at the top of a function or component to inform Next.js the return value should be cached and reused for subsequent requests. This is an experimental Next.js feature, and not a native React feature like [`use client`](/docs/app/api-reference/directives/use-client) or [`use server`](/docs/app/api-reference/directives/use-server).

## [Usage](#usage)

Enable support for the `use cache` directive with the [`dynamicIO`](/docs/app/api-reference/config/next-config-js/dynamicIO) flag in your `next.config.ts` file:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 experimental: {
 dynamicIO: true,
 },
}

export default nextConfig
\`\`\`

Then, you can use the `use cache` directive at the file, component, or function level:

\`\`\`
// File level
'use cache'

export default async function Page() {
 // ...
}

// Component level
export async function MyComponent() {
 'use cache'
 return \\
}

// Function level
export async function getData() {
 'use cache'
 const data = await fetch('/api/data')
 return data
}
\`\`\`
## [Good to know](#good-to-know)

* `use cache` is an experimental Next.js feature, and not a native React feature like [`use client`](/docs/app/api-reference/directives/use-client) or [`use server`](/docs/app/api-reference/directives/use-server).
* Any [serializable](https://react.dev/reference/rsc/use-server#serializable-parameters-and-return-values) arguments (or props) passed to the cached function, as well as any serializable values it reads from the parent scope, will be converted to a format like JSON and automatically become a part of the cache key.
* Any non\-serializable arguments, props, or closed\-over values will turn into opaque references inside the cached function, and can be only passed through and not inspected nor modified. These non\-serializable values will be filled in at the request time and won't become a part of the cache key.
	+ For example, a cached function can take in JSX as a `children` prop and return `{children}`, but it won't be able to introspect the actual `children` object.
* The return value of the cacheable function must also be serializable. This ensures that the cached data can be stored and retrieved correctly.
* Functions that use the `use cache` directive must not have any side\-effects, such as modifying state, directly manipulating the DOM, or setting timers to execute code at intervals.
* If used alongside [Partial Prerendering](/docs/app/building-your-application/rendering/partial-prerendering), segments that have `use cache` will be prerendered as part of the static HTML shell.
* The `use cache` directive will be available separately from the [`dynamicIO`](/docs/app/api-reference/config/next-config-js/dynamicIO) flag in the future.
* Unlike [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache) which only supports JSON data, `use cache` can cache any serializable data React can render, including the render output of components.

## [Examples](#examples)

### [Caching entire routes with `use cache`](#caching-entire-routes-with-use-cache)

To prerender an entire route, add `use cache` to the top **both** the `layout` and `page` files. Each of these segments are treated as separate entry points in your application, and will be cached independently.

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use cache'
import { unstable\_cacheLife as cacheLife } from 'next/cache'

export default function Layout({ children }: { children: ReactNode }) {
 return \{children}\
}
\`\`\`

Any components imported and nested in `page` file will inherit the cache behavior of `page`.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use cache'
import { unstable\_cacheLife as cacheLife } from 'next/cache'

async function Users() {
 const users = await fetch('/api/users')
 // loop through users
}

export default function Page() {
 return (
 \
 \
 \
 )
}
\`\`\`

> This is recommended for applications that previously used the [`export const dynamic = "force-static"`](/docs/app/api-reference/file-conventions/route-segment-config#dynamic) option, and will ensure the entire route is prerendered.

### [Caching component output with `use cache`](#caching-component-output-with-use-cache)

You can use `use cache` at the component level to cache any fetches or computations performed within that component. When you reuse the component throughout your application it can share the same cache entry as long as the props maintain the same structure.

The props are serialized and form part of the cache key, and the cache entry will be reused as long as the serialized props produce the same value in each instance.

app/components/bookings.tsxTypeScriptJavaScriptTypeScript\`\`\`
export async function Bookings({ type = 'haircut' }: BookingsProps) {
 'use cache'
 async function getBookingsData() {
 const data = await fetch(\`/api/bookings?type=${encodeURIComponent(type)}\`)
 return data
 }
 return //...
}

interface BookingsProps {
 type: string
}
\`\`\`

### [Caching function output with `use cache`](#caching-function-output-with-use-cache)

Since you can add `use cache` to any asynchronous function, you aren't limited to caching components or routes only. You might want to cache a network request or database query or compute something that is very slow. By adding `use cache` to a function containing this type of work it becomes cacheable, and when reused, will share the same cache entry.

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
export async function getData() {
 'use cache'

 const data = await fetch('/api/data')
 return data
}
\`\`\`

### [Revalidating](#revalidating)

By default, Next.js sets a **[revalidation period](/docs/app/building-your-application/data-fetching/fetching#revalidating-cached-data) of 15 minutes** when you use the `use cache` directive. Next.js sets a near\-infinite expiration duration, meaning it's suitable for content that doesn't need frequent updates.

While this revalidation period may be useful for content you don't expect to change often, you can use the `cacheLife` and `cacheTag` APIs to configure the cache behavior:

* [`cacheLife`](/docs/app/api-reference/functions/cacheLife): For time\-based revalidation periods.
* [`cacheTag`](/docs/app/api-reference/functions/cacheTag): For on\-demand revalidation.

Both of these APIs integrate across the client and server caching layers, meaning you can configure your caching semantics in one place and have them apply everywhere.

See the [`cacheLife`](/docs/app/api-reference/functions/cacheLife) and [`cacheTag`](/docs/app/api-reference/functions/cacheTag) docs for more information.

### [Interleaving](#interleaving)

If you need to pass non\-serializable arguments to a cacheable function, you can pass them as `children`. This means the `children` reference can change without affecting the cache entry.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page() {
 const uncachedData = await getData()
 return (
 \
 \
 \
 )
}

async function CacheComponent({ children }: { children: ReactNode }) {
 'use cache'
 const cachedData = await fetch('/api/cached\-data')
 return (
 \
 \
 {children}
 \
 )
}
\`\`\`

You can also pass Server Actions through cached components to Client Components without invoking them inside the cacheable function.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import ClientComponent from './ClientComponent'

export default async function Page() {
 const performUpdate = async () =\> {
 'use server'
 // Perform some server\-side update
 await db.update(...)
 }

 return \
}

async function CachedComponent({
 performUpdate,
}: {
 performUpdate: () =\> Promise\
}) {
 'use cache'
 // Do not call performUpdate here
 return \
}
\`\`\`

app/ClientComponent.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

export default function ClientComponent({
 action,
}: {
 action: () =\> Promise\
}) {
 return \Update\
}
\`\`\`
## Related

View related API references.[### dynamicIO

Learn how to enable the dynamicIO flag in Next.js.](/docs/app/api-reference/config/next-config-js/dynamicIO)[### cacheLife

Learn how to set up cacheLife configurations in Next.js.](/docs/app/api-reference/config/next-config-js/cacheLife)[### cacheTag

Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.](/docs/app/api-reference/functions/cacheTag)[### cacheLife

Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.](/docs/app/api-reference/functions/cacheLife)[### revalidateTag

API Reference for the revalidateTag function.](/docs/app/api-reference/functions/revalidateTag)Was this helpful?



## Getting Started: CSS and Styling | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started/css-and-styling)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[Getting Started](/docs/app/getting-started)CSS and Styling# How to use CSS in your application

Next.js provides several ways to use CSS in your application, including:

* [CSS Modules](#css-modules)
* [Global CSS](#global-css)
* [Tailwind CSS](#tailwind-css)
* [Sass](#sass)
* [CSS\-in\-JS](#css-in-js)
* [External Stylesheets](#external-stylesheets)

This page will guide you through how to use each of these approaches.

## [CSS Modules](#css-modules)

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about collisions.

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `app` directory:

app/blog/styles.module.css\`\`\`
.blog {
 padding: 24px;
}
\`\`\`
app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import styles from './styles.module.css'

export default function Page({ children }: { children: React.ReactNode }) {
 return \{children}\
}
\`\`\`

## [Global CSS](#global-css)

You can use global CSS to apply styles across your application.

To use global styles, create a new CSS file, for example `app/global.css`:

app/global.css\`\`\`
body {
 padding: 20px 20px 60px;
 max\-width: 680px;
 margin: 0 auto;
}
\`\`\`
Import the file in the root layout (`app/layout.js`) to apply the styles to **every route** in your application:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
// These styles apply to every route in the application
import './global.css'

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

> **Good to know:** Global styles can be imported into any layout, page, or component inside the `app` directory. However, since Next.js uses React's built\-in support for stylesheets to integrate with Suspense. This built\-in support currently does not remove stylesheets as you navigate between routes. Therefore, we recommend using global styles for *truly* global CSS, and [CSS Modules](#css-modules) for scoped CSS.

## [Tailwind CSS](#tailwind-css)

[Tailwind CSS](https://tailwindcss.com/) is a utility\-first CSS framework that integrates seamlessly with Next.js.

### [Installing Tailwind](#installing-tailwind)

To start using Tailwind, install the Tailwind CSS packages and run the `init` command to generate both the `tailwind.config.js` and `postcss.config.js` files:

Terminal\`\`\`
npm install \-D tailwindcss postcss autoprefixer
npx tailwindcss init \-p
\`\`\`
### [Configuring Tailwind](#configuring-tailwind)

Inside your Tailwind configuration file, add paths to the files that will use the Tailwind class names:

tailwind.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { Config } from 'tailwindcss'

export default {
 content: \[
 './app/\*\*/\*.{js,ts,jsx,tsx,mdx}',
 // Or if using \`src\` directory:
 './src/\*\*/\*.{js,ts,jsx,tsx,mdx}',
 ],
 theme: {
 extend: {},
 },
 plugins: \[],
} satisfies Config
\`\`\`

### [Using Tailwind](#using-tailwind)

Add the [Tailwind directives](https://tailwindcss.com/docs/functions-and-directives#directives) to your [Global Stylesheet](#global-css):

app/globals.css\`\`\`
@tailwind base;
@tailwind components;
@tailwind utilities;
\`\`\`
Then, import the styles in the [root layout](/docs/app/api-reference/file-conventions/layout#root-layouts):

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

// These styles apply to every route in the application
import './globals.css'

export const metadata: Metadata = {
 title: 'Create Next App',
 description: 'Generated by create next app',
}

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

Lastly, you can start writing Tailwind's utility classes in your application.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Page() {
 return \Hello, Next.js!\
}
\`\`\`

## [Sass](#sass)

Next.js integrates with [Sass](https://sass-lang.com/) using both the [`.scss`](https://sass-lang.com/documentation/syntax/#scss) and [`.sass`](https://sass-lang.com/documentation/syntax#the-indented-syntax) extensions and syntax.

You can also use component\-level Sass via [CSS Modules](#css-modules) and the `.module.scss`or `.module.sass` extension.

### [Installing Sass](#installing-sass)

To start using Sass, install the `sass` package:

Terminal\`\`\`
npm install \-\-save\-dev sass
\`\`\`
### [Customizing Sass options](#customizing-sass-options)

If you want to configure your Sass options, use the [`sassOptions`](/docs/app/api-reference/config/next-config-js/sassOptions) option in `next.config.js`.

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 sassOptions: {
 additionalData: \`$var: red;\`,
 },
}

export default nextConfig
\`\`\`

## [CSS\-in\-JS](#css-in-js)

> **Warning:** CSS\-in\-JS libraries which require runtime JavaScript are not currently supported in React Server Components. Using CSS\-in\-JS with newer React features like Server Components and Streaming requires library authors to support the latest version of React.

The following libraries are supported in **Client Components** in the `app` directory (alphabetical):

* [`ant-design`](https://ant.design/docs/react/use-with-next#using-app-router)
* [`chakra-ui`](https://chakra-ui.com/getting-started/nextjs-app-guide)
* [`@fluentui/react-components`](https://react.fluentui.dev/?path=/docs/concepts-developer-server-side-rendering-next-js-appdir-setup--page)
* [`kuma-ui`](https://kuma-ui.com)
* [`@mui/material`](https://mui.com/material-ui/guides/next-js-app-router/)
* [`@mui/joy`](https://mui.com/joy-ui/integrations/next-js-app-router/)
* [`pandacss`](https://panda-css.com)
* [`styled-jsx`](#styled-jsx)
* [`styled-components`](#styled-components)
* [`stylex`](https://stylexjs.com)
* [`tamagui`](https://tamagui.dev/docs/guides/next-js#server-components)
* [`tss-react`](https://tss-react.dev/)
* [`vanilla-extract`](https://vanilla-extract.style)

The following are currently working on support:

* [`emotion`](https://github.com/emotion-js/emotion/issues/2928)

If you want to style Server Components, we recommend using [CSS Modules](#css-modules) or other solutions that output CSS files, like [Tailwind CSS](#tailwind-css).

### [Configuring CSS\-in\-JS](#configuring-css-in-js)

To configure CSS\-in\-JS, you need to:

1. Create a **style registry** to collect all CSS rules in a render.
2. Use the `useServerInsertedHTML` hook to inject rules before any content that might use them.
3. Create a Client Component that wraps your app with the style registry during initial server\-side rendering.

#### [`styled-jsx`](#styled-jsx)

To configure `styled-jsx` for your application, create a new registry:

app/registry.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { StyleRegistry, createStyleRegistry } from 'styled\-jsx'

export default function StyledJsxRegistry({
 children,
}: {
 children: React.ReactNode
}) {
 // Only create stylesheet once with lazy initial state
 // x\-ref: https://reactjs.org/docs/hooks\-reference.html\#lazy\-initial\-state
 const \[jsxStyleRegistry] = useState(() =\> createStyleRegistry())

 useServerInsertedHTML(() =\> {
 const styles = jsxStyleRegistry.styles()
 jsxStyleRegistry.flush()
 return \{styles}\
 })

 return \{children}\
}
\`\`\`

Then, wrap your [root layout](/docs/app/api-reference/file-conventions/layout#root-layouts) with the registry:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import StyledJsxRegistry from './registry'

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \
 \{children}\
 \
 \
 )
}
\`\`\`

#### [`styled-components`](#styled-components)

To use `styled-components`, enable it in `next.config.js`:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 compiler: {
 styledComponents: true,
 },
}

export default nextConfig
\`\`\`

Then, use the `styled-components` API to create a global registry component to collect all CSS style rules generated during a render, and a function to return those rules. Then use the `useServerInsertedHTML` hook to inject the styles collected in the registry into the `` HTML tag in the root layout.

lib/registry.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { ServerStyleSheet, StyleSheetManager } from 'styled\-components'

export default function StyledComponentsRegistry({
 children,
}: {
 children: React.ReactNode
}) {
 // Only create stylesheet once with lazy initial state
 // x\-ref: https://reactjs.org/docs/hooks\-reference.html\#lazy\-initial\-state
 const \[styledComponentsStyleSheet] = useState(() =\> new ServerStyleSheet())

 useServerInsertedHTML(() =\> {
 const styles = styledComponentsStyleSheet.getStyleElement()
 styledComponentsStyleSheet.instance.clearTag()
 return \{styles}\
 })

 if (typeof window !== 'undefined') return \{children}\

 return (
 \
 {children}
 \
 )
}
\`\`\`

Wrap the `children` of the root layout with the style registry component:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import StyledComponentsRegistry from './lib/registry'

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \
 \{children}\
 \
 \
 )
}
\`\`\`

## [External stylesheets](#external-stylesheets)

Stylesheets published by external packages can be imported anywhere in the `app` directory, including colocated components:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import 'bootstrap/dist/css/bootstrap.css'

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

External stylesheets must be directly imported from an npm package or downloaded and colocated with your codebase. You cannot use ``.

## API Reference

Learn more about the features mentioned in this page by reading the API Reference.[### sassOptions

Configure Sass options.](/docs/app/api-reference/config/next-config-js/sassOptions)[### Next.js Compiler

Next.js Compiler, written in Rust, which transforms and minifies your Next.js application.](/docs/architecture/nextjs-compiler)Was this helpful?



## Metadata Files: sitemap.xml | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[File Conventions](/docs/app/api-reference/file-conventions)[Metadata Files](/docs/app/api-reference/file-conventions/metadata)sitemap.xml# sitemap.xml

`sitemap.(xml|js|ts)` is a special file that matches the [Sitemaps XML format](https://www.sitemaps.org/protocol.html) to help search engine crawlers index your site more efficiently.

### [Sitemap files (.xml)](#sitemap-files-xml)

For smaller applications, you can create a `sitemap.xml` file and place it in the root of your `app` directory.

app/sitemap.xml\`\`\`
\
 \
 \https://acme.com\
 \2023\-04\-06T15:02:24\.021Z\
 \yearly\
 \1\
 \
 \
 \https://acme.com/about\
 \2023\-04\-06T15:02:24\.021Z\
 \monthly\
 \0\.8\
 \
 \
 \https://acme.com/blog\
 \2023\-04\-06T15:02:24\.021Z\
 \weekly\
 \0\.5\
 \
\
\`\`\`
### [Generating a sitemap using code (.js, .ts)](#generating-a-sitemap-using-code-js-ts)

You can use the `sitemap.(js|ts)` file convention to programmatically **generate** a sitemap by exporting a default function that returns an array of URLs. If using TypeScript, a [`Sitemap`](#returns) type is available.

> **Good to know**: `sitemap.js` is a special Route Handler that is cached by default unless it uses a [Dynamic API](/docs/app/building-your-application/caching#dynamic-apis) or [dynamic config](/docs/app/building-your-application/caching#segment-config-options) option.

app/sitemap.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
 return \[
 {
 url: 'https://acme.com',
 lastModified: new Date(),
 changeFrequency: 'yearly',
 priority: 1,
 },
 {
 url: 'https://acme.com/about',
 lastModified: new Date(),
 changeFrequency: 'monthly',
 priority: 0\.8,
 },
 {
 url: 'https://acme.com/blog',
 lastModified: new Date(),
 changeFrequency: 'weekly',
 priority: 0\.5,
 },
 ]
}
\`\`\`

Output:

acme.com/sitemap.xml\`\`\`
\
 \
 \https://acme.com\
 \2023\-04\-06T15:02:24\.021Z\
 \yearly\
 \1\
 \
 \
 \https://acme.com/about\
 \2023\-04\-06T15:02:24\.021Z\
 \monthly\
 \0\.8\
 \
 \
 \https://acme.com/blog\
 \2023\-04\-06T15:02:24\.021Z\
 \weekly\
 \0\.5\
 \
\
\`\`\`
### [Image Sitemaps](#image-sitemaps)

You can use `images` property to create image sitemaps. Learn more details in the [Google Developer Docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps).

app/sitemap.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
 return \[
 {
 url: 'https://example.com',
 lastModified: '2021\-01\-01',
 changeFrequency: 'weekly',
 priority: 0\.5,
 images: \['https://example.com/image.jpg'],
 },
 ]
}
\`\`\`
Output:

acme.com/sitemap.xml\`\`\`
\
\
 \
 \https://example.com\
 \
 \https://example.com/image.jpg\
 \
 \2021\-01\-01\
 \weekly\
 \0\.5\
 \
\
\`\`\`
### [Video Sitemaps](#video-sitemaps)

You can use `videos` property to create video sitemaps. Learn more details in the [Google Developer Docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps).

app/sitemap.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
 return \[
 {
 url: 'https://example.com',
 lastModified: '2021\-01\-01',
 changeFrequency: 'weekly',
 priority: 0\.5,
 videos: \[
 {
 title: 'example',
 thumbnail\_loc: 'https://example.com/image.jpg',
 description: 'this is the description',
 },
 ],
 },
 ]
}
\`\`\`
Output:

acme.com/sitemap.xml\`\`\`
\
\
 \
 \https://example.com\
 \
 \example\
 \https://example.com/image.jpg\
 \this is the description\
 \
 \2021\-01\-01\
 \weekly\
 \0\.5\
 \
\
\`\`\`
### [Generate a localized Sitemap](#generate-a-localized-sitemap)

app/sitemap.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
 return \[
 {
 url: 'https://acme.com',
 lastModified: new Date(),
 alternates: {
 languages: {
 es: 'https://acme.com/es',
 de: 'https://acme.com/de',
 },
 },
 },
 {
 url: 'https://acme.com/about',
 lastModified: new Date(),
 alternates: {
 languages: {
 es: 'https://acme.com/es/about',
 de: 'https://acme.com/de/about',
 },
 },
 },
 {
 url: 'https://acme.com/blog',
 lastModified: new Date(),
 alternates: {
 languages: {
 es: 'https://acme.com/es/blog',
 de: 'https://acme.com/de/blog',
 },
 },
 },
 ]
}
\`\`\`

Output:

acme.com/sitemap.xml\`\`\`
\
 \
 \https://acme.com\
 \
 \
 \2023\-04\-06T15:02:24\.021Z\
 \
 \
 \https://acme.com/about\
 \
 \
 \2023\-04\-06T15:02:24\.021Z\
 \
 \
 \https://acme.com/blog\
 \
 \
 \2023\-04\-06T15:02:24\.021Z\
 \
\
\`\`\`
### [Generating multiple sitemaps](#generating-multiple-sitemaps)

While a single sitemap will work for most applications. For large web applications, you may need to split a sitemap into multiple files.

There are two ways you can create multiple sitemaps:

* By nesting `sitemap.(xml|js|ts)` inside multiple route segments e.g. `app/sitemap.xml` and `app/products/sitemap.xml`.
* By using the [`generateSitemaps`](/docs/app/api-reference/functions/generate-sitemaps) function.

For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.

app/product/sitemap.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'
import { BASE\_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
 // Fetch the total number of products and calculate the number of sitemaps needed
 return \[{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap({
 id,
}: {
 id: number
}): Promise\ {
 // Google's limit is 50,000 URLs per sitemap
 const start = id \* 50000
 const end = start \+ 50000
 const products = await getProducts(
 \`SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}\`
 )
 return products.map((product) =\> ({
 url: \`${BASE\_URL}/product/${product.id}\`,
 lastModified: product.date,
 }))
}
\`\`\`

Your generated sitemaps will be available at `/.../sitemap/[id]`. For example, `/product/sitemap/1.xml`.

See the [`generateSitemaps` API reference](/docs/app/api-reference/functions/generate-sitemaps) for more information.

## [Returns](#returns)

The default function exported from `sitemap.(xml|ts|js)` should return an array of objects with the following properties:

\`\`\`
type Sitemap = Array\
 }
}\>
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v14.2.0` | Add localizations support. |
| `v13.4.14` | Add `changeFrequency` and `priority` attributes to sitemaps. |
| `v13.3.0` | `sitemap` introduced. |

## Next Steps

Learn how to use the generateSitemaps function.[### generateSitemaps

Learn how to use the generateSiteMaps function to create multiple sitemaps for your application.](/docs/app/api-reference/functions/generate-sitemaps)Was this helpful?



## Components: <Script> | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/components/script)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Components](/docs/app/api-reference/components)\# \

This API reference will help you understand how to use [props](#props) available for the Script Component. For features and usage, please see the [Optimizing Scripts](/docs/app/building-your-application/optimizing/scripts) page.

app/dashboard/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Script from 'next/script'

export default function Dashboard() {
 return (
 \
 \
 \
 )
}
\`\`\`

## [Props](#props)

Here's a summary of the props available for the Script Component:

| Prop | Example | Type | Required |
| --- | --- | --- | --- |
| [`src`](#src) | `src="http://example.com/script"` | String | Required unless inline script is used |
| [`strategy`](#strategy) | `strategy="lazyOnload"` | String | \- |
| [`onLoad`](#onload) | `onLoad={onLoadFunc}` | Function | \- |
| [`onReady`](#onready) | `onReady={onReadyFunc}` | Function | \- |
| [`onError`](#onerror) | `onError={onErrorFunc}` | Function | \- |

## [Required Props](#required-props)

The `` component requires the following properties.

### [`src`](#src)

A path string specifying the URL of an external script. This can be either an absolute external URL or an internal path. The `src` property is required unless an inline script is used.

## [Optional Props](#optional-props)

The `` component accepts a number of additional properties beyond those which are required.

### [`strategy`](#strategy)

The loading strategy of the script. There are four different strategies that can be used:

* `beforeInteractive`: Load before any Next.js code and before any page hydration occurs.
* `afterInteractive`: (**default**) Load early but after some hydration on the page occurs.
* `lazyOnload`: Load during browser idle time.
* `worker`: (experimental) Load in a web worker.

### [`beforeInteractive`](#beforeinteractive)

Scripts that load with the `beforeInteractive` strategy are injected into the initial HTML from the server, downloaded before any Next.js module, and executed in the order they are placed before *any* hydration occurs on the page.

Scripts denoted with this strategy are preloaded and fetched before any first\-party code, but their execution does not block page hydration from occurring.

`beforeInteractive` scripts must be placed inside the root layout (`app/layout.tsx`) and are designed to load scripts that are needed by the entire site (i.e. the script will load when any page in the application has been loaded server\-side).

**This strategy should only be used for critical scripts that need to be fetched before any part of the page becomes interactive.**

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Script from 'next/script'

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \
 {children}
 \
 \
 \
 )
}
\`\`\`

> **Good to know**: Scripts with `beforeInteractive` will always be injected inside the `head` of the HTML document regardless of where it's placed in the component.

Some examples of scripts that should be loaded as soon as possible with `beforeInteractive` include:

* Bot detectors
* Cookie consent managers

### [`afterInteractive`](#afterinteractive)

Scripts that use the `afterInteractive` strategy are injected into the HTML client\-side and will load after some (or all) hydration occurs on the page. **This is the default strategy** of the Script component and should be used for any script that needs to load as soon as possible but not before any first\-party Next.js code.

`afterInteractive` scripts can be placed inside of any page or layout and will only load and execute when that page (or group of pages) is opened in the browser.

app/page.js\`\`\`
import Script from 'next/script'

export default function Page() {
 return (
 \
 \
 \
 )
}
\`\`\`
Some examples of scripts that are good candidates for `afterInteractive` include:

* Tag managers
* Analytics

### [`lazyOnload`](#lazyonload)

Scripts that use the `lazyOnload` strategy are injected into the HTML client\-side during browser idle time and will load after all resources on the page have been fetched. This strategy should be used for any background or low priority scripts that do not need to load early.

`lazyOnload` scripts can be placed inside of any page or layout and will only load and execute when that page (or group of pages) is opened in the browser.

app/page.js\`\`\`
import Script from 'next/script'

export default function Page() {
 return (
 \
 \
 \
 )
}
\`\`\`
Examples of scripts that do not need to load immediately and can be fetched with `lazyOnload` include:

* Chat support plugins
* Social media widgets

### [`worker`](#worker)

> **Warning:** The `worker` strategy is not yet stable and does not yet work with the App Router. Use with caution.

Scripts that use the `worker` strategy are off\-loaded to a web worker in order to free up the main thread and ensure that only critical, first\-party resources are processed on it. While this strategy can be used for any script, it is an advanced use case that is not guaranteed to support all third\-party scripts.

To use `worker` as a strategy, the `nextScriptWorkers` flag must be enabled in `next.config.js`:

next.config.js\`\`\`
module.exports = {
 experimental: {
 nextScriptWorkers: true,
 },
}
\`\`\`
`worker` scripts can **only currently be used in the `pages/` directory**:

pages/home.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Script from 'next/script'

export default function Home() {
 return (
 \
 \
 \
 )
}
\`\`\`

### [`onLoad`](#onload)

> **Warning:** `onLoad` does not yet work with Server Components and can only be used in Client Components. Further, `onLoad` can't be used with `beforeInteractive` – consider using `onReady` instead.

Some third\-party scripts require users to run JavaScript code once after the script has finished loading in order to instantiate content or call a function. If you are loading a script with either `afterInteractive` or `lazyOnload` as a loading strategy, you can execute code after it has loaded using the `onLoad` property.

Here's an example of executing a lodash method only after the library has been loaded.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import Script from 'next/script'

export default function Page() {
 return (
 \
 \ {
 console.log(\_.sample(\[1, 2, 3, 4]))
 }}
 /\>
 \
 )
}
\`\`\`

### [`onReady`](#onready)

> **Warning:** `onReady` does not yet work with Server Components and can only be used in Client Components.

Some third\-party scripts require users to run JavaScript code after the script has finished loading and every time the component is mounted (after a route navigation for example). You can execute code after the script's load event when it first loads and then after every subsequent component re\-mount using the `onReady` property.

Here's an example of how to re\-instantiate a Google Maps JS embed every time the component is mounted:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useRef } from 'react'
import Script from 'next/script'

export default function Page() {
 const mapRef = useRef()

 return (
 \
 \\
 \ {
 new google.maps.Map(mapRef.current, {
 center: { lat: \-34\.397, lng: 150\.644 },
 zoom: 8,
 })
 }}
 /\>
 \
 )
}
\`\`\`

### [`onError`](#onerror)

> **Warning:** `onError` does not yet work with Server Components and can only be used in Client Components. `onError` cannot be used with the `beforeInteractive` loading strategy.

Sometimes it is helpful to catch when a script fails to load. These errors can be handled with the `onError` property:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import Script from 'next/script'

export default function Page() {
 return (
 \
 \ {
 console.error('Script failed to load', e)
 }}
 /\>
 \
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `beforeInteractive` and `afterInteractive` is modified to support `app`. |
| `v12.2.4` | `onReady` prop added. |
| `v12.2.2` | Allow `next/script` with `beforeInteractive` to be placed in `_document`. |
| `v11.0.0` | `next/script` introduced. |

Was this helpful?



## Functions: after | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/after)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)after# after

`after` allows you to schedule work to be executed after a response (or prerender) is finished. This is useful for tasks and other side effects that should not block the response, such as logging and analytics.

It can be used in [Server Components](/docs/app/building-your-application/rendering/server-components) (including [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)), [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations), [Route Handlers](/docs/app/building-your-application/routing/route-handlers), and [Middleware](/docs/app/building-your-application/routing/middleware).

The function accepts a callback that will be executed after the response (or prerender) is finished:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { after } from 'next/server'
// Custom logging function
import { log } from '@/app/utils'

export default function Layout({ children }: { children: React.ReactNode }) {
 after(() =\> {
 // Execute after the layout is rendered and sent to the user
 log()
 })
 return \{children}\
}
\`\`\`

> **Good to know:** `after` is not a [Dynamic API](/docs/app/building-your-application/rendering/server-components#dynamic-apis) and calling it does not cause a route to become dynamic. If it's used within a static page, the callback will execute at build time, or whenever a page is revalidated.

## [Reference](#reference)

### [Parameters](#parameters)

* A callback function which will be executed after the response (or prerender) is finished.

### [Duration](#duration)

`after` will run for the platform's default or configured max duration of your route. If your platform supports it, you can configure the timeout limit using the [`maxDuration`](/docs/app/api-reference/file-conventions/route-segment-config#maxduration) route segment config.

## [Good to know](#good-to-know)

* `after` will be executed even if the response didn't complete successfully. Including when an error is thrown or when `notFound` or `redirect` is called.
* You can use React `cache` to deduplicate functions called inside `after`.
* `after` can be nested inside other `after` calls, for example, you can create utility functions that wrap `after` calls to add additional functionality.

## [Alternatives](#alternatives)

The use case for `after` is to process secondary tasks without blocking the primary response. It's similar to using the platform's [`waitUntil()`](https://vercel.com/docs/functions/functions-api-reference) or removing `await` from a promise, but with the following differences:

* **`waitUntil()`**: accepts a promise and enqueues a task to be executed during the lifecycle of the request, whereas `after` accepts a callback that will be executed **after** the response is finished.
* **Removing `await`**: starts executing during the response, which uses resources. It's also not reliable in serverless environments as the function stops computation immediately after the response is sent, potentially interrupting the task.

We recommend using `after` as it has been designed to consider other Next.js APIs and contexts.

## [Examples](#examples)

### [With request APIs](#with-request-apis)

You can use request APIs such as [`cookies`](/docs/app/api-reference/functions/cookies) and [`headers`](/docs/app/api-reference/functions/headers) inside `after` in [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) and [Route Handlers](/docs/app/api-reference/file-conventions/route). This is useful for logging activity after a mutation. For example:

app/api/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'

export async function POST(request: Request) {
 // Perform mutation
 // ...

 // Log user activity for analytics
 after(async () =\> {
 const userAgent = (await headers().get('user\-agent')) \|\| 'unknown'
 const sessionCookie =
 (await cookies().get('session\-id'))?.value \|\| 'anonymous'

 logUserAction({ sessionCookie, userAgent })
 })

 return new Response(JSON.stringify({ status: 'success' }), {
 status: 200,
 headers: { 'Content\-Type': 'application/json' },
 })
}
\`\`\`

However, you cannot use these request APIs inside `after` in [Server Components](/docs/app/building-your-application/rendering/server-components). This is because Next.js needs to know which part of the tree access the request APIs to support [Partial Prerendering](/docs/app/building-your-application/rendering/partial-prerendering), but `after` runs after React's rendering lifecycle.

| Version History | Description |
| --- | --- |
| `v15.1.0` | `after` became stable. |
| `v15.0.0-rc` | `unstable_after` introduced. |

Was this helpful?



## Components: <Link> | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/components/link)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Components](/docs/app/api-reference/components)\# \

`` is a React component that extends the HTML `` element to provide [prefetching](/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching) and client\-side navigation between routes. It is the primary way to navigate between routes in Next.js.

Basic usage:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page() {
 return \Dashboard\
}
\`\`\`

## [Reference](#reference)

The following props can be passed to the `` component:

| Prop | Example | Type | Required |
| --- | --- | --- | --- |
| [`href`](#href-required) | `href="/dashboard"` | String or Object | Yes |
| [`replace`](#replace) | `replace={false}` | Boolean | \- |
| [`scroll`](#scroll) | `scroll={false}` | Boolean | \- |
| [`prefetch`](#prefetch) | `prefetch={false}` | Boolean or null | \- |

> **Good to know**: `` tag attributes such as `className` or `target="_blank"` can be added to `` as props and will be passed to the underlying `` element.

### [`href` (required)](#href-required)

The path or URL to navigate to.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

// Navigate to /about?name=test
export default function Page() {
 return (
 \
 About
 \
 )
}
\`\`\`

### [`replace`](#replace)

**Defaults to `false`.** When `true`, `next/link` will replace the current history state instead of adding a new URL into the [browser's history](https://developer.mozilla.org/docs/Web/API/History_API) stack.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page() {
 return (
 \
 Dashboard
 \
 )
}
\`\`\`

### [`scroll`](#scroll)

**Defaults to `true`.** The default scrolling behavior of `` in Next.js **is to maintain scroll position**, similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](/docs/app/api-reference/file-conventions/page), scroll position will stay the same as long as the Page is visible in the viewport. However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element.

When `scroll = {false}`, Next.js will not attempt to scroll to the first Page element.

> **Good to know**: Next.js checks if `scroll: false` before managing scroll behavior. If scrolling is enabled, it identifies the relevant DOM node for navigation and inspects each top\-level element. All non\-scrollable elements and those without rendered HTML are bypassed, this includes sticky or fixed positioned elements, and non\-visible elements such as those calculated with `getBoundingClientRect`. Next.js then continues through siblings until it identifies a scrollable element that is visible in the viewport.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page() {
 return (
 \
 Dashboard
 \
 )
}
\`\`\`

### [`prefetch`](#prefetch)

Prefetching happens when a `` component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the `href`) and its data in the background to improve the performance of client\-side navigations. If the prefetched data has expired by the time the user hovers over a ``, Next.js will attempt to prefetch it again. **Prefetching is only enabled in production**.

The following values can be passed to the `prefetch` prop:

* **`null` (default)**: Prefetch behavior depends on whether the route is static or dynamic. For static routes, the full route will be prefetched (including all its data). For dynamic routes, the partial route down to the nearest segment with a [`loading.js`](/docs/app/building-your-application/routing/loading-ui-and-streaming#instant-loading-states) boundary will be prefetched.
* `true`: The full route will be prefetched for both static and dynamic routes.
* `false`: Prefetching will never happen both on entering the viewport and on hover.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page() {
 return (
 \
 Dashboard
 \
 )
}
\`\`\`

## [Examples](#examples)

The following examples demonstrate how to use the `` component in different scenarios.

### [Linking to dynamic segments](#linking-to-dynamic-segments)

When linking to [dynamic segments](/docs/app/building-your-application/routing/dynamic-routes), you can use [template literals and interpolation](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Template_literals) to generate a list of links. For example, to generate a list of blog posts:

app/blog/post\-list.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

interface Post {
 id: number
 title: string
 slug: string
}

export default function PostList({ posts }: { posts: Post\[] }) {
 return (
 \
 {posts.map((post) =\> (
 \
 \{post.title}\
 \
 ))}
 \
 )
}
\`\`\`### [Checking active links](#checking-active-links)

You can use [`usePathname()`](/docs/app/api-reference/functions/use-pathname) to determine if a link is active. For example, to add a class to the active link, you can check if the current `pathname` matches the `href` of the link:

app/ui/nav\-links.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function Links() {
 const pathname = usePathname()

 return (
 \
 \
 Home
 \

 \
 About
 \
 \
 )
}
\`\`\`### [Scrolling to an `id`](#scrolling-to-an-id)

If you'd like to scroll to a specific `id` on navigation, you can append your URL with a `#` hash link or just pass a hash link to the `href` prop. This is possible since `` renders to an `` element.

\`\`\`
\Settings\

// Output
\Settings\
\`\`\`
> **Good to know**:
> 
> 
> * Next.js will scroll to the [Page](/docs/app/api-reference/file-conventions/page) if it is not visible in the viewport upon navigation.

### [Linking to dynamic route segments](#linking-to-dynamic-route-segments)

For [dynamic route segments](/docs/app/building-your-application/routing/dynamic-routes), it can be handy to use template literals to create the link's path.

For example, you can generate a list of links to the dynamic route `app/blog/[slug]/page.js`:

app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page({ posts }) {
 return (
 \
 {posts.map((post) =\> (
 \
 \{post.title}\
 \
 ))}
 \
 )
}
\`\`\`
### [If the child is a custom component that wraps an `` tag](#if-the-child-is-a-custom-component-that-wraps-an-a-tag)

If the child of `Link` is a custom component that wraps an `` tag, you must add `passHref` to `Link`. This is necessary if you’re using libraries like [styled\-components](https://styled-components.com/). Without this, the `` tag will not have the `href` attribute, which hurts your site's accessibility and might affect SEO. If you're using [ESLint](/docs/pages/api-reference/config/eslint), there is a built\-in rule `next/link-passhref` to ensure correct usage of `passHref`.

components/nav\-link.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'
import styled from 'styled\-components'

// This creates a custom component that wraps an \ tag
const RedLink = styled.a\`
 color: red;
\`

function NavLink({ href, name }) {
 return (
 \
 \{name}\
 \
 )
}

export default NavLink
\`\`\`

* If you’re using [emotion](https://emotion.sh/)’s JSX pragma feature (`@jsx jsx`), you must use `passHref` even if you use an `` tag directly.
* The component should support `onClick` property to trigger navigation correctly.

### [Nesting a functional component](#nesting-a-functional-component)

If the child of `Link` is a functional component, in addition to using `passHref` and `legacyBehavior`, you must wrap the component in [`React.forwardRef`](https://react.dev/reference/react/forwardRef):

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'
import React from 'react'

// Define the props type for MyButton
interface MyButtonProps {
 onClick?: React.MouseEventHandler\
 href?: string
}

// Use React.ForwardRefRenderFunction to properly type the forwarded ref
const MyButton: React.ForwardRefRenderFunction\ = ({ onClick, href }, ref) =\> {
 return (
 \
 Click Me
 \
 )
}

// Use React.forwardRef to wrap the component
const ForwardedMyButton = React.forwardRef(MyButton)

export default function Page() {
 return (
 \
 \
 \
 )
}
\`\`\`

### [Replace the URL instead of push](#replace-the-url-instead-of-push)

The default behavior of the `Link` component is to `push` a new URL into the `history` stack. You can use the `replace` prop to prevent adding a new entry, as in the following example:

app/page.jsTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page() {
 return (
 \
 About us
 \
 )
}
\`\`\`

### [Disable scrolling to the top of the page](#disable-scrolling-to-the-top-of-the-page)

The default scrolling behavior of `` in Next.js **is to maintain scroll position**, similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](/docs/app/api-reference/file-conventions/page), scroll position will stay the same as long as the Page is visible in the viewport.

However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element. If you'd like to disable this behavior, you can pass `scroll={false}` to the `` component, or `scroll: false` to `router.push()` or `router.replace()`.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Page() {
 return (
 \
 Disables scrolling to the top
 \
 )
}
\`\`\`Using `router.push()` or `router.replace()`:

\`\`\`
// useRouter
import { useRouter } from 'next/navigation'

const router = useRouter()

router.push('/dashboard', { scroll: false })
\`\`\`

### [Prefetching links in Middleware](#prefetching-links-in-middleware)

It's common to use [Middleware](/docs/app/building-your-application/routing/middleware) for authentication or other purposes that involve rewriting the user to a different page. In order for the `` component to properly prefetch links with rewrites via Middleware, you need to tell Next.js both the URL to display and the URL to prefetch. This is required to avoid un\-necessary fetches to middleware to know the correct route to prefetch.

For example, if you want to serve a `/dashboard` route that has authenticated and visitor views, you can add the following in your Middleware to redirect the user to the correct page:

middleware.tsTypeScriptJavaScriptTypeScript\`\`\`
import { NextResponse } from 'next/server'

export function middleware(request: Request) {
 const nextUrl = request.nextUrl
 if (nextUrl.pathname === '/dashboard') {
 if (request.cookies.authToken) {
 return NextResponse.rewrite(new URL('/auth/dashboard', request.url))
 } else {
 return NextResponse.rewrite(new URL('/public/dashboard', request.url))
 }
 }
}
\`\`\`

In this case, you would want to use the following code in your `` component:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Page() {
 const isAuthed = useIsAuthed()
 const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
 return (
 \
 Dashboard
 \
 )
}
\`\`\`

## [Version history](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | No longer requires a child `` tag. A [codemod](/docs/app/building-your-application/upgrading/codemods#remove-a-tags-from-link-components) is provided to automatically update your codebase. |
| `v10.0.0` | `href` props pointing to a dynamic route are automatically resolved and no longer require an `as` prop. |
| `v8.0.0` | Improved prefetching performance. |
| `v1.0.0` | `next/link` introduced. |

Was this helpful?



## Functions: useSelectedLayoutSegments | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)useSelectedLayoutSegments# useSelectedLayoutSegments

`useSelectedLayoutSegments` is a **Client Component** hook that lets you read the active route segments **below** the Layout it is called from.

It is useful for creating UI in parent Layouts that need knowledge of active child segments such as breadcrumbs.

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useSelectedLayoutSegments } from 'next/navigation'

export default function ExampleClientComponent() {
 const segments = useSelectedLayoutSegments()

 return (
 \
 {segments.map((segment, index) =\> (
 \{segment}\
 ))}
 \
 )
}
\`\`\`

> **Good to know**:
> 
> 
> * Since `useSelectedLayoutSegments` is a [Client Component](/docs/app/building-your-application/rendering/client-components) hook, and Layouts are [Server Components](/docs/app/building-your-application/rendering/server-components) by default, `useSelectedLayoutSegments` is usually called via a Client Component that is imported into a Layout.
> * The returned segments include [Route Groups](/docs/app/building-your-application/routing/route-groups), which you might not want to be included in your UI. You can use the `filter()` array method to remove items that start with a bracket.

## [Parameters](#parameters)

\`\`\`
const segments = useSelectedLayoutSegments(parallelRoutesKey?: string)
\`\`\`
`useSelectedLayoutSegments` *optionally* accepts a [`parallelRoutesKey`](/docs/app/building-your-application/routing/parallel-routes#useselectedlayoutsegments), which allows you to read the active route segment within that slot.

## [Returns](#returns)

`useSelectedLayoutSegments` returns an array of strings containing the active segments one level down from the layout the hook was called from. Or an empty array if none exist.

For example, given the Layouts and URLs below, the returned segments would be:

| Layout | Visited URL | Returned Segments |
| --- | --- | --- |
| `app/layout.js` | `/` | `[]` |
| `app/layout.js` | `/dashboard` | `['dashboard']` |
| `app/layout.js` | `/dashboard/settings` | `['dashboard', 'settings']` |
| `app/dashboard/layout.js` | `/dashboard` | `[]` |
| `app/dashboard/layout.js` | `/dashboard/settings` | `['settings']` |

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `useSelectedLayoutSegments` introduced. |

Was this helpful?



## Directives: use server | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/directives/use-server)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Directives](/docs/app/api-reference/directives)use server# use server

The `use server` directive designates a function or file to be executed on the **server side**. It can be used at the top of a file to indicate that all functions in the file are server\-side, or inline at the top of a function to mark the function as a [Server Function](https://19.react.dev/reference/rsc/server-functions). This is a React feature.

## [Using `use server` at the top of a file](#using-use-server-at-the-top-of-a-file)

The following example shows a file with a `use server` directive at the top. All functions in the file are executed on the server.

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'
import { db } from '@/lib/db' // Your database client

export async function createUser(data: { name: string; email: string }) {
 const user = await db.user.create({ data })
 return user
}
\`\`\`

### [Using Server Functions in a Client Component](#using-server-functions-in-a-client-component)

To use Server Functions in Client Components you need to create your Server Functions in a dedicated file using the `use server` directive at the top of the file. These Server Functions can then be imported into Client and Server Components and executed.

Assuming you have a `fetchUsers` Server Function in `actions.ts`:

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'
import { db } from '@/lib/db' // Your database client

export async function fetchUsers() {
 const users = await db.user.findMany()
 return users
}
\`\`\`

Then you can import the `fetchUsers` Server Function into a Client Component and execute it on the client\-side.

app/components/my\-button.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'
import { fetchUsers } from '../actions'

export default function MyButton() {
 return \ fetchUsers()}\>Fetch Users\
}
\`\`\`

## [Using `use server` inline](#using-use-server-inline)

In the following example, `use server` is used inline at the top of a function to mark it as a [Server Function](https://19.react.dev/reference/rsc/server-functions):

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { db } from '@/lib/db' // Your database client

export default function UserList() {
 async function fetchUsers() {
 'use server'
 const users = await db.user.findMany()
 return users
 }

 return \ fetchUsers()}\>Fetch Users\
}
\`\`\`

## [Security considerations](#security-considerations)

When using the `use server` directive, it's important to ensure that all server\-side logic is secure and that sensitive data remains protected.

### [Authentication and authorization](#authentication-and-authorization)

Always authenticate and authorize users before performing sensitive server\-side operations.

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { db } from '@/lib/db' // Your database client
import { authenticate } from '@/lib/auth' // Your authentication library

export async function createUser(
 data: { name: string; email: string },
 token: string
) {
 const user = authenticate(token)
 if (!user) {
 throw new Error('Unauthorized')
 }
 const newUser = await db.user.create({ data })
 return newUser
}
\`\`\`

## [Reference](#reference)

See the [React documentation](https://react.dev/reference/rsc/use-server) for more information on `use server`.

Was this helpful?



## File Conventions: page.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/page)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)page.js# page.js

The `page` file allows you to define UI that is **unique** to a route. You can create a page by default exporting a component from the file:

app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Page({
 params,
 searchParams,
}: {
 params: Promise\
 searchParams: Promise\
}) {
 return \My Page\
}
\`\`\`

## [Good to know](#good-to-know)

* The `.js`, `.jsx`, or `.tsx` file extensions can be used for `page`.
* A `page` is always the **leaf** of the route subtree.
* A `page` file is required to make a route segment **publicly accessible**.
* Pages are [Server Components](https://react.dev/reference/rsc/server-components) by default, but can be set to a [Client Component](https://react.dev/reference/rsc/use-client).

## [Reference](#reference)

### [Props](#props)

#### [`params` (optional)](#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) from the root segment down to that page.

app/shop/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page({
 params,
}: {
 params: Promise\
}) {
 const slug = (await params).slug
}
\`\`\`

| Example Route | URL | `params` |
| --- | --- | --- |
| `app/shop/[slug]/page.js` | `/shop/1` | `Promise` |
| `app/shop/[category]/[item]/page.js` | `/shop/1/2` | `Promise` |
| `app/shop/[...slug]/page.js` | `/shop/1/2` | `Promise` |

* Since the `params` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
	+ In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.

#### [`searchParams` (optional)](#searchparams-optional)

A promise that resolves to an object containing the [search parameters](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters) of the current URL. For example:

app/shop/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page({
 searchParams,
}: {
 searchParams: Promise\
}) {
 const filters = (await searchParams).filters
}
\`\`\`

| Example URL | `searchParams` |
| --- | --- |
| `/shop?a=1` | `Promise` |
| `/shop?a=1&b=2` | `Promise` |
| `/shop?a=1&a=2` | `Promise` |

* Since the `searchParams` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
	+ In version 14 and earlier, `searchParams` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* `searchParams` is a **[Dynamic API](/docs/app/building-your-application/rendering/server-components#server-rendering-strategies#dynamic-apis)** whose values cannot be known ahead of time. Using it will opt the page into **[dynamic rendering](/docs/app/building-your-application/rendering/server-components#dynamic-rendering)** at request time.
* `searchParams` is a plain JavaScript object, not a `URLSearchParams` instance.

## [Examples](#examples)

### [Displaying content based on `params`](#displaying-content-based-on-params)

Using [dynamic route segments](/docs/app/building-your-application/routing/dynamic-routes), you can display or fetch specific content for the page based on the `params` prop.

app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page({
 params,
}: {
 params: Promise\
}) {
 const { slug } = await params
 return \Blog Post: {slug}\
}
\`\`\`

### [Handling filtering with `searchParams`](#handling-filtering-with-searchparams)

You can use the `searchParams` prop to handle filtering, pagination, or sorting based on the query string of the URL.

app/shop/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page({
 searchParams,
}: {
 searchParams: Promise\
}) {
 const { page = '1', sort = 'asc', query = '' } = await searchParams

 return (
 \
 \Product Listing\
 \Search query: {query}\
 \Current page: {page}\
 \Sort order: {sort}\
 \
 )
}
\`\`\`

### [Reading `searchParams` and `params` in Client Components](#reading-searchparams-and-params-in-client-components)

To use `searchParams` and `params` in a Client Component (which cannot be `async`), you can use React's [`use`](https://react.dev/reference/react/use) function to read the promise:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { use } from 'react'

export default function Page({
 params,
 searchParams,
}: {
 params: Promise\
 searchParams: Promise\
}) {
 const { slug } = use(params)
 const { query } = use(searchParams)
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `params` and `searchParams` are now promises. A [codemod](/docs/app/building-your-application/upgrading/codemods#150) is available. |
| `v13.0.0` | `page` introduced. |

Was this helpful?



## Functions: notFound | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/not-found)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)notFound# notFound

The `notFound` function allows you to render the [`not-found file`](/docs/app/api-reference/file-conventions/not-found) within a route segment as well as inject a `` tag.

## [`notFound()`](#notfound)

Invoking the `notFound()` function throws a `NEXT_NOT_FOUND` error and terminates rendering of the route segment in which it was thrown. Specifying a [**not\-found** file](/docs/app/api-reference/file-conventions/not-found) allows you to gracefully handle such errors by rendering a Not Found UI within the segment.

app/user/\[id]/page.js\`\`\`
import { notFound } from 'next/navigation'

async function fetchUser(id) {
 const res = await fetch('https://...')
 if (!res.ok) return undefined
 return res.json()
}

export default async function Profile({ params }) {
 const user = await fetchUser(params.id)

 if (!user) {
 notFound()
 }

 // ...
}
\`\`\`

> **Good to know**: `notFound()` does not require you to use `return notFound()` due to using the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `notFound` introduced. |

Was this helpful?



## File Conventions: Metadata Files | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)Metadata Files# Metadata Files API Reference

This section of the docs covers **Metadata file conventions**. File\-based metadata can be defined by adding special metadata files to route segments.

Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).

Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.

> **Good to know**:
> 
> 
> * Special Route Handlers like [`sitemap.ts`](/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image), and [`icon.tsx`](/docs/app/api-reference/file-conventions/metadata/app-icons), and other [metadata files](/docs/app/api-reference/file-conventions/metadata) are cached by default.
> * If using along with [`middleware.ts`](/docs/app/api-reference/file-conventions/middleware), [configure the matcher](/docs/app/building-your-application/routing/middleware#matcher) to exclude the metadata files.

[### favicon, icon, and apple\-icon

API Reference for the Favicon, Icon and Apple Icon file conventions.](/docs/app/api-reference/file-conventions/metadata/app-icons)[### manifest.json

API Reference for manifest.json file.](/docs/app/api-reference/file-conventions/metadata/manifest)[### opengraph\-image and twitter\-image

API Reference for the Open Graph Image and Twitter Image file conventions.](/docs/app/api-reference/file-conventions/metadata/opengraph-image)[### robots.txt

API Reference for robots.txt file.](/docs/app/api-reference/file-conventions/metadata/robots)[### sitemap.xml

API Reference for the sitemap.xml file.](/docs/app/api-reference/file-conventions/metadata/sitemap)Was this helpful?



## Functions: generateImageMetadata | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)generateImageMetadata# generateImageMetadata

You can use `generateImageMetadata` to generate different versions of one image or return multiple images for one route segment. This is useful for when you want to avoid hard\-coding metadata values, such as for icons.

## [Parameters](#parameters)

`generateImageMetadata` function accepts the following parameters:

#### [`params` (optional)](#params-optional)

An object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) object from the root segment down to the segment `generateImageMetadata` is called from.

icon.tsxTypeScriptJavaScriptTypeScript\`\`\`
export function generateImageMetadata({
 params,
}: {
 params: { slug: string }
}) {
 // ...
}
\`\`\`

| Route | URL | `params` |
| --- | --- | --- |
| `app/shop/icon.js` | `/shop` | `undefined` |
| `app/shop/[slug]/icon.js` | `/shop/1` | `{ slug: '1' }` |
| `app/shop/[tag]/[item]/icon.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |

## [Returns](#returns)

The `generateImageMetadata` function should return an `array` of objects containing the image's metadata such as `alt` and `size`. In addition, each item **must** include an `id` value which will be passed to the props of the image generating function.

| Image Metadata Object | Type |
| --- | --- |
| `id` | `string` (required) |
| `alt` | `string` |
| `size` | `{ width: number; height: number }` |
| `contentType` | `string` |

icon.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'

export function generateImageMetadata() {
 return \[
 {
 contentType: 'image/png',
 size: { width: 48, height: 48 },
 id: 'small',
 },
 {
 contentType: 'image/png',
 size: { width: 72, height: 72 },
 id: 'medium',
 },
 ]
}

export default function Icon({ id }: { id: string }) {
 return new ImageResponse(
 (
 \
 Icon {id}
 \
 )
 )
}
\`\`\`

### [Examples](#examples)

#### [Using external data](#using-external-data)

This example uses the `params` object and external data to generate multiple [Open Graph images](/docs/app/api-reference/file-conventions/metadata/opengraph-image) for a route segment.

app/products/\[id]/opengraph\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'
import { getCaptionForImage, getOGImages } from '@/app/utils/images'

export async function generateImageMetadata({
 params,
}: {
 params: { id: string }
}) {
 const images = await getOGImages(params.id)

 return images.map((image, idx) =\> ({
 id: idx,
 size: { width: 1200, height: 600 },
 alt: image.text,
 contentType: 'image/png',
 }))
}

export default async function Image({
 params,
 id,
}: {
 params: { id: string }
 id: number
}) {
 const productId = (await params).id
 const imageId = id
 const text = await getCaptionForImage(productId, imageId)

 return new ImageResponse(
 (
 \
 {text}
 \
 )
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `generateImageMetadata` introduced. |

## Next Steps

View all the Metadata API options.[### Metadata Files

API documentation for the metadata file conventions.](/docs/app/api-reference/file-conventions/metadata)[### Metadata

Use the Metadata API to define metadata in any layout or page.](/docs/app/building-your-application/optimizing/metadata)Was this helpful?



## Functions: headers | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/headers)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)headers# headers

`headers` is an **async** function that allows you to **read** the HTTP incoming request headers from a [Server Component](/docs/app/building-your-application/rendering/server-components).

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { headers } from 'next/headers'

export default async function Page() {
 const headersList = await headers()
 const userAgent = headersList.get('user\-agent')
}
\`\`\`

## [Reference](#reference)

### [Parameters](#parameters)

`headers` does not take any parameters.

### [Returns](#returns)

`headers` returns a **read\-only** [Web Headers](https://developer.mozilla.org/docs/Web/API/Headers) object.

* [`Headers.entries()`](https://developer.mozilla.org/docs/Web/API/Headers/entries): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing to go through all key/value pairs contained in this object.
* [`Headers.forEach()`](https://developer.mozilla.org/docs/Web/API/Headers/forEach): Executes a provided function once for each key/value pair in this `Headers` object.
* [`Headers.get()`](https://developer.mozilla.org/docs/Web/API/Headers/get): Returns a [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) sequence of all the values of a header within a `Headers` object with a given name.
* [`Headers.has()`](https://developer.mozilla.org/docs/Web/API/Headers/has): Returns a boolean stating whether a `Headers` object contains a certain header.
* [`Headers.keys()`](https://developer.mozilla.org/docs/Web/API/Headers/keys): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all keys of the key/value pairs contained in this object.
* [`Headers.values()`](https://developer.mozilla.org/docs/Web/API/Headers/values): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all values of the key/value pairs contained in this object.

## [Good to know](#good-to-know)

* `headers` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
	+ In version 14 and earlier, `headers` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* Since `headers` is read\-only, you cannot `set` or `delete` the outgoing request headers.
* `headers` is a [Dynamic API](/docs/app/building-your-application/rendering/server-components#server-rendering-strategies#dynamic-apis) whose returned values cannot be known ahead of time. Using it in will opt a route into **[dynamic rendering](/docs/app/building-your-application/rendering/server-components#dynamic-rendering)**.

## [Examples](#examples)

### [Using the Authorization header](#using-the-authorization-header)

app/page.js\`\`\`
import { headers } from 'next/headers'

export default async function Page() {
 const authorization = (await headers()).get('authorization')
 const res = await fetch('...', {
 headers: { authorization }, // Forward the authorization header
 })
 const user = await res.json()

 return \{user.name}\
}
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `headers` is now an async function. A [codemod](/docs/app/building-your-application/upgrading/codemods#150) is available. |
| `v13.0.0` | `headers` introduced. |

Was this helpful?



## Functions: NextResponse | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/next-response)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)NextResponse# NextResponse

NextResponse extends the [Web Response API](https://developer.mozilla.org/docs/Web/API/Response) with additional convenience methods.

## [`cookies`](#cookies)

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the response.

### [`set(name, value)`](#setname-value)

Given a name, set a cookie with the given value on the response.

\`\`\`
// Given incoming request /home
let response = NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show\-banner', 'false')
// Response will have a \`Set\-Cookie:show\-banner=false;path=/home\` header
return response
\`\`\`
### [`get(name)`](#getname)

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

\`\`\`
// Given incoming request /home
let response = NextResponse.next()
// { name: 'show\-banner', value: 'false', Path: '/home' }
response.cookies.get('show\-banner')
\`\`\`
### [`getAll()`](#getall)

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.

\`\`\`
// Given incoming request /home
let response = NextResponse.next()
// \[
// { name: 'experiments', value: 'new\-pricing\-page', Path: '/home' },
// { name: 'experiments', value: 'winter\-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
\`\`\`
### [`delete(name)`](#deletename)

Given a cookie name, delete the cookie from the response.

\`\`\`
// Given incoming request /home
let response = NextResponse.next()
// Returns true for deleted, false is nothing is deleted
response.cookies.delete('experiments')
\`\`\`
## [`json()`](#json)

Produce a response with the given JSON body.

app/api/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { NextResponse } from 'next/server'

export async function GET(request: Request) {
 return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
\`\`\`

## [`redirect()`](#redirect)

Produce a response that redirects to a [URL](https://developer.mozilla.org/docs/Web/API/URL).

\`\`\`
import { NextResponse } from 'next/server'

return NextResponse.redirect(new URL('/new', request.url))
\`\`\`
The [URL](https://developer.mozilla.org/docs/Web/API/URL) can be created and modified before being used in the `NextResponse.redirect()` method. For example, you can use the `request.nextUrl` property to get the current URL, and then modify it to redirect to a different URL.

\`\`\`
import { NextResponse } from 'next/server'

// Given an incoming request...
const loginUrl = new URL('/login', request.url)
// Add ?from=/incoming\-url to the /login URL
loginUrl.searchParams.set('from', request.nextUrl.pathname)
// And redirect to the new URL
return NextResponse.redirect(loginUrl)
\`\`\`
## [`rewrite()`](#rewrite)

Produce a response that rewrites (proxies) the given [URL](https://developer.mozilla.org/docs/Web/API/URL) while preserving the original URL.

\`\`\`
import { NextResponse } from 'next/server'

// Incoming request: /about, browser shows /about
// Rewritten request: /proxy, browser shows /about
return NextResponse.rewrite(new URL('/proxy', request.url))
\`\`\`
## [`next()`](#next)

The `next()` method is useful for Middleware, as it allows you to return early and continue routing.

\`\`\`
import { NextResponse } from 'next/server'

return NextResponse.next()
\`\`\`
You can also forward `headers` when producing the response:

\`\`\`
import { NextResponse } from 'next/server'

// Given an incoming request...
const newHeaders = new Headers(request.headers)
// Add a new header
newHeaders.set('x\-version', '123')
// And produce a response with the new headers
return NextResponse.next({
 request: {
 // New request headers
 headers: newHeaders,
 },
})
\`\`\`Was this helpful?



## File Conventions: error.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/error)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)error.js# error.js

An **error** file allows you to handle unexpected runtime errors and display fallback UI.


app/dashboard/error.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({
 error,
 reset,
}: {
 error: Error \& { digest?: string }
 reset: () =\> void
}) {
 useEffect(() =\> {
 // Log the error to an error reporting service
 console.error(error)
 }, \[error])

 return (
 \
 \Something went wrong!\
 \ reset()
 }
 \>
 Try again
 \
 \
 )
}
\`\`\`

## [How `error.js` Works](#how-errorjs-works)

`error.js` wraps a route segment and its nested children in a [React Error Boundary](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary). When an error throws within the boundary, the `error` component shows as the fallback UI.



> **Good to know**:
> 
> 
> * The [React DevTools](https://react.dev/learn/react-developer-tools) allow you to toggle error boundaries to test error states.

## [Props](#props)

### [`error`](#error)

An instance of an [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error) object forwarded to the `error.js` Client Component.

> **Good to know:** During development, the `Error` object forwarded to the client will be serialized and include the `message` of the original error for easier debugging. However, **this behavior is different in production** to avoid leaking potentially sensitive details included in the error to the client.

#### [`error.message`](#errormessage)

* Errors forwarded from Client Components show the original `Error` message.
* Errors forwarded from Server Components show a generic message with an identifier. This is to prevent leaking sensitive details. You can use the identifier, under `errors.digest`, to match the corresponding server\-side logs.

#### [`error.digest`](#errordigest)

An automatically generated hash of the error thrown. It can be used to match the corresponding error in server\-side logs.

### [`reset`](#reset)

The cause of an error can sometimes be temporary. In these cases, trying again might resolve the issue.

An error component can use the `reset()` function to prompt the user to attempt to recover from the error. When executed, the function will try to re\-render the error boundary's contents. If successful, the fallback error component is replaced with the result of the re\-render.

app/dashboard/error.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client' // Error boundaries must be Client Components

export default function Error({
 error,
 reset,
}: {
 error: Error \& { digest?: string }
 reset: () =\> void
}) {
 return (
 \
 \Something went wrong!\
 \ reset()}\>Try again\
 \
 )
}
\`\`\`

## [`global-error.js`](#global-errorjs)

While less common, you can handle errors in the root layout or template using `app/global-error.js`, located in the root app directory, even when leveraging [internationalization](/docs/app/building-your-application/routing/internationalization). Global error UI must define its own `` and `` tags. This file replaces the root layout or template when active.

app/global\-error.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client' // Error boundaries must be Client Components

export default function GlobalError({
 error,
 reset,
}: {
 error: Error \& { digest?: string }
 reset: () =\> void
}) {
 return (
 // global\-error must include html and body tags
 \
 \
 \Something went wrong!\
 \ reset()}\>Try again\
 \
 \
 )
}
\`\`\`

> **Good to know**:
> 
> 
> * `global-error.js` is only enabled in production. In development, our error overlay will show instead.

## [not\-found.js](#not-foundjs)

The [`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) file shows UI when calling the `notFound()` function within a route segment.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.1.0` | `global-error` introduced. |
| `v13.0.0` | `error` introduced. |

## Learn more about error handling

[### Error Handling

Learn how to display expected errors and handle uncaught exceptions.](/docs/app/building-your-application/routing/error-handling)Was this helpful?



## Functions: generateStaticParams | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)generateStaticParams# generateStaticParams

The `generateStaticParams` function can be used in combination with [dynamic route segments](/docs/app/building-your-application/routing/dynamic-routes) to [**statically generate**](/docs/app/building-your-application/rendering/server-components#static-rendering-default) routes at build time instead of on\-demand at request time.

app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
// Return a list of \`params\` to populate the \[slug] dynamic segment
export async function generateStaticParams() {
 const posts = await fetch('https://.../posts').then((res) =\> res.json())

 return posts.map((post) =\> ({
 slug: post.slug,
 }))
}

// Multiple versions of this page will be statically generated
// using the \`params\` returned by \`generateStaticParams\`
export default async function Page({
 params,
}: {
 params: Promise\
}) {
 const { slug } = await params
 // ...
}
\`\`\`

> **Good to know**:
> 
> 
> * You can use the [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) segment config option to control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
> * You must return [an empty array from `generateStaticParams`](#all-paths-at-build-time) or utilize [`export const dynamic = 'force-static'`](/docs/app/api-reference/file-conventions/route-segment-config#dynamic) in order to revalidate (ISR) [paths at runtime](#all-paths-at-runtime).
> * During `next dev`, `generateStaticParams` will be called when you navigate to a route.
> * During `next build`, `generateStaticParams` runs before the corresponding Layouts or Pages are generated.
> * During revalidation (ISR), `generateStaticParams` will not be called again.
> * `generateStaticParams` replaces the [`getStaticPaths`](/docs/pages/api-reference/functions/get-static-paths) function in the Pages Router.

## [Parameters](#parameters)

`options.params` (optional)

If multiple dynamic segments in a route use `generateStaticParams`, the child `generateStaticParams` function is executed once for each set of `params` the parent generates.

The `params` object contains the populated `params` from the parent `generateStaticParams`, which can be used to [generate the `params` in a child segment](#multiple-dynamic-segments-in-a-route).

## [Returns](#returns)

`generateStaticParams` should return an array of objects where each object represents the populated dynamic segments of a single route.

* Each property in the object is a dynamic segment to be filled in for the route.
* The properties name is the segment's name, and the properties value is what that segment should be filled in with.

| Example Route | `generateStaticParams` Return Type |
| --- | --- |
| `/product/[id]` | `{ id: string }[]` |
| `/products/[category]/[product]` | `{ category: string, product: string }[]` |
| `/products/[...slug]` | `{ slug: string[] }[]` |

## [Single Dynamic Segment](#single-dynamic-segment)

app/product/\[id]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export function generateStaticParams() {
 return \[{ id: '1' }, { id: '2' }, { id: '3' }]
}

// Three versions of this page will be statically generated
// using the \`params\` returned by \`generateStaticParams\`
// \- /product/1
// \- /product/2
// \- /product/3
export default async function Page({
 params,
}: {
 params: Promise\
}) {
 const { id } = await params
 // ...
}
\`\`\`

## [Multiple Dynamic Segments](#multiple-dynamic-segments)

app/products/\[category]/\[product]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export function generateStaticParams() {
 return \[
 { category: 'a', product: '1' },
 { category: 'b', product: '2' },
 { category: 'c', product: '3' },
 ]
}

// Three versions of this page will be statically generated
// using the \`params\` returned by \`generateStaticParams\`
// \- /products/a/1
// \- /products/b/2
// \- /products/c/3
export default async function Page({
 params,
}: {
 params: Promise\
}) {
 const { category, product } = await params
 // ...
}
\`\`\`

## [Catch\-all Dynamic Segment](#catch-all-dynamic-segment)

app/product/\[...slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export function generateStaticParams() {
 return \[{ slug: \['a', '1'] }, { slug: \['b', '2'] }, { slug: \['c', '3'] }]
}

// Three versions of this page will be statically generated
// using the \`params\` returned by \`generateStaticParams\`
// \- /product/a/1
// \- /product/b/2
// \- /product/c/3
export default async function Page({
 params,
}: {
 params: Promise\
}) {
 const { slug } = await params
 // ...
}
\`\`\`

## [Examples](#examples)

### [Static Rendering](#static-rendering)

#### [All paths at build time](#all-paths-at-build-time)

To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:

app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export async function generateStaticParams() {
 const posts = await fetch('https://.../posts').then((res) =\> res.json())

 return posts.map((post) =\> ({
 slug: post.slug,
 }))
}
\`\`\`

#### [Subset of paths at build time](#subset-of-paths-at-build-time)

To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:

app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export async function generateStaticParams() {
 const posts = await fetch('https://.../posts').then((res) =\> res.json())

 // Render the first 10 posts at build time
 return posts.slice(0, 10\).map((post) =\> ({
 slug: post.slug,
 }))
}
\`\`\`

Then, by using the [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) segment config option, you can control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.

app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
// All posts besides the top 10 will be a 404
export const dynamicParams = false

export async function generateStaticParams() {
 const posts = await fetch('https://.../posts').then((res) =\> res.json())
 const topPosts = posts.slice(0, 10\)

 return topPosts.map((post) =\> ({
 slug: post.slug,
 }))
}
\`\`\`

#### [All paths at runtime](#all-paths-at-runtime)

To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize [`export const dynamic = 'force-static'`](/docs/app/api-reference/file-conventions/route-segment-config#dynamic):

app/blog/\[slug]/page.js\`\`\`
export async function generateStaticParams() {
 return \[]
}
\`\`\`

> **Good to know:** You must always return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.

app/changelog/\[slug]/page.js\`\`\`
export const dynamic = 'force\-static'
\`\`\`
### [Disable rendering for unspecified paths](#disable-rendering-for-unspecified-paths)

To prevent unspecified paths from being statically rendered at runtime, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and unspecified routes will 404 or match (in the case of [catch\-all routes](/docs/app/building-your-application/routing/dynamic-routes#catch-all-segments)).

### [Multiple Dynamic Segments in a Route](#multiple-dynamic-segments-in-a-route)

You can generate params for dynamic segments above the current layout or page, but **not below**. For example, given the `app/products/[category]/[product]` route:

* `app/products/[category]/[product]/page.js` can generate params for **both** `[category]` and `[product]`.
* `app/products/[category]/layout.js` can **only** generate params for `[category]`.

There are two approaches to generating params for a route with multiple dynamic segments:

#### [Generate params from the bottom up](#generate-params-from-the-bottom-up)

Generate multiple dynamic segments from the child route segment.

app/products/\[category]/\[product]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
// Generate segments for both \[category] and \[product]
export async function generateStaticParams() {
 const products = await fetch('https://.../products').then((res) =\> res.json())

 return products.map((product) =\> ({
 category: product.category.slug,
 product: product.id,
 }))
}

export default function Page({
 params,
}: {
 params: Promise\
}) {
 // ...
}
\`\`\`

#### [Generate params from the top down](#generate-params-from-the-top-down)

Generate the parent segments first and use the result to generate the child segments.

app/products/\[category]/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
// Generate segments for \[category]
export async function generateStaticParams() {
 const products = await fetch('https://.../products').then((res) =\> res.json())

 return products.map((product) =\> ({
 category: product.category.slug,
 }))
}

export default function Layout({
 params,
}: {
 params: Promise\
}) {
 // ...
}
\`\`\`

A child route segment's `generateStaticParams` function is executed once for each segment a parent `generateStaticParams` generates.

The child `generateStaticParams` function can use the `params` returned from the parent `generateStaticParams` function to dynamically generate its own segments.

app/products/\[category]/\[product]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
// Generate segments for \[product] using the \`params\` passed from
// the parent segment's \`generateStaticParams\` function
export async function generateStaticParams({
 params: { category },
}: {
 params: { category: string }
}) {
 const products = await fetch(
 \`https://.../products?category=${category}\`
 ).then((res) =\> res.json())

 return products.map((product) =\> ({
 product: product.id,
 }))
}

export default function Page({
 params,
}: {
 params: Promise\
}) {
 // ...
}
\`\`\`

> **Good to know**: `fetch` requests are automatically [memoized](/docs/app/building-your-application/caching#request-memoization) for the same data across all `generate`\-prefixed functions, Layouts, Pages, and Server Components. React [`cache` can be used](/docs/app/building-your-application/caching#react-cache-function) if `fetch` is unavailable.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `generateStaticParams` introduced. |

Was this helpful?



## Components: <Form> | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/components/form)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Components](/docs/app/api-reference/components)\# \

The `` component extends the HTML `` element to provide [**prefetching**](/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching) of [loading UI](/docs/app/building-your-application/routing/loading-ui-and-streaming), **client\-side navigation** on submission, and **progressive enhancement**.

It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.

Basic usage:

/app/ui/search.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Form from 'next/form'

export default function Page() {
 return (
 \
 {/\* On submission, the input value will be appended to 
 the URL, e.g. /search?query=abc \*/}
 \
 \Submit\
 \
 )
}
\`\`\`

## [Reference](#reference)

The behavior of the `` component depends on whether the `action` prop is passed a `string` or `function`.

* When `action` is a **string**, the `` behaves like a native HTML form that uses a **`GET`** method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
	+ [Prefetches](/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching) the path when the form becomes visible, this preloads shared UI (e.g. `layout.js` and `loading.js`), resulting in faster navigation.
	+ Performs a [client\-side navigation](/docs/app/building-your-application/routing/linking-and-navigating#5-soft-navigation) instead of a full page reload when the form is submitted. This retains shared UI and client\-side state.
* When `action` is a **function** (Server Action), `` behaves like a [React form](https://react.dev/reference/react-dom/components/form), executing the action when the form is submitted.

### [`action` (string) Props](#action-string-props)

When `action` is a string, the `` component supports the following props:

| Prop | Example | Type | Required |
| --- | --- | --- | --- |
| `action` | `action="/search"` | `string` (URL or relative path) | Yes |
| `replace` | `replace={false}` | `boolean` | \- |
| `scroll` | `scroll={true}` | `boolean` | \- |
| `prefetch` | `prefetch={true}` | `boolean` | \- |

* **`action`**: The URL or path to navigate to when the form is submitted.
	+ An empty string `""` will navigate to the same route with updated search params.
* **`replace`**: Replaces the current history state instead of pushing a new one to the [browser's history](https://developer.mozilla.org/en-US/docs/Web/API/History_API) stack. Default is `false`.
* **`scroll`**: Controls the scroll behavior during navigation. Defaults to `true`, this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.
* **`prefetch`**: Controls whether the path should be prefetched when the form becomes visible in the user's viewport. Defaults to `true`.

### [`action` (function) Props](#action-function-props)

When `action` is a function, the `` component supports the following prop:

| Prop | Example | Type | Required |
| --- | --- | --- | --- |
| `action` | `action={myAction}` | `function` (Server Action) | Yes |

* **`action`**: The Server Action to be called when the form is submitted. See the [React docs](https://react.dev/reference/react-dom/components/form#props) for more.

> **Good to know**: When `action` is a function, the `replace` and `scroll` props are ignored.

### [Caveats](#caveats)

* **`formAction`**: Can be used in a `` or `` fields to override the `action` prop. Next.js will perform a client\-side navigation, however, this approach doesn't support prefetching.
	+ When using [`basePath`](/docs/app/api-reference/config/next-config-js/basePath), you must also include it in the `formAction` path. e.g. `formAction="/base-path/search"`.
* **`key`**: Passing a `key` prop to a string `action` is not supported. If you'd like to trigger a re\-render or perform a mutation, consider using a function `action` instead.

* **`onSubmit`**: Can be used to handle form submission logic. However, calling `event.preventDefault()` will override `` behavior such as navigating to the specified URL.
* **[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method), [`encType`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype), [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#target)**: Are not supported as they override `` behavior.
	+ Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
	+ If you need to use these props, use the HTML `` element instead.
* **``**: Using this input type when the `action` is a string will match browser behavior by submitting the filename instead of the file object.

## [Examples](#examples)

### [Search form that leads to a search result page](#search-form-that-leads-to-a-search-result-page)

You can create a search form that navigates to a search results page by passing the path as an `action`:

/app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Form from 'next/form'

export default function Page() {
 return (
 \
 \
 \Submit\
 \
 )
}
\`\`\`When the user updates the query input field and submits the form, the form data will be encoded into the URL as search params, e.g. `/search?query=abc`.

> **Good to know**: If you pass an empty string `""` to `action`, the form will navigate to the same route with updated search params.

On the results page, you can access the query using the [`searchParams`](/docs/app/api-reference/file-conventions/page#searchparams-optional) `page.js` prop and use it to fetch data from an external source.

/app/search/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { getSearchResults } from '@/lib/search'

export default async function SearchPage({
 searchParams,
}: {
 searchParams: { \[key: string]: string \| string\[] \| undefined }
}) {
 const results = await getSearchResults(searchParams.query)

 return \...\
}
\`\`\`When the `` becomes visible in the user's viewport, shared UI (such as `layout.js` and `loading.js`) on the `/search` page will be prefetched. On submission, the form will immediately navigate to the new route and show loading UI while the results are being fetched. You can design the fallback UI using [`loading.js`](/docs/app/api-reference/file-conventions/loading):

/app/search/loading.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Loading() {
 return \Loading...\
}
\`\`\`To cover cases when shared UI hasn't yet loaded, you can show instant feedback to the user using [`useFormStatus`](https://react.dev/reference/react-dom/hooks/useFormStatus).

First, create a component that displays a loading state when the form is pending:

/app/ui/search\-button.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'
import { useFormStatus } from 'react\-dom'

export default function SearchButton() {
 const status = useFormStatus()
 return (
 \{status.pending ? 'Searching...' : 'Search'}\
 )
}
\`\`\`Then, update the search form page to use the `SearchButton` component:

/app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Form from 'next/form'
import { SearchButton } from '@/ui/search\-button'

export default function Page() {
 return (
 \
 \
 \
 \
 )
}
\`\`\`### [Mutations with Server Actions](#mutations-with-server-actions)

You can perform mutations by passing a function to the `action` prop.

/app/posts/create/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Form from 'next/form'
import { createPost } from '@/posts/actions'

export default function Page() {
 return (
 \
 \
 {/\* ... \*/}
 \Create Post\
 \
 )
}
\`\`\`After a mutation, it's common to redirect to the new resource. You can use the [`redirect`](/docs/app/building-your-application/routing/redirecting) function from `next/navigation` to navigate to the new post page.

> **Good to know**: Since the "destination" of the form submission is not known until the action is executed, `` cannot automatically prefetch shared UI.

/app/posts/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
 // Create a new post
 // ...

 // Redirect to the new post
 redirect(\`/posts/${data.id}\`)
}
\`\`\`Then, in the new page, you can fetch data using the `params` prop:

/app/posts/\[id]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { getPost } from '@/posts/data'

export default async function PostPage({
 params,
}: {
 params: Promise\
}) {
 const data = await getPost((await params).id)

 return (
 \
 \{data.title}\
 {/\* ... \*/}
 \
 )
}
\`\`\`See the [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) docs for more examples.

Was this helpful?



## Functions: ImageResponse | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/image-response)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)ImageResponse# ImageResponse

The `ImageResponse` constructor allows you to generate dynamic images using JSX and CSS. This is useful for generating social media images such as Open Graph images, Twitter cards, and more.

The following options are available for `ImageResponse`:

\`\`\`
import { ImageResponse } from 'next/og'

new ImageResponse(
 element: ReactElement,
 options: {
 width?: number = 1200
 height?: number = 630
 emoji?: 'twemoji' \| 'blobmoji' \| 'noto' \| 'openmoji' = 'twemoji',
 fonts?: {
 name: string,
 data: ArrayBuffer,
 weight: number,
 style: 'normal' \| 'italic'
 }\[]
 debug?: boolean = false

 // Options that will be passed to the HTTP response
 status?: number = 200
 statusText?: string
 headers?: Record\
 },
)
\`\`\`
## [Supported CSS Properties](#supported-css-properties)

Please refer to [Satori’s documentation](https://github.com/vercel/satori#css) for a list of supported HTML and CSS features.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v14.0.0` | `ImageResponse` moved from `next/server` to `next/og` |
| `v13.3.0` | `ImageResponse` can be imported from `next/server`. |
| `v13.0.0` | `ImageResponse` introduced via `@vercel/og` package. |

Was this helpful?



## Functions: generateSitemaps | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)generateSitemaps# generateSitemaps

You can use the `generateSitemaps` function to generate multiple sitemaps for your application.

## [Returns](#returns)

The `generateSitemaps` returns an array of objects with an `id` property.

## [URLs](#urls)

Your generated sitemaps will be available at `/.../sitemap/[id].xml`. For example, `/product/sitemap/1.xml`.

## [Example](#example)

For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.

app/product/sitemap.tsTypeScriptJavaScriptTypeScript\`\`\`
import { BASE\_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
 // Fetch the total number of products and calculate the number of sitemaps needed
 return \[{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap({
 id,
}: {
 id: number
}): Promise\ {
 // Google's limit is 50,000 URLs per sitemap
 const start = id \* 50000
 const end = start \+ 50000
 const products = await getProducts(
 \`SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}\`
 )
 return products.map((product) =\> ({
 url: \`${BASE\_URL}/product/${product.id}\`,
 lastModified: product.date,
 }))
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `generateSitemaps` now generates consistent URLs between development and production |
| `v13.3.2` | `generateSitemaps` introduced. In development, you can view the generated sitemap on `/.../sitemap.xml/[id]`. For example, `/product/sitemap.xml/1`. |

## Next Steps

Learn how to create sitemaps for your Next.js application.[### sitemap.xml

API Reference for the sitemap.xml file.](/docs/app/api-reference/file-conventions/metadata/sitemap)Was this helpful?



## Functions: usePathname | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-pathname)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)usePathname# usePathname

`usePathname` is a **Client Component** hook that lets you read the current URL's **pathname**.

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { usePathname } from 'next/navigation'

export default function ExampleClientComponent() {
 const pathname = usePathname()
 return \Current pathname: {pathname}\
}
\`\`\`

`usePathname` intentionally requires using a [Client Component](/docs/app/building-your-application/rendering/client-components). It's important to note Client Components are not a de\-optimization. They are an integral part of the [Server Components](/docs/app/building-your-application/rendering/server-components) architecture.

For example, a Client Component with `usePathname` will be rendered into HTML on the initial page load. When navigating to a new route, this component does not need to be re\-fetched. Instead, the component is downloaded once (in the client JavaScript bundle), and re\-renders based on the current state.

> **Good to know**:
> 
> 
> * Reading the current URL from a [Server Component](/docs/app/building-your-application/rendering/server-components) is not supported. This design is intentional to support layout state being preserved across page navigations.
> * Compatibility mode:
> 	+ `usePathname` can return `null` when a [fallback route](/docs/pages/api-reference/functions/get-static-paths#fallback-true) is being rendered or when a `pages` directory page has been [automatically statically optimized](/docs/pages/building-your-application/rendering/automatic-static-optimization) by Next.js and the router is not ready.
> 	+ When using `usePathname` with rewrites in [`next.config`](/docs/app/api-reference/config/next-config-js/rewrites) or [`Middleware`](/docs/app/building-your-application/routing/middleware), `useState` and `useEffect` must also be used in order to avoid hydration mismatch errors. See the [rewrites example](https://github.com/vercel/next.js/tree/canary/examples/rewrites) for more information.
> 	+ Next.js will automatically update your types if it detects both an `app` and `pages` directory in your project.

## [Parameters](#parameters)

\`\`\`
const pathname = usePathname()
\`\`\`
`usePathname` does not take any parameters.

## [Returns](#returns)

`usePathname` returns a string of the current URL's pathname. For example:

| URL | Returned value |
| --- | --- |
| `/` | `'/'` |
| `/dashboard` | `'/dashboard'` |
| `/dashboard?v=2` | `'/dashboard'` |
| `/blog/hello-world` | `'/blog/hello-world'` |

## [Examples](#examples)

### [Do something in response to a route change](#do-something-in-response-to-a-route-change)

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { usePathname, useSearchParams } from 'next/navigation'

function ExampleClientComponent() {
 const pathname = usePathname()
 const searchParams = useSearchParams()
 useEffect(() =\> {
 // Do something here...
 }, \[pathname, searchParams])
}
\`\`\`

| Version | Changes |
| --- | --- |
| `v13.0.0` | `usePathname` introduced. |

Was this helpful?



## App Router: API Reference | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[Introduction](/docs)[App Router](/docs/app)API Reference# API Reference

The Next.js API reference is divided into the following sections:

[### Directives

Directives are used to modify the behavior of your Next.js application.](/docs/app/api-reference/directives)[### Components

API Reference for Next.js built\-in components.](/docs/app/api-reference/components)[### File Conventions

API Reference for Next.js File Conventions.](/docs/app/api-reference/file-conventions)[### Functions

API Reference for Next.js Functions and Hooks.](/docs/app/api-reference/functions)[### Configuration

Learn how to configure Next.js applications.](/docs/app/api-reference/config)[### CLI

API Reference for the Next.js Command Line Interface (CLI) tools.](/docs/app/api-reference/cli)[### Edge Runtime

API Reference for the Edge Runtime.](/docs/app/api-reference/edge)[### Turbopack

Turbopack is an incremental bundler optimized for JavaScript and TypeScript, written in Rust, and built into Next.js.](/docs/app/api-reference/turbopack)Was this helpful?



## Functions: cacheTag | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/cacheTag)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)cacheTag# cacheTag

This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](/docs/app/building-your-application/upgrading/canary), and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The `cacheTag` function allows you to tag cached data for on\-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.

## [Usage](#usage)

To use `cacheTag`, enable the [`dynamicIO` flag](/docs/app/api-reference/config/next-config-js/dynamicIO) in your `next.config.js` file:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 experimental: {
 dynamicIO: true,
 },
}

export default nextConfig
\`\`\`

The `cacheTag` function takes a single string value, or a string array.

app/data.tsTypeScriptJavaScriptTypeScript\`\`\`
import { unstable\_cacheTag as cacheTag } from 'next/cache'

export async function getData() {
 'use cache'
 cacheTag('my\-data')
 const data = await fetch('/api/data')
 return data
}
\`\`\`

You can then purge the cache on\-demand using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) API in another function, for example, a [route handler](/docs/app/building-your-application/routing/route-handlers) or [Server Action](/docs/app/building-your-application/data-fetching/server-actions-and-mutations):

app/action.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
 await addPost()
 revalidateTag('my\-data')
}
\`\`\`

## [Good to know](#good-to-know)

* **Idempotent Tags**: Applying the same tag multiple times has no additional effect.
* **Multiple Tags**: You can assign multiple tags to a single cache entry by passing an array to `cacheTag`.

\`\`\`
cacheTag('tag\-one', 'tag\-two')
\`\`\`
## [Examples](#examples)

### [Tagging components or functions](#tagging-components-or-functions)

Tag your cached data by calling `cacheTag` within a cached function or component:

app/components/bookings.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { unstable\_cacheTag as cacheTag } from 'next/cache'

interface BookingsProps {
 type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
 'use cache'
 cacheTag('bookings\-data')

 async function getBookingsData() {
 const data = await fetch(\`/api/bookings?type=${encodeURIComponent(type)}\`)
 return data
 }

 return //...
}
\`\`\`

### [Creating tags from external data](#creating-tags-from-external-data)

You can use the data returned from an async function to tag the cache entry.

app/components/bookings.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { unstable\_cacheTag as cacheTag } from 'next/cache'

interface BookingsProps {
 type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
 async function getBookingsData() {
 'use cache'
 const data = await fetch(\`/api/bookings?type=${encodeURIComponent(type)}\`)
 cacheTag('bookings\-data', data.id)
 return data
 }
 return //...
}
\`\`\`

### [Invalidating tagged cache](#invalidating-tagged-cache)

Using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag), you can invalidate the cache for a specific tag when needed:

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { revalidateTag } from 'next/cache'

export async function updateBookings() {
 await updateBookingData()
 revalidateTag('bookings\-data')
}
\`\`\`
## Related

View related API references.[### dynamicIO

Learn how to enable the dynamicIO flag in Next.js.](/docs/app/api-reference/config/next-config-js/dynamicIO)[### use cache

Learn how to use the use cache directive to cache data in your Next.js application.](/docs/app/api-reference/directives/use-cache)[### revalidateTag

API Reference for the revalidateTag function.](/docs/app/api-reference/functions/revalidateTag)[### cacheLife

Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.](/docs/app/api-reference/functions/cacheLife)Was this helpful?



## Functions: generateViewport | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)generateViewport# generateViewport

You can customize the initial viewport of the page with the static `viewport` object or the dynamic `generateViewport` function.

> **Good to know**:
> 
> 
> * The `viewport` object and `generateViewport` function exports are **only supported in Server Components**.
> * You cannot export both the `viewport` object and `generateViewport` function from the same route segment.
> * If you're coming from migrating `metadata` exports, you can use [metadata\-to\-viewport\-export codemod](/docs/app/building-your-application/upgrading/codemods#metadata-to-viewport-export) to update your changes.

## [The `viewport` object](#the-viewport-object)

To define the viewport options, export a `viewport` object from a `layout.jsx` or `page.jsx` file.

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Viewport } from 'next'

export const viewport: Viewport = {
 themeColor: 'black',
}

export default function Page() {}
\`\`\`

## [`generateViewport` function](#generateviewport-function)

`generateViewport` should return a [`Viewport` object](#viewport-fields) containing one or more viewport fields.

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export function generateViewport({ params }) {
 return {
 themeColor: '...',
 }
}
\`\`\`

> **Good to know**:
> 
> 
> * If the viewport doesn't depend on runtime information, it should be defined using the static [`viewport` object](#the-viewport-object) rather than `generateViewport`.

## [Viewport Fields](#viewport-fields)

### [`themeColor`](#themecolor)

Learn more about [`theme-color`](https://developer.mozilla.org/docs/Web/HTML/Element/meta/name/theme-color).

**Simple theme color**

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Viewport } from 'next'

export const viewport: Viewport = {
 themeColor: 'black',
}
\`\`\`

\ output\`\`\`
\
\`\`\`
**With media attribute**

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Viewport } from 'next'

export const viewport: Viewport = {
 themeColor: \[
 { media: '(prefers\-color\-scheme: light)', color: 'cyan' },
 { media: '(prefers\-color\-scheme: dark)', color: 'black' },
 ],
}
\`\`\`

\ output\`\`\`
\
\
\`\`\`
### [`width`, `initialScale`, `maximumScale` and `userScalable`](#width-initialscale-maximumscale-and-userscalable)

> **Good to know**: The `viewport` meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Viewport } from 'next'

export const viewport: Viewport = {
 width: 'device\-width',
 initialScale: 1,
 maximumScale: 1,
 userScalable: false,
 // Also supported but less commonly used
 // interactiveWidget: 'resizes\-visual',
}
\`\`\`

\ output\`\`\`
\
\`\`\`
### [`colorScheme`](#colorscheme)

Learn more about [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta/name#:~:text=color%2Dscheme%3A%20specifies,of%20the%20following%3A).

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Viewport } from 'next'

export const viewport: Viewport = {
 colorScheme: 'dark',
}
\`\`\`

\ output\`\`\`
\
\`\`\`
## [Types](#types)

You can add type safety to your viewport object by using the `Viewport` type. If you are using the [built\-in TypeScript plugin](/docs/app/api-reference/config/typescript) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

### [`viewport` object](#viewport-object)

\`\`\`
import type { Viewport } from 'next'

export const viewport: Viewport = {
 themeColor: 'black',
}
\`\`\`
### [`generateViewport` function](#generateviewport-function-1)

#### [Regular function](#regular-function)

\`\`\`
import type { Viewport } from 'next'

export function generateViewport(): Viewport {
 return {
 themeColor: 'black',
 }
}
\`\`\`
#### [With segment props](#with-segment-props)

\`\`\`
import type { Viewport } from 'next'

type Props = {
 params: Promise\
 searchParams: Promise\
}

export function generateViewport({ params, searchParams }: Props): Viewport {
 return {
 themeColor: 'black',
 }
}

export default function Page({ params, searchParams }: Props) {}
\`\`\`
#### [JavaScript Projects](#javascript-projects)

For JavaScript projects, you can use JSDoc to add type safety.

\`\`\`
/\*\* @type {import("next").Viewport} \*/
export const viewport = {
 themeColor: 'black',
}
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v14.0.0` | `viewport` and `generateViewport` introduced. |

## Next Steps

View all the Metadata API options.[### Metadata Files

API documentation for the metadata file conventions.](/docs/app/api-reference/file-conventions/metadata)[### Metadata

Use the Metadata API to define metadata in any layout or page.](/docs/app/building-your-application/optimizing/metadata)Was this helpful?



## Functions: revalidateTag | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unstable_expireTag)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)revalidateTag# revalidateTag

`revalidateTag` allows you to purge [cached data](/docs/app/building-your-application/caching) on\-demand for a specific cache tag.

> **Good to know**:
> 
> 
> * `revalidateTag` is available in both [Node.js and Edge runtimes](/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes).
> * `revalidateTag` only invalidates the cache when the path is next visited. This means calling `revalidateTag` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.

## [Parameters](#parameters)

\`\`\`
revalidateTag(tag: string): void;
\`\`\`
* `tag`: A string representing the cache tag associated with the data you want to revalidate. Must be less than or equal to 256 characters. This value is case\-sensitive.

You can add tags to `fetch` as follows:

\`\`\`
fetch(url, { next: { tags: \[...] } });
\`\`\`
## [Returns](#returns)

`revalidateTag` does not return a value.

## [Examples](#examples)

### [Server Action](#server-action)

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
 await addPost()
 revalidateTag('posts')
}
\`\`\`

### [Route Handler](#route-handler)

app/api/revalidate/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextRequest } from 'next/server'
import { revalidateTag } from 'next/cache'

export async function GET(request: NextRequest) {
 const tag = request.nextUrl.searchParams.get('tag')
 revalidateTag(tag)
 return Response.json({ revalidated: true, now: Date.now() })
}
\`\`\`
Was this helpful?



## File Conventions: template.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/template)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)template.js# template.js

A **template** file is similar to a [layout](/docs/app/building-your-application/routing/layouts-and-templates#layouts) in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.

app/template.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Template({ children }: { children: React.ReactNode }) {
 return \{children}\
}
\`\`\`


While less common, you might choose to use a template over a layout if you want:

* Features that rely on `useEffect` (e.g logging page views) and `useState` (e.g a per\-page feedback form).
* To change the default framework behavior. For example, Suspense Boundaries inside layouts only show the fallback the first time the Layout is loaded and not when switching pages. For templates, the fallback is shown on each navigation.

## [Props](#props)

### [`children` (required)](#children-required)

Template accepts a `children` prop. For example:

Output\`\`\`
\
 {/\* Note that the template is automatically given a unique key. \*/}
 \{children}\
\
\`\`\`

> **Good to know**:
> 
> 
> * By default, `template` is a [Server Component](/docs/app/building-your-application/rendering/server-components), but can also be used as a [Client Component](/docs/app/building-your-application/rendering/client-components) through the `"use client"` directive.
> * When a user navigates between routes that share a `template`, a new instance of the component is mounted, DOM elements are recreated, state is **not** preserved in Client Components, and effects are re\-synchronized.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `template` introduced. |

Was this helpful?



## API Reference: Components | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/components)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)Components# Components

[### Font

Optimizing loading web fonts with the built\-in \`next/font\` loaders.](/docs/app/api-reference/components/font)[### \

Learn how to use the \`\\` component to handle form submissions and search params updates with client\-side navigation.](/docs/app/api-reference/components/form)[### \

Optimize Images in your Next.js Application using the built\-in \`next/image\` Component.](/docs/app/api-reference/components/image)[### \

Enable fast client\-side navigation with the built\-in \`next/link\` component.](/docs/app/api-reference/components/link)[### \

Optimize third\-party scripts in your Next.js application using the built\-in \`next/script\` Component.](/docs/app/api-reference/components/script)Was this helpful?



## File Conventions: loading.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/loading)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)loading.js# loading.js

A **loading** file can create instant loading states built on [Suspense](/docs/app/building-your-application/routing/loading-ui-and-streaming).

By default, this file is a [Server Component](/docs/app/building-your-application/rendering/server-components) \- but can also be used as a Client Component through the `"use client"` directive.

app/feed/loading.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Loading() {
 // Or a custom loading skeleton component
 return \Loading...\
}
\`\`\`

Loading UI components do not accept any parameters.

> **Good to know**:
> 
> 
> * While designing loading UI, you may find it helpful to use the [React Developer Tools](https://react.dev/learn/react-developer-tools) to manually toggle Suspense boundaries.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `loading` introduced. |

Was this helpful?



## Functions: useSearchParams | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-search-params)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)useSearchParams# useSearchParams

`useSearchParams` is a **Client Component** hook that lets you read the current URL's **query string**.

`useSearchParams` returns a **read\-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface.

app/dashboard/search\-bar.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
 const searchParams = useSearchParams()

 const search = searchParams.get('search')

 // URL \-\> \`/dashboard?search=my\-project\`
 // \`search\` \-\> 'my\-project'
 return \Search: {search}\
}
\`\`\`

## [Parameters](#parameters)

\`\`\`
const searchParams = useSearchParams()
\`\`\`
`useSearchParams` does not take any parameters.

## [Returns](#returns)

`useSearchParams` returns a **read\-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface, which includes utility methods for reading the URL's query string:

* [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): Returns the first value associated with the search parameter. For example:

| URL | `searchParams.get("a")` |
| --- | --- |
| `/dashboard?a=1` | `'1'` |
| `/dashboard?a=` | `''` |
| `/dashboard?b=3` | `null` |
| `/dashboard?a=1&a=2` | `'1'` *\- use [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll) to get all values* |
* [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): Returns a boolean value indicating if the given parameter exists. For example:

| URL | `searchParams.has("a")` |
| --- | --- |
| `/dashboard?a=1` | `true` |
| `/dashboard?b=3` | `false` |
* Learn more about other **read\-only** methods of [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams), including the [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), and [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString).

> **Good to know**:
> 
> 
> * `useSearchParams` is a [Client Component](/docs/app/building-your-application/rendering/client-components) hook and is **not supported** in [Server Components](/docs/app/building-your-application/rendering/server-components) to prevent stale values during [partial rendering](/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering).
> * If an application includes the `/pages` directory, `useSearchParams` will return `ReadonlyURLSearchParams | null`. The `null` value is for compatibility during migration since search params cannot be known during pre\-rendering of a page that doesn't use `getServerSideProps`

## [Behavior](#behavior)

### [Static Rendering](#static-rendering)

If a route is [statically rendered](/docs/app/building-your-application/rendering/server-components#static-rendering-default), calling `useSearchParams` will cause the Client Component tree up to the closest [`Suspense` boundary](/docs/app/building-your-application/routing/loading-ui-and-streaming#example) to be client\-side rendered.

This allows a part of the route to be statically rendered while the dynamic part that uses `useSearchParams` is client\-side rendered.

We recommend wrapping the Client Component that uses `useSearchParams` in a `` boundary. This will allow any Client Components above it to be statically rendered and sent as part of initial HTML. [Example](/docs/app/api-reference/functions/use-search-params#static-rendering).

For example:

app/dashboard/search\-bar.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
 const searchParams = useSearchParams()

 const search = searchParams.get('search')

 // This will not be logged on the server when using static rendering
 console.log(search)

 return \Search: {search}\
}
\`\`\`

app/dashboard/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { Suspense } from 'react'
import SearchBar from './search\-bar'

// This component passed as a fallback to the Suspense boundary
// will be rendered in place of the search bar in the initial HTML.
// When the value is available during React hydration the fallback
// will be replaced with the \`\\` component.
function SearchBarFallback() {
 return \placeholder\
}

export default function Page() {
 return (
 \
 \
 \}\>
 \
 \
 \
 \Dashboard\
 \
 )
}
\`\`\`

### [Dynamic Rendering](#dynamic-rendering)

If a route is [dynamically rendered](/docs/app/building-your-application/rendering/server-components#dynamic-rendering), `useSearchParams` will be available on the server during the initial server render of the Client Component.

For example:

app/dashboard/search\-bar.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
 const searchParams = useSearchParams()

 const search = searchParams.get('search')

 // This will be logged on the server during the initial render
 // and on the client on subsequent navigations.
 console.log(search)

 return \Search: {search}\
}
\`\`\`

app/dashboard/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import SearchBar from './search\-bar'

export const dynamic = 'force\-dynamic'

export default function Page() {
 return (
 \
 \
 \
 \
 \Dashboard\
 \
 )
}
\`\`\`

> **Good to know**: Setting the [`dynamic` route segment config option](/docs/app/api-reference/file-conventions/route-segment-config#dynamic) to `force-dynamic` can be used to force dynamic rendering.

### [Server Components](#server-components)

#### [Pages](#pages)

To access search params in [Pages](/docs/app/api-reference/file-conventions/page) (Server Components), use the [`searchParams`](/docs/app/api-reference/file-conventions/page#searchparams-optional) prop.

#### [Layouts](#layouts)

Unlike Pages, [Layouts](/docs/app/api-reference/file-conventions/layout) (Server Components) **do not** receive the `searchParams` prop. This is because a shared layout is [not re\-rendered during navigation](/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering) which could lead to stale `searchParams` between navigations. View [detailed explanation](/docs/app/api-reference/file-conventions/layout#layouts-do-not-receive-searchparams).

Instead, use the Page [`searchParams`](/docs/app/api-reference/file-conventions/page) prop or the [`useSearchParams`](/docs/app/api-reference/functions/use-search-params) hook in a Client Component, which is re\-rendered on the client with the latest `searchParams`.

## [Examples](#examples)

### [Updating `searchParams`](#updating-searchparams)

You can use [`useRouter`](/docs/app/api-reference/functions/use-router) or [`Link`](/docs/app/api-reference/components/link) to set new `searchParams`. After a navigation is performed, the current [`page.js`](/docs/app/api-reference/file-conventions/page) will receive an updated [`searchParams` prop](/docs/app/api-reference/file-conventions/page#searchparams-optional).

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

export default function ExampleClientComponent() {
 const router = useRouter()
 const pathname = usePathname()
 const searchParams = useSearchParams()

 // Get a new searchParams string by merging the current
 // searchParams with a provided key/value pair
 const createQueryString = useCallback(
 (name: string, value: string) =\> {
 const params = new URLSearchParams(searchParams.toString())
 params.set(name, value)

 return params.toString()
 },
 \[searchParams]
 )

 return (
 \
 \Sort By\

 {/\* using useRouter \*/}
 \ {
 // \?sort=asc
 router.push(pathname \+ '?' \+ createQueryString('sort', 'asc'))
 }}
 \>
 ASC
 \

 {/\* using \ \*/}
 \?sort=desc
 pathname \+ '?' \+ createQueryString('sort', 'desc')
 }
 \>
 DESC
 \
 \
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `useSearchParams` introduced. |

Was this helpful?



## Metadata Files: opengraph-image and twitter-image | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[File Conventions](/docs/app/api-reference/file-conventions)[Metadata Files](/docs/app/api-reference/file-conventions/metadata)opengraph\-image and twitter\-image# opengraph\-image and twitter\-image

The `opengraph-image` and `twitter-image` file conventions allow you to set Open Graph and Twitter images for a route segment.

They are useful for setting the images that appear on social networks and messaging apps when a user shares a link to your site.

There are two ways to set Open Graph and Twitter images:

* [Using image files (.jpg, .png, .gif)](#image-files-jpg-png-gif)
* [Using code to generate images (.js, .ts, .tsx)](#generate-images-using-code-js-ts-tsx)

## [Image files (.jpg, .png, .gif)](#image-files-jpg-png-gif)

Use an image file to set a route segment's shared image by placing an `opengraph-image` or `twitter-image` image file in the segment.

Next.js will evaluate the file and automatically add the appropriate tags to your app's `` element.

| File convention | Supported file types |
| --- | --- |
| [`opengraph-image`](#opengraph-image) | `.jpg`, `.jpeg`, `.png`, `.gif` |
| [`twitter-image`](#twitter-image) | `.jpg`, `.jpeg`, `.png`, `.gif` |
| [`opengraph-image.alt`](#opengraph-imagealttxt) | `.txt` |
| [`twitter-image.alt`](#twitter-imagealttxt) | `.txt` |

> **Good to know**:
> 
> 
> The `twitter-image` file size must not exceed [5MB](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary), and the `opengraph-image` file size must not exceed [8MB](https://developers.facebook.com/docs/sharing/webmasters/images). If the image file size exceeds these limits, the build will fail.

### [`opengraph-image`](#opengraph-image)

Add an `opengraph-image.(jpg|jpeg|png|gif)` image file to any route segment.

\ output\`\`\`
\" /\>
\" /\>
\" /\>
\" /\>
\`\`\`
### [`twitter-image`](#twitter-image)

Add a `twitter-image.(jpg|jpeg|png|gif)` image file to any route segment.

\ output\`\`\`
\" /\>
\" /\>
\" /\>
\" /\>
\`\`\`
### [`opengraph-image.alt.txt`](#opengraph-imagealttxt)

Add an accompanying `opengraph-image.alt.txt` file in the same route segment as the `opengraph-image.(jpg|jpeg|png|gif)` image it's alt text.

opengraph\-image.alt.txt\`\`\`
About Acme
\`\`\`
\ output\`\`\`
\
\`\`\`
### [`twitter-image.alt.txt`](#twitter-imagealttxt)

Add an accompanying `twitter-image.alt.txt` file in the same route segment as the `twitter-image.(jpg|jpeg|png|gif)` image it's alt text.

twitter\-image.alt.txt\`\`\`
About Acme
\`\`\`
\ output\`\`\`
\
\`\`\`
## [Generate images using code (.js, .ts, .tsx)](#generate-images-using-code-js-ts-tsx)

In addition to using [literal image files](#image-files-jpg-png-gif), you can programmatically **generate** images using code.

Generate a route segment's shared image by creating an `opengraph-image` or `twitter-image` route that default exports a function.

| File convention | Supported file types |
| --- | --- |
| `opengraph-image` | `.js`, `.ts`, `.tsx` |
| `twitter-image` | `.js`, `.ts`, `.tsx` |

> **Good to know**:
> 
> 
> * By default, generated images are [**statically optimized**](/docs/app/building-your-application/rendering/server-components#static-rendering-default) (generated at build time and cached) unless they use [Dynamic APIs](/docs/app/building-your-application/rendering/server-components#server-rendering-strategies#dynamic-apis) or uncached data.
> * You can generate multiple Images in the same file using [`generateImageMetadata`](/docs/app/api-reference/functions/generate-image-metadata).
> * `opengraph-image.js` and `twitter-image.js` are special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/building-your-application/caching#dynamic-apis) or [dynamic config](/docs/app/building-your-application/caching#segment-config-options) option.

The easiest way to generate an image is to use the [ImageResponse](/docs/app/api-reference/functions/image-response) API from `next/og`.

app/about/opengraph\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'

export const runtime = 'edge'

// Image metadata
export const alt = 'About Acme'
export const size = {
 width: 1200,
 height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image() {
 // Font
 const interSemiBold = fetch(
 new URL('./Inter\-SemiBold.ttf', import.meta.url)
 ).then((res) =\> res.arrayBuffer())

 return new ImageResponse(
 (
 // ImageResponse JSX element
 \
 About Acme
 \
 ),
 // ImageResponse options
 {
 // For convenience, we can re\-use the exported opengraph\-image
 // size config to also set the ImageResponse's width and height.
 ...size,
 fonts: \[
 {
 name: 'Inter',
 data: await interSemiBold,
 style: 'normal',
 weight: 400,
 },
 ],
 }
 )
}
\`\`\`

\ output\`\`\`
\" /\>
\
\
\
\
\`\`\`
### [Props](#props)

The default export function receives the following props:

#### [`params` (optional)](#params-optional)

An object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) object from the root segment down to the segment `opengraph-image` or `twitter-image` is colocated in.

app/shop/\[slug]/opengraph\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Image({ params }: { params: { slug: string } }) {
 // ...
}
\`\`\`

| Route | URL | `params` |
| --- | --- | --- |
| `app/shop/opengraph-image.js` | `/shop` | `undefined` |
| `app/shop/[slug]/opengraph-image.js` | `/shop/1` | `{ slug: '1' }` |
| `app/shop/[tag]/[item]/opengraph-image.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |

### [Returns](#returns)

The default export function should return a `Blob` \| `ArrayBuffer` \| `TypedArray` \| `DataView` \| `ReadableStream` \| `Response`.

> **Good to know**: `ImageResponse` satisfies this return type.

### [Config exports](#config-exports)

You can optionally configure the image's metadata by exporting `alt`, `size`, and `contentType` variables from `opengraph-image` or `twitter-image` route.

| Option | Type |
| --- | --- |
| [`alt`](#alt) | `string` |
| [`size`](#size) | `{ width: number; height: number }` |
| [`contentType`](#contenttype) | `string` \- [image MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types) |

#### [`alt`](#alt)

opengraph\-image.tsx \| twitter\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
export const alt = 'My images alt text'

export default function Image() {}
\`\`\`

\ output\`\`\`
\
\`\`\`
#### [`size`](#size)

opengraph\-image.tsx \| twitter\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
export const size = { width: 1200, height: 630 }

export default function Image() {}
\`\`\`

\ output\`\`\`
\
\
\`\`\`
#### [`contentType`](#contenttype)

opengraph\-image.tsx \| twitter\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
export const contentType = 'image/png'

export default function Image() {}
\`\`\`

\ output\`\`\`
\
\`\`\`
#### [Route Segment Config](#route-segment-config)

`opengraph-image` and `twitter-image` are specialized [Route Handlers](/docs/app/building-your-application/routing/route-handlers) that can use the same [route segment configuration](/docs/app/api-reference/file-conventions/route-segment-config) options as Pages and Layouts.

### [Examples](#examples)

#### [Using external data](#using-external-data)

This example uses the `params` object and external data to generate the image.

> **Good to know**:
> By default, this generated image will be [statically optimized](/docs/app/building-your-application/rendering/server-components#static-rendering-default). You can configure the individual `fetch` [`options`](/docs/app/api-reference/functions/fetch) or route segments [options](/docs/app/api-reference/file-conventions/route-segment-config#revalidate) to change this behavior.

app/posts/\[slug]/opengraph\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'

export const alt = 'About Acme'
export const size = {
 width: 1200,
 height: 630,
}
export const contentType = 'image/png'

export default async function Image({ params }: { params: { slug: string } }) {
 const post = await fetch(\`https://.../posts/${params.slug}\`).then((res) =\>
 res.json()
 )

 return new ImageResponse(
 (
 \
 {post.title}
 \
 ),
 {
 ...size,
 }
 )
}
\`\`\`

#### [Using Edge runtime with local assets](#using-edge-runtime-with-local-assets)

This example uses the Edge runtime to fetch a local image on the file system and passes it as an `ArrayBuffer` to the `src` attribute of an `` element. The local asset should be placed relative to the example source file location.

app/opengraph\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'

export const runtime = 'edge'

export default async function Image() {
 const logoSrc = await fetch(new URL('./logo.png', import.meta.url)).then(
 (res) =\> res.arrayBuffer()
 )

 return new ImageResponse(
 (
 \
 \
 \
 )
 )
}
\`\`\`

#### [Using Node.js runtime with local assets](#using-nodejs-runtime-with-local-assets)

This example uses the Node.js runtime to fetch a local image on the file system and passes it as an `ArrayBuffer` to the `src` attribute of an `` element. The local asset should be placed relative to the root of your project, rather than the location of the example source file.

app/opengraph\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
 const logoData = await readFile(join(process.cwd(), 'logo.png'))
 const logoSrc = Uint8Array.from(logoData).buffer

 return new ImageResponse(
 (
 \
 \
 \
 )
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `opengraph-image` and `twitter-image` introduced. |

Was this helpful?



## File Conventions: not-found.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)not\-found.js# not\-found.js

The **not\-found** file is used to render UI when the [`notFound`](/docs/app/api-reference/functions/not-found) function is thrown within a route segment. Along with serving a custom UI, Next.js will return a `200` HTTP status code for streamed responses, and `404` for non\-streamed responses.

app/not\-found.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function NotFound() {
 return (
 \
 \Not Found\
 \Could not find requested resource\
 \Return Home\
 \
 )
}
\`\`\`

## [Reference](#reference)

### [Props](#props)

`not-found.js` components do not accept any props.

> **Good to know**: In addition to catching expected `notFound()` errors, the root `app/not-found.js` file also handles any unmatched URLs for your whole application. This means users that visit a URL that is not handled by your app will be shown the UI exported by the `app/not-found.js` file.

## [Examples](#examples)

### [Data Fetching](#data-fetching)

By default, `not-found` is a Server Component. You can mark it as `async` to fetch and display data:

app/not\-found.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'
import { headers } from 'next/headers'

export default async function NotFound() {
 const headersList = await headers()
 const domain = headersList.get('host')
 const data = await getSiteData(domain)
 return (
 \
 \Not Found: {data.name}\
 \Could not find requested resource\
 \
 View \all posts\
 \
 \
 )
}
\`\`\`

If you need to use Client Component hooks like `usePathname` to display content based on the path, you must fetch data on the client\-side instead.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | Root `app/not-found` handles global unmatched URLs. |
| `v13.0.0` | `not-found` introduced. |

Was this helpful?



## Functions: cookies | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/cookies)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)cookies# cookies

`cookies` is an **async** function that allows you to read the HTTP incoming request cookies in [Server Component](/docs/app/building-your-application/rendering/server-components), and read/write outgoing request cookies in [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) or [Route Handlers](/docs/app/building-your-application/routing/route-handlers).

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { cookies } from 'next/headers'

export default async function Page() {
 const cookieStore = await cookies()
 const theme = cookieStore.get('theme')
 return '...'
}
\`\`\`

## [Reference](#reference)

### [Methods](#methods)

The following methods are available:

| Method | Return Type | Description |
| --- | --- | --- |
| `get('name')` | Object | Accepts a cookie name and returns an object with the name and value. |
| `getAll()` | Array of objects | Returns a list of all the cookies with a matching name. |
| `has('name')` | Boolean | Accepts a cookie name and returns a boolean based on if the cookie exists. |
| `set(name, value, options)` | \- | Accepts a cookie name, value, and options and sets the outgoing request cookie. |
| `delete(name)` | \- | Accepts a cookie name and deletes the cookie. |
| `clear()` | \- | Deletes all cookies. |
| `toString()` | String | Returns a string representation of the cookies. |

### [Options](#options)

When setting a cookie, the following properties from the `options` object are supported:

| Option | Type | Description |
| --- | --- | --- |
| `name` | String | Specifies the name of the cookie. |
| `value` | String | Specifies the value to be stored in the cookie. |
| `expires` | Date | Defines the exact date when the cookie will expire. |
| `maxAge` | Number | Sets the cookie’s lifespan in seconds. |
| `domain` | String | Specifies the domain where the cookie is available. |
| `path` | String, default: `'/'` | Limits the cookie's scope to a specific path within the domain. |
| `secure` | Boolean | Ensures the cookie is sent only over HTTPS connections for added security. |
| `httpOnly` | Boolean | Restricts the cookie to HTTP requests, preventing client\-side access. |
| `sameSite` | Boolean, `'lax'`, `'strict'`, `'none'` | Controls the cookie's cross\-site request behavior. |
| `priority` | String (`"low"`, `"medium"`, `"high"`) | Specifies the cookie's priority |
| `encode('value')` | Function | Specifies a function that will be used to encode a cookie's value. |
| `partitioned` | Boolean | Indicates whether the cookie is [partitioned](https://github.com/privacycg/CHIPS). |

The only option with a default value is `path`.

To learn more about these options, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

## [Good to know](#good-to-know)

* `cookies` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access cookies.
	+ In version 14 and earlier, `cookies` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* `cookies` is a [Dynamic API](/docs/app/building-your-application/rendering/server-components#dynamic-apis) whose returned values cannot be known ahead of time. Using it in a layout or page will opt a route into [dynamic rendering](/docs/app/building-your-application/rendering/server-components#dynamic-rendering).
* The `.delete` method can only be called:
	+ In a [Server Action](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) or [Route Handler](/docs/app/building-your-application/routing/route-handlers).
	+ If it belongs to the same domain from which `.set` is called. Additionally, the code must be executed on the same protocol (HTTP or HTTPS) as the cookie you want to delete.
* HTTP does not allow setting cookies after streaming starts, so you must use `.set` in a [Server Action](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) or [Route Handler](/docs/app/building-your-application/routing/route-handlers).

## [Understanding Cookie Behavior in Server Components](#understanding-cookie-behavior-in-server-components)

When working with cookies in Server Components, it's important to understand that cookies are fundamentally a client\-side storage mechanism:

* **Reading cookies** works in Server Components because you're accessing the cookie data that the client's browser sends to the server in the HTTP request headers.
* **Setting cookies** cannot be done directly in a Server Component, even when using a Route Handler or Server Action. This is because cookies are actually stored by the browser, not the server.

The server can only send instructions (via `Set-Cookie` headers) to tell the browser to store cookies \- the actual storage happens on the client side. This is why cookie operations that modify state (`.set`, `.delete`, `.clear`) must be performed in a Route Handler or Server Action where the response headers can be properly set.

## [Examples](#examples)

### [Getting a cookie](#getting-a-cookie)

You can use the `(await cookies()).get('name')` method to get a single cookie:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { cookies } from 'next/headers'

export default async function Page() {
 const cookieStore = await cookies()
 const theme = cookieStore.get('theme')
 return '...'
}
\`\`\`

### [Getting all cookies](#getting-all-cookies)

You can use the `(await cookies()).getAll()` method to get all cookies with a matching name. If `name` is unspecified, it returns all the available cookies.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { cookies } from 'next/headers'

export default async function Page() {
 const cookieStore = await cookies()
 return cookieStore.getAll().map((cookie) =\> (
 \
 \Name: {cookie.name}\
 \Value: {cookie.value}\
 \
 ))
}
\`\`\`

### [Setting a cookie](#setting-a-cookie)

You can use the `(await cookies()).set(name, value, options)` method in a [Server Action](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) or [Route Handler](/docs/app/building-your-application/routing/route-handlers) to set a cookie. The [`options` object](#options) is optional.

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { cookies } from 'next/headers'

export async function create(data) {
 const cookieStore = await cookies()

 cookieStore.set('name', 'lee')
 // or
 cookieStore.set('name', 'lee', { secure: true })
 // or
 cookieStore.set({
 name: 'name',
 value: 'lee',
 httpOnly: true,
 path: '/',
 })
}
\`\`\`

### [Checking if a cookie exists](#checking-if-a-cookie-exists)

You can use the `(await cookies()).has(name)` method to check if a cookie exists:

app/page.tsTypeScriptJavaScriptTypeScript\`\`\`
import { cookies } from 'next/headers'

export default async function Page() {
 const cookieStore = await cookies()
 const hasCookie = cookieStore.has('theme')
 return '...'
}
\`\`\`

### [Deleting cookies](#deleting-cookies)

There are three ways you can delete a cookie.

Using the `delete()` method:

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
 (await cookies()).delete('name')
}
\`\`\`

Setting a new cookie with the same name and an empty value:

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
 (await cookies()).set('name', '')
}
\`\`\`

Setting the `maxAge` to 0 will immediately expire a cookie. `maxAge` accepts a value in seconds.

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
 (await cookies()).set('name', 'value', { maxAge: 0 })
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `cookies` is now an async function. A [codemod](/docs/app/building-your-application/upgrading/codemods#150) is available. |
| `v13.0.0` | `cookies` introduced. |

Was this helpful?



## Functions: NextRequest | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/next-request)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)NextRequest# NextRequest

NextRequest extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional convenience methods.

## [`cookies`](#cookies)

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the request.

### [`set(name, value)`](#setname-value)

Given a name, set a cookie with the given value on the request.

\`\`\`
// Given incoming request /home
// Set a cookie to hide the banner
// request will have a \`Set\-Cookie:show\-banner=false;path=/home\` header
request.cookies.set('show\-banner', 'false')
\`\`\`
### [`get(name)`](#getname)

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

\`\`\`
// Given incoming request /home
// { name: 'show\-banner', value: 'false', Path: '/home' }
request.cookies.get('show\-banner')
\`\`\`
### [`getAll()`](#getall)

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.

\`\`\`
// Given incoming request /home
// \[
// { name: 'experiments', value: 'new\-pricing\-page', Path: '/home' },
// { name: 'experiments', value: 'winter\-launch', Path: '/home' },
// ]
request.cookies.getAll('experiments')
// Alternatively, get all cookies for the request
request.cookies.getAll()
\`\`\`
### [`delete(name)`](#deletename)

Given a cookie name, delete the cookie from the request.

\`\`\`
// Returns true for deleted, false is nothing is deleted
request.cookies.delete('experiments')
\`\`\`
### [`has(name)`](#hasname)

Given a cookie name, return `true` if the cookie exists on the request.

\`\`\`
// Returns true if cookie exists, false if it does not
request.cookies.has('experiments')
\`\`\`
### [`clear()`](#clear)

Remove the `Set-Cookie` header from the request.

\`\`\`
request.cookies.clear()
\`\`\`
## [`nextUrl`](#nexturl)

Extends the native [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API with additional convenience methods, including Next.js specific properties.

\`\`\`
// Given a request to /home, pathname is /home
request.nextUrl.pathname
// Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
request.nextUrl.searchParams
\`\`\`
The following options are available:

| Property | Type | Description |
| --- | --- | --- |
| `basePath` | `string` | The [base path](/docs/app/api-reference/config/next-config-js/basePath) of the URL. |
| `buildId` | `string` \| `undefined` | The build identifier of the Next.js application. Can be [customized](/docs/app/api-reference/config/next-config-js/generateBuildId). |
| `pathname` | `string` | The pathname of the URL. |
| `searchParams` | `Object` | The search parameters of the URL. |

> **Note:** The internationalization properties from the Pages Router are not available for usage in the App Router. Learn more about [internationalization with the App Router](/docs/app/building-your-application/routing/internationalization).

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `ip` and `geo` removed. |

Was this helpful?



## Functions: useParams | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-params)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)useParams# useParams

`useParams` is a **Client Component** hook that lets you read a route's [dynamic params](/docs/app/building-your-application/routing/dynamic-routes) filled in by the current URL.

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useParams } from 'next/navigation'

export default function ExampleClientComponent() {
 const params = useParams\()

 // Route \-\> /shop/\[tag]/\[item]
 // URL \-\> /shop/shoes/nike\-air\-max\-97
 // \`params\` \-\> { tag: 'shoes', item: 'nike\-air\-max\-97' }
 console.log(params)

 return '...'
}
\`\`\`

## [Parameters](#parameters)

\`\`\`
const params = useParams()
\`\`\`
`useParams` does not take any parameters.

## [Returns](#returns)

`useParams` returns an object containing the current route's filled in [dynamic parameters](/docs/app/building-your-application/routing/dynamic-routes).

* Each property in the object is an active dynamic segment.
* The properties name is the segment's name, and the properties value is what the segment is filled in with.
* The properties value will either be a `string` or array of `string`'s depending on the [type of dynamic segment](/docs/app/building-your-application/routing/dynamic-routes).
* If the route contains no dynamic parameters, `useParams` returns an empty object.
* If used in Pages Router, `useParams` will return `null` on the initial render and updates with properties following the rules above once the router is ready.

For example:

| Route | URL | `useParams()` |
| --- | --- | --- |
| `app/shop/page.js` | `/shop` | `{}` |
| `app/shop/[slug]/page.js` | `/shop/1` | `{ slug: '1' }` |
| `app/shop/[tag]/[item]/page.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |
| `app/shop/[...slug]/page.js` | `/shop/1/2` | `{ slug: ['1', '2'] }` |

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `useParams` introduced. |

Was this helpful?



## Getting Started: Layouts and Pages | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started/layouts-and-pages)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Layouts and Pages# How to create layouts and pages

Next.js uses **file\-system based routing**, meaning you can use folders and files to define routes. This page will guide you through how to create layouts and pages, and link between them.

## [Creating a page](#creating-a-page)

A **page** is UI that is rendered on a specific route. To create a page, add a [`page` file](/docs/app/api-reference/file-conventions/page) inside the `app` directory and default export a React component. For example, to create an index page (`/`):


app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Page() {
 return \Hello Next.js!\
}
\`\`\`

## [Creating a layout](#creating-a-layout)

A layout is UI that is **shared** between multiple pages. On navigation, layouts preserve state, remain interactive, and do not rerender.

You can define a layout by default exporting a React component from a [`layout` file](/docs/app/api-reference/file-conventions/layout). The component should accept a `children` prop which can be a page or another [layout](#nesting-layouts).

For example, to create a layout that accepts your index page as child, add a `layout` file inside the `app` directory:


app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function DashboardLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \
 {/\* Layout UI \*/}
 {/\* Place children where you want to render a page or nested layout \*/}
 \{children}\
 \
 \
 )
}
\`\`\`

The layout above is called a [root layout](/docs/app/api-reference/file-conventions/layout#root-layouts) because it's defined at the root of the `app` directory. The root layout is **required** and must contain `html` and `body` tags.

## [Creating a nested route](#creating-a-nested-route)

A nested route is a route composed of multiple URL segments. For example, the `/blog/[slug]` route is composed of three segments:

* `/` (Root Segment)
* `blog` (Segment)
* `[slug]` (Leaf Segment)

In Next.js:

* **Folders** are used to define the route segments that map to URL segments.
* **Files** (like `page` and `layout`) are used to create UI that is shown for a segment.

To create nested routes, you can nest folders inside each other. For example, to add a route for `/blog`, create a folder called `blog` in the `app` directory. Then, to make `/blog` publicly accessible, add a `page` file:


app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { getPosts } from '@/lib/posts'
import { Post } from '@/ui/post'

export default async function Page() {
 const posts = await getPosts()

 return (
 \
 {posts.map((post) =\> (
 \
 ))}
 \
 )
}
\`\`\`

You can continue nesting folders to create nested routes. For example, to create a route for a specific blog post, create a new `[slug]` folder inside `blog` and add a `page` file:


app/blog/\[slug]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
function generateStaticParams() {}

export default function Page() {
 return \Hello, Blog Post Page!\
}
\`\`\`

> **Good to know**: Wrapping a folder name in square brackets (e.g. `[slug]`) creates a special [dynamic route segment](/docs/app/building-your-application/routing/dynamic-routes) used to generate multiple pages from data. This is useful for blog posts, product pages, etc.

## [Nesting layouts](#nesting-layouts)

By default, layouts in the folder hierarchy are also nested, which means they wrap child layouts via their `children` prop. You can nest layouts by adding `layout` inside specific route segments (folders).

For example, to create a layout for the `/blog` route, add a new `layout` file inside the `blog` folder.


app/blog/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function BlogLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return \{children}\
}
\`\`\`

If you were to combine the two layouts above, the root layout (`app/layout.js`) would wrap the blog layout (`app/blog/layout.js`), which would wrap the blog (`app/blog/page.js`) and blog post page (`app/blog/[slug]/page.js`).

## [Linking between pages](#linking-between-pages)

You can use the [`` component](/docs/app/api-reference/components/link) to navigate between routes. `` is a built\-in Next.js component that extends the HTML `` tag to provide prefetching and client\-side navigation.

For example, to generate a list of blog posts, import `` from `next/link` and pass a `href` prop to the component:

app/ui/post.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default async function Post({ post }) {
 const posts = await getPosts()

 return (
 \
 {posts.map((post) =\> (
 \
 \{post.title}\
 \
 ))}
 \
 )
}
\`\`\`

`` is the primary and recommended way to navigate between routes in your Next.js application. However, you can also use the [`useRouter` hook](/docs/app/api-reference/functions/use-router) for more advanced navigation.

## API Reference

Learn more about the features mentioned in this page by reading the API Reference.[### layout.js

API reference for the layout.js file.](/docs/app/api-reference/file-conventions/layout)[### page.js

API reference for the page.js file.](/docs/app/api-reference/file-conventions/page)[### \

Enable fast client\-side navigation with the built\-in \`next/link\` component.](/docs/app/api-reference/components/link)Was this helpful?



## Functions: generateMetadata | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)generateMetadata# generateMetadata

This page covers all **Config\-based Metadata** options with `generateMetadata` and the static metadata object.

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

// either Static metadata
export const metadata: Metadata = {
 title: '...',
}

// or Dynamic metadata
export async function generateMetadata({ params }) {
 return {
 title: '...',
 }
}
\`\`\`

> **Good to know**:
> 
> 
> * The `metadata` object and `generateMetadata` function exports are **only supported in Server Components**.
> * You cannot export both the `metadata` object and `generateMetadata` function from the same route segment.
> * On the initial load, streaming is blocked until `generateMetadata` has fully resolved, including any content from `loading.js`.

## [The `metadata` object](#the-metadata-object)

To define static metadata, export a [`Metadata` object](#metadata-fields) from a `layout.js` or `page.js` file.

layout.tsx \| page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: '...',
 description: '...',
}

export default function Page() {}
\`\`\`

See the [Metadata Fields](#metadata-fields) for a complete list of supported options.

## [`generateMetadata` function](#generatemetadata-function)

Dynamic metadata depends on **dynamic information**, such as the current route parameters, external data, or `metadata` in parent segments, can be set by exporting a `generateMetadata` function that returns a [`Metadata` object](#metadata-fields).

app/products/\[id]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata, ResolvingMetadata } from 'next'

type Props = {
 params: Promise\
 searchParams: Promise\
}

export async function generateMetadata(
 { params, searchParams }: Props,
 parent: ResolvingMetadata
): Promise\ {
 // read route params
 const id = (await params).id

 // fetch data
 const product = await fetch(\`https://.../${id}\`).then((res) =\> res.json())

 // optionally access and extend (rather than replace) parent metadata
 const previousImages = (await parent).openGraph?.images \|\| \[]

 return {
 title: product.title,
 openGraph: {
 images: \['/some\-specific\-page\-image.jpg', ...previousImages],
 },
 }
}

export default function Page({ params, searchParams }: Props) {}
\`\`\`

### [Parameters](#parameters)

`generateMetadata` function accepts the following parameters:

* `props` \- An object containing the parameters of the current route:

	+ `params` \- An object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) object from the root segment down to the segment `generateMetadata` is called from. Examples:

	| Route | URL | `params` |
	| --- | --- | --- |
	| `app/shop/[slug]/page.js` | `/shop/1` | `{ slug: '1' }` |
	| `app/shop/[tag]/[item]/page.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |
	| `app/shop/[...slug]/page.js` | `/shop/1/2` | `{ slug: ['1', '2'] }` |
	+ `searchParams` \- An object containing the current URL's [search params](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters). Examples:

	| URL | `searchParams` |
	| --- | --- |
	| `/shop?a=1` | `{ a: '1' }` |
	| `/shop?a=1&b=2` | `{ a: '1', b: '2' }` |
	| `/shop?a=1&a=2` | `{ a: ['1', '2'] }` |
* `parent` \- A promise of the resolved metadata from parent route segments.

### [Returns](#returns)

`generateMetadata` should return a [`Metadata` object](#metadata-fields) containing one or more metadata fields.

> **Good to know**:
> 
> 
> * If metadata doesn't depend on runtime information, it should be defined using the static [`metadata` object](#the-metadata-object) rather than `generateMetadata`.
> * `fetch` requests are automatically [memoized](/docs/app/building-your-application/caching#request-memoization) for the same data across `generateMetadata`, `generateStaticParams`, Layouts, Pages, and Server Components. React [`cache` can be used](/docs/app/building-your-application/caching#react-cache-function) if `fetch` is unavailable.
> * `searchParams` are only available in `page.js` segments.
> * The [`redirect()`](/docs/app/api-reference/functions/redirect) and [`notFound()`](/docs/app/api-reference/functions/not-found) Next.js methods can also be used inside `generateMetadata`.

## [Metadata Fields](#metadata-fields)

### [`title`](#title)

The `title` attribute is used to set the title of the document. It can be defined as a simple [string](#string) or an optional [template object](#template-object).

#### [String](#string)

layout.js \| page.js\`\`\`
export const metadata = {
 title: 'Next.js',
}
\`\`\`
\ output\`\`\`
\Next.js\
\`\`\`
#### [Template object](#template-object)

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: {
 template: '...',
 default: '...',
 absolute: '...',
 },
}
\`\`\`

##### [Default](#default)

`title.default` can be used to provide a **fallback title** to child route segments that don't define a `title`.

app/layout.tsx\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: {
 default: 'Acme',
 },
}
\`\`\`
app/about/page.tsx\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {}

// Output: \Acme\
\`\`\`
##### [Template](#template)

`title.template` can be used to add a prefix or a suffix to `titles` defined in **child** route segments.

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: {
 template: '%s \| Acme',
 default: 'Acme', // a default is required when creating a template
 },
}
\`\`\`

app/about/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: 'About',
}

// Output: \About \| Acme\
\`\`\`

> **Good to know**:
> 
> 
> * `title.template` applies to **child** route segments and **not** the segment it's defined in. This means:
> 
> 
> 	+ `title.default` is **required** when you add a `title.template`.
> 	+ `title.template` defined in `layout.js` will not apply to a `title` defined in a `page.js` of the same route segment.
> 	+ `title.template` defined in `page.js` has no effect because a page is always the terminating segment (it doesn't have any children route segments).
> * `title.template` has **no effect** if a route has not defined a `title` or `title.default`.

##### [Absolute](#absolute)

`title.absolute` can be used to provide a title that **ignores** `title.template` set in parent segments.

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: {
 template: '%s \| Acme',
 },
}
\`\`\`

app/about/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: {
 absolute: 'About',
 },
}

// Output: \About\
\`\`\`

> **Good to know**:
> 
> 
> * `layout.js`
> 
> 
> 	+ `title` (string) and `title.default` define the default title for child segments (that do not define their own `title`). It will augment `title.template` from the closest parent segment if it exists.
> 	+ `title.absolute` defines the default title for child segments. It ignores `title.template` from parent segments.
> 	+ `title.template` defines a new title template for child segments.
> * `page.js`
> 
> 
> 	+ If a page does not define its own title the closest parents resolved title will be used.
> 	+ `title` (string) defines the routes title. It will augment `title.template` from the closest parent segment if it exists.
> 	+ `title.absolute` defines the route title. It ignores `title.template` from parent segments.
> 	+ `title.template` has no effect in `page.js` because a page is always the terminating segment of a route.

### [`description`](#description)

layout.js \| page.js\`\`\`
export const metadata = {
 description: 'The React Framework for the Web',
}
\`\`\`
\ output\`\`\`
\
\`\`\`
### [Basic Fields](#basic-fields)

layout.js \| page.js\`\`\`
export const metadata = {
 generator: 'Next.js',
 applicationName: 'Next.js',
 referrer: 'origin\-when\-cross\-origin',
 keywords: \['Next.js', 'React', 'JavaScript'],
 authors: \[{ name: 'Seb' }, { name: 'Josh', url: 'https://nextjs.org' }],
 creator: 'Jiachi Liu',
 publisher: 'Sebastian Markbåge',
 formatDetection: {
 email: false,
 address: false,
 telephone: false,
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\
\
\
\
\
\`\`\`
### [`metadataBase`](#metadatabase)

`metadataBase` is a convenience option to set a base URL prefix for `metadata` fields that require a fully qualified URL.

* `metadataBase` allows URL\-based `metadata` fields defined in the **current route segment and below** to use a **relative path** instead of an otherwise required absolute URL.
* The field's relative path will be composed with `metadataBase` to form a fully qualified URL.
* If not configured, `metadataBase` is **automatically populated** with a [default value](#default-value).

layout.js \| page.js\`\`\`
export const metadata = {
 metadataBase: new URL('https://acme.com'),
 alternates: {
 canonical: '/',
 languages: {
 'en\-US': '/en\-US',
 'de\-DE': '/de\-DE',
 },
 },
 openGraph: {
 images: '/og\-image.png',
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\`\`\`

> **Good to know**:
> 
> 
> * `metadataBase` is typically set in root `app/layout.js` to apply to URL\-based `metadata` fields across all routes.
> * All URL\-based `metadata` fields that require absolute URLs can be configured with a `metadataBase` option.
> * `metadataBase` can contain a subdomain e.g. `https://app.acme.com` or base path e.g. `https://acme.com/start/from/here`
> * If a `metadata` field provides an absolute URL, `metadataBase` will be ignored.
> * Using a relative path in a URL\-based `metadata` field without configuring a `metadataBase` will cause a build error.
> * Next.js will normalize duplicate slashes between `metadataBase` (e.g. `https://acme.com/`) and a relative field (e.g. `/path`) to a single slash (e.g. `https://acme.com/path`)

#### [Default value](#default-value)

If not configured, `metadataBase` has a **default value**.

> On Vercel:
> 
> 
> * For production deployments, `VERCEL_PROJECT_PRODUCTION_URL` will be used.
> * For preview deployments, `VERCEL_BRANCH_URL` will take priority, and fallback to `VERCEL_URL` if it's not present.
> 
> 
> If these values are present they will be used as the **default value** of `metadataBase`, otherwise it falls back to `http://localhost:${process.env.PORT || 3000}`. This allows Open Graph images to work on both local build and Vercel preview and production deployments. When overriding the default, we recommend using environment variables to compute the URL. This allows configuring a URL for local development, staging, and production environments.
> 
> 
> See more details about these environment variables in the [System Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables/system-environment-variables) docs.

#### [URL Composition](#url-composition)

URL composition favors developer intent over default directory traversal semantics.

* Trailing slashes between `metadataBase` and `metadata` fields are normalized.
* An "absolute" path in a `metadata` field (that typically would replace the whole URL path) is treated as a "relative" path (starting from the end of `metadataBase`).

For example, given the following `metadataBase`:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 metadataBase: new URL('https://acme.com'),
}
\`\`\`

Any `metadata` fields that inherit the above `metadataBase` and set their own value will be resolved as follows:

| `metadata` field | Resolved URL |
| --- | --- |
| `/` | `https://acme.com` |
| `./` | `https://acme.com` |
| `payments` | `https://acme.com/payments` |
| `/payments` | `https://acme.com/payments` |
| `./payments` | `https://acme.com/payments` |
| `../payments` | `https://acme.com/payments` |
| `https://beta.acme.com/payments` | `https://beta.acme.com/payments` |

### [`openGraph`](#opengraph)

layout.js \| page.js\`\`\`
export const metadata = {
 openGraph: {
 title: 'Next.js',
 description: 'The React Framework for the Web',
 url: 'https://nextjs.org',
 siteName: 'Next.js',
 images: \[
 {
 url: 'https://nextjs.org/og.png', // Must be an absolute URL
 width: 800,
 height: 600,
 },
 {
 url: 'https://nextjs.org/og\-alt.png', // Must be an absolute URL
 width: 1800,
 height: 1600,
 alt: 'My custom alt',
 },
 ],
 videos: \[
 {
 url: 'https://nextjs.org/video.mp4', // Must be an absolute URL
 width: 800,
 height: 600,
 },
 ],
 audio: \[
 {
 url: 'https://nextjs.org/audio.mp3', // Must be an absolute URL
 },
 ],
 locale: 'en\_US',
 type: 'website',
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\`\`\`
layout.js \| page.js\`\`\`
export const metadata = {
 openGraph: {
 title: 'Next.js',
 description: 'The React Framework for the Web',
 type: 'article',
 publishedTime: '2023\-01\-01T00:00:00\.000Z',
 authors: \['Seb', 'Josh'],
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\`\`\`

> **Good to know**:
> 
> 
> * It may be more convenient to use the [file\-based Metadata API](/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif) for Open Graph images. Rather than having to sync the config export with actual files, the file\-based API will automatically generate the correct metadata for you.

### [`robots`](#robots)

layout.tsx \| page.tsx\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 robots: {
 index: false,
 follow: true,
 nocache: true,
 googleBot: {
 index: true,
 follow: false,
 noimageindex: true,
 'max\-video\-preview': \-1,
 'max\-image\-preview': 'large',
 'max\-snippet': \-1,
 },
 },
}
\`\`\`
\ output\`\`\`
\
\
\`\`\`
### [`icons`](#icons)

> **Good to know**: We recommend using the [file\-based Metadata API](/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png) for icons where possible. Rather than having to sync the config export with actual files, the file\-based API will automatically generate the correct metadata for you.

layout.js \| page.js\`\`\`
export const metadata = {
 icons: {
 icon: '/icon.png',
 shortcut: '/shortcut\-icon.png',
 apple: '/apple\-icon.png',
 other: {
 rel: 'apple\-touch\-icon\-precomposed',
 url: '/apple\-touch\-icon\-precomposed.png',
 },
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\`\`\`
layout.js \| page.js\`\`\`
export const metadata = {
 icons: {
 icon: \[
 { url: '/icon.png' },
 new URL('/icon.png', 'https://example.com'),
 { url: '/icon\-dark.png', media: '(prefers\-color\-scheme: dark)' },
 ],
 shortcut: \['/shortcut\-icon.png'],
 apple: \[
 { url: '/apple\-icon.png' },
 { url: '/apple\-icon\-x3\.png', sizes: '180x180', type: 'image/png' },
 ],
 other: \[
 {
 rel: 'apple\-touch\-icon\-precomposed',
 url: '/apple\-touch\-icon\-precomposed.png',
 },
 ],
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\
\`\`\`

> **Good to know**: The `msapplication-*` meta tags are no longer supported in Chromium builds of Microsoft Edge, and thus no longer needed.

### [`themeColor`](#themecolor)

> **Deprecated**: The `themeColor` option in `metadata` is deprecated as of Next.js 14\. Please use the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport) instead.

### [`manifest`](#manifest)

A web application manifest, as defined in the [Web Application Manifest specification](https://developer.mozilla.org/docs/Web/Manifest).

layout.js \| page.js\`\`\`
export const metadata = {
 manifest: 'https://nextjs.org/manifest.json',
}
\`\`\`
\ output\`\`\`
\
\`\`\`
### [`twitter`](#twitter)

The Twitter specification is (surprisingly) used for more than just X (formerly known as Twitter).

Learn more about the [Twitter Card markup reference](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/markup).

layout.js \| page.js\`\`\`
export const metadata = {
 twitter: {
 card: 'summary\_large\_image',
 title: 'Next.js',
 description: 'The React Framework for the Web',
 siteId: '1467726470533754880',
 creator: '@nextjs',
 creatorId: '1467726470533754880',
 images: \['https://nextjs.org/og.png'], // Must be an absolute URL
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\
\`\`\`
layout.js \| page.js\`\`\`
export const metadata = {
 twitter: {
 card: 'app',
 title: 'Next.js',
 description: 'The React Framework for the Web',
 siteId: '1467726470533754880',
 creator: '@nextjs',
 creatorId: '1467726470533754880',
 images: {
 url: 'https://nextjs.org/og.png',
 alt: 'Next.js Logo',
 },
 app: {
 name: 'twitter\_app',
 id: {
 iphone: 'twitter\_app://iphone',
 ipad: 'twitter\_app://ipad',
 googleplay: 'twitter\_app://googleplay',
 },
 url: {
 iphone: 'https://iphone\_url',
 ipad: 'https://ipad\_url',
 },
 },
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\`\`\`
### [`viewport`](#viewport)

> **Deprecated**: The `viewport` option in `metadata` is deprecated as of Next.js 14\. Please use the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport) instead.

### [`verification`](#verification)

layout.js \| page.js\`\`\`
export const metadata = {
 verification: {
 google: 'google',
 yandex: 'yandex',
 yahoo: 'yahoo',
 other: {
 me: \['my\-email', 'my\-link'],
 },
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\`\`\`
### [`appleWebApp`](#applewebapp)

layout.js \| page.js\`\`\`
export const metadata = {
 itunes: {
 appId: 'myAppStoreID',
 appArgument: 'myAppArgument',
 },
 appleWebApp: {
 title: 'Apple Web App',
 statusBarStyle: 'black\-translucent',
 startupImage: \[
 '/assets/startup/apple\-touch\-startup\-image\-768x1004\.png',
 {
 url: '/assets/startup/apple\-touch\-startup\-image\-1536x2008\.png',
 media: '(device\-width: 768px) and (device\-height: 1024px)',
 },
 ],
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\`\`\`
### [`alternates`](#alternates)

layout.js \| page.js\`\`\`
export const metadata = {
 alternates: {
 canonical: 'https://nextjs.org',
 languages: {
 'en\-US': 'https://nextjs.org/en\-US',
 'de\-DE': 'https://nextjs.org/de\-DE',
 },
 media: {
 'only screen and (max\-width: 600px)': 'https://nextjs.org/mobile',
 },
 types: {
 'application/rss\+xml': 'https://nextjs.org/rss',
 },
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\`\`\`
### [`appLinks`](#applinks)

layout.js \| page.js\`\`\`
export const metadata = {
 appLinks: {
 ios: {
 url: 'https://nextjs.org/ios',
 app\_store\_id: 'app\_store\_id',
 },
 android: {
 package: 'com.example.android/package',
 app\_name: 'app\_name\_android',
 },
 web: {
 url: 'https://nextjs.org/web',
 should\_fallback: true,
 },
 },
}
\`\`\`
\ output\`\`\`
\
\
\
\
\
\
\`\`\`
### [`archives`](#archives)

Describes a collection of records, documents, or other materials of historical interest ([source](https://www.w3.org/TR/2011/WD-html5-20110113/links.html#rel-archives)).

layout.js \| page.js\`\`\`
export const metadata = {
 archives: \['https://nextjs.org/13'],
}
\`\`\`
\ output\`\`\`
\
\`\`\`
### [`assets`](#assets)

layout.js \| page.js\`\`\`
export const metadata = {
 assets: \['https://nextjs.org/assets'],
}
\`\`\`
\ output\`\`\`
\
\`\`\`
### [`bookmarks`](#bookmarks)

layout.js \| page.js\`\`\`
export const metadata = {
 bookmarks: \['https://nextjs.org/13'],
}
\`\`\`
\ output\`\`\`
\
\`\`\`
### [`category`](#category)

layout.js \| page.js\`\`\`
export const metadata = {
 category: 'technology',
}
\`\`\`
\ output\`\`\`
\
\`\`\`
### [`facebook`](#facebook)

You can connect a Facebook app or Facebook account to you webpage for certain Facebook Social Plugins [Facebook Documentation](https://developers.facebook.com/docs/plugins/comments/#moderation-setup-instructions)

> **Good to know**: You can specify either appId or admins, but not both.

layout.js \| page.js\`\`\`
export const metadata = {
 facebook: {
 appId: '12345678',
 },
}
\`\`\`
\ output\`\`\`
\
\`\`\`
layout.js \| page.js\`\`\`
export const metadata = {
 facebook: {
 admins: '12345678',
 },
}
\`\`\`
\ output\`\`\`
\
\`\`\`
If you want to generate multiple fb:admins meta tags you can use array value.

layout.js \| page.js\`\`\`
export const metadata = {
 facebook: {
 admins: \['12345678', '87654321'],
 },
}
\`\`\`
\ output\`\`\`
\
\
\`\`\`
### [`other`](#other)

All metadata options should be covered using the built\-in support. However, there may be custom metadata tags specific to your site, or brand new metadata tags just released. You can use the `other` option to render any custom metadata tag.

layout.js \| page.js\`\`\`
export const metadata = {
 other: {
 custom: 'meta',
 },
}
\`\`\`
\ output\`\`\`
\
\`\`\`
If you want to generate multiple same key meta tags you can use array value.

layout.js \| page.js\`\`\`
export const metadata = {
 other: {
 custom: \['meta1', 'meta2'],
 },
}
\`\`\`
\ output\`\`\`
\ \
\`\`\`
## [Unsupported Metadata](#unsupported-metadata)

The following metadata types do not currently have built\-in support. However, they can still be rendered in the layout or page itself.

| Metadata | Recommendation |
| --- | --- |
| `` | Use appropriate HTTP Headers via [`redirect()`](/docs/app/api-reference/functions/redirect), [Middleware](/docs/app/building-your-application/routing/middleware#nextresponse), [Security Headers](/docs/app/api-reference/config/next-config-js/headers) |
| `` | Render the tag in the layout or page itself. |
| `` | Render the tag in the layout or page itself. |
| `` | Learn more about [styling in Next.js](/docs/app/building-your-application/styling/css). |
| `` | Learn more about [using scripts](/docs/app/building-your-application/optimizing/scripts). |
| `` | `import` stylesheets directly in the layout or page itself. |
| `` | Use [ReactDOM preload method](#link-relpreload) |
| `` | Use [ReactDOM preconnect method](#link-relpreconnect) |
| `` | Use [ReactDOM prefetchDNS method](#link-reldns-prefetch) |

### [Resource hints](#resource-hints)

The `` element has a number of `rel` keywords that can be used to hint to the browser that an external resource is likely to be needed. The browser uses this information to apply preloading optimizations depending on the keyword.

While the Metadata API doesn't directly support these hints, you can use new [`ReactDOM` methods](https://github.com/facebook/react/pull/26237) to safely insert them into the `` of the document.

app/preload\-resources.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import ReactDOM from 'react\-dom'

export function PreloadResources() {
 ReactDOM.preload('...', { as: '...' })
 ReactDOM.preconnect('...', { crossOrigin: '...' })
 ReactDOM.prefetchDNS('...')

 return '...'
}
\`\`\`

##### [``](#link-relpreload)

Start loading a resource early in the page rendering (browser) lifecycle. [MDN Docs](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/preload).

\`\`\`
ReactDOM.preload(href: string, options: { as: string })
\`\`\`
\ output\`\`\`
\
\`\`\`
##### [``](#link-relpreconnect)

Preemptively initiate a connection to an origin. [MDN Docs](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/preconnect).

\`\`\`
ReactDOM.preconnect(href: string, options?: { crossOrigin?: string })
\`\`\`
\ output\`\`\`
\
\`\`\`
##### [``](#link-reldns-prefetch)

Attempt to resolve a domain name before resources get requested. [MDN Docs](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/dns-prefetch).

\`\`\`
ReactDOM.prefetchDNS(href: string)
\`\`\`
\ output\`\`\`
\
\`\`\`

> **Good to know**:
> 
> 
> * These methods are currently only supported in Client Components, which are still Server Side Rendered on initial page load.
> * Next.js in\-built features such as `next/font`, `next/image` and `next/script` automatically handle relevant resource hints.

## [Types](#types)

You can add type safety to your metadata by using the `Metadata` type. If you are using the [built\-in TypeScript plugin](/docs/app/api-reference/config/typescript) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

### [`metadata` object](#metadata-object)

layout.tsx \| page.tsx\`\`\`
import type { Metadata } from 'next'

export const metadata: Metadata = {
 title: 'Next.js',
}
\`\`\`
### [`generateMetadata` function](#generatemetadata-function-1)

#### [Regular function](#regular-function)

layout.tsx \| page.tsx\`\`\`
import type { Metadata } from 'next'

export function generateMetadata(): Metadata {
 return {
 title: 'Next.js',
 }
}
\`\`\`
#### [Async function](#async-function)

layout.tsx \| page.tsx\`\`\`
import type { Metadata } from 'next'

export async function generateMetadata(): Promise\ {
 return {
 title: 'Next.js',
 }
}
\`\`\`
#### [With segment props](#with-segment-props)

layout.tsx \| page.tsx\`\`\`
import type { Metadata } from 'next'

type Props = {
 params: Promise\
 searchParams: Promise\
}

export function generateMetadata({ params, searchParams }: Props): Metadata {
 return {
 title: 'Next.js',
 }
}

export default function Page({ params, searchParams }: Props) {}
\`\`\`
#### [With parent metadata](#with-parent-metadata)

layout.tsx \| page.tsx\`\`\`
import type { Metadata, ResolvingMetadata } from 'next'

export async function generateMetadata(
 { params, searchParams }: Props,
 parent: ResolvingMetadata
): Promise\ {
 return {
 title: 'Next.js',
 }
}
\`\`\`
#### [JavaScript Projects](#javascript-projects)

For JavaScript projects, you can use JSDoc to add type safety.

layout.js \| page.js\`\`\`
/\*\* @type {import("next").Metadata} \*/
export const metadata = {
 title: 'Next.js',
}
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.2.0` | `viewport`, `themeColor`, and `colorScheme` deprecated in favor of the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport). |
| `v13.2.0` | `metadata` and `generateMetadata` introduced. |

## Next Steps

View all the Metadata API options.[### Metadata Files

API documentation for the metadata file conventions.](/docs/app/api-reference/file-conventions/metadata)[### generateViewport

API Reference for the generateViewport function.](/docs/app/api-reference/functions/generate-viewport)[### Metadata

Use the Metadata API to define metadata in any layout or page.](/docs/app/building-your-application/optimizing/metadata)Was this helpful?



## File Conventions: mdx-components.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)mdx\-components.js# mdx\-components.js

The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](/docs/app/building-your-application/configuring/mdx) and will not work without it. Additionally, you can use it to [customize styles](/docs/app/building-your-application/configuring/mdx#using-custom-styles-and-components).

Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

mdx\-components.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { MDXComponents } from 'mdx/types'

export function useMDXComponents(components: MDXComponents): MDXComponents {
 return {
 ...components,
 }
}
\`\`\`

## [Exports](#exports)

### [`useMDXComponents` function](#usemdxcomponents-function)

The file must export a single function, either as a default export or named `useMDXComponents`.

mdx\-components.tsxTypeScriptJavaScriptTypeScript\`\`\`
import type { MDXComponents } from 'mdx/types'

export function useMDXComponents(components: MDXComponents): MDXComponents {
 return {
 ...components,
 }
}
\`\`\`

## [Params](#params)

### [`components`](#components)

When defining MDX Components, the export function accepts a single parameter, `components`. This parameter is an instance of `MDXComponents`.

* The key is the name of the HTML element to override.
* The value is the component to render instead.

> **Good to know**: Remember to pass all other components (i.e. `...components`) that do not have overrides.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.1.2` | MDX Components added |

## Learn more about MDX Components

[### MDX

Learn how to configure MDX and use it in your Next.js apps.](/docs/app/building-your-application/configuring/mdx)Was this helpful?



## Getting Started: Images and Fonts | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started/images-and-fonts)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Images and Fonts# How to optimize images and fonts

Next.js comes with automatic image and font optimization for better performance and user experience. This page will guide you through how to start using them.

## [Handling static assets](#handling-static-assets)

You can store static files, like images and fonts, under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).


## [Optimizing images](#optimizing-images)

The Next.js [``](/docs/app/building-your-application/optimizing/images) component extends the HTML `` element to provide:

* **Size optimization:** Automatically serving correctly sized images for each device, using modern image formats like WebP and AVIF.
* **Visual stability:** Preventing [layout shift](https://web.dev/articles/cls) automatically when images are loading.
* **Faster page loads:** Only loading images when they enter the viewport using native browser lazy loading, with optional blur\-up placeholders.
* **Asset flexibility:** Resizing images on\-demand, even images stored on remote servers.

To start using ``, import it from `next/image` and render it within your component.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Image from 'next/image'

export default function Page() {
 return \
}
\`\`\`

The `src` property can be a [local](#local-images) or [remote](#remote-images) image.

### [Local images](#local-images)

To use a local image, `import` your `.jpg`, `.png`, or `.webp` image files from your [`public` folder](#handling-static-assets).

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Image from 'next/image'
import profilePic from './me.png'

export default function Page() {
 return (
 \
 )
}
\`\`\`

Next.js will automatically determine the intrinsic [`width`](/docs/app/api-reference/components/image#width) and [`height`](/docs/app/api-reference/components/image#height) of your image based on the imported file. These values are used to determine the image ratio and prevent [Cumulative Layout Shift](https://web.dev/articles/cls) while your image is loading.

### [Remote images](#remote-images)

To use a remote image, you can provide a URL string for the `src` property.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Image from 'next/image'

export default function Page() {
 return (
 \
 )
}
\`\`\`

Since Next.js does not have access to remote files during the build process, you'll need to provide the [`width`](/docs/app/api-reference/components/image#width), [`height`](/docs/app/api-reference/components/image#height) and optional [`blurDataURL`](/docs/app/api-reference/components/image#blurdataurl) props manually. The `width` and `height` attributes are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in.

Then, to safely allow images from remote servers, you need to define a list of supported URL patterns in [`next.config.js`](/docs/app/api-reference/config/next-config-js). Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import { NextConfig } from 'next'

const config: NextConfig = {
 images: {
 remotePatterns: \[
 {
 protocol: 'https',
 hostname: 's3\.amazonaws.com',
 port: '',
 pathname: '/my\-bucket/\*\*',
 search: '',
 },
 ],
 },
}

export default config
\`\`\`

## [Optimizing fonts](#optimizing-fonts)

The [`next/font`](/docs/app/api-reference/components/font) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes **built\-in automatic self\-hosting** for *any* font file. This means you can optimally load web fonts with no layout shift.

To start using `next/font`, import it from [`next/font/local`](#local-fonts) or [`next/font/google`](#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { Geist } from 'next/font/google'

const geist = Geist({
 subsets: \['latin'],
})

export default function Layout({ children }: { children: React.ReactNode }) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

### [Google fonts](#google-fonts)

You can automatically self\-host any Google Font. Fonts are included in the deployment and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from `next/font/google`:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { Geist } from 'next/font/google'

const geist = Geist({
 subsets: \['latin'],
})

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility. But if you can't use a variable font, you will **need to specify a weight**:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { Roboto } from 'next/font/google'

const roboto = Roboto({
 weight: '400',
 subsets: \['latin'],
})

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

### [Local fonts](#local-fonts)

To use a local font, import your font from `next/font/local` and specify the `src` of your local font file in the [`public` folder](#handling-static-assets).

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import localFont from 'next/font/local'

const myFont = localFont({
 src: './my\-font.woff2',
})

export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

If you want to use multiple files for a single font family, `src` can be an array:

\`\`\`
const roboto = localFont({
 src: \[
 {
 path: './Roboto\-Regular.woff2',
 weight: '400',
 style: 'normal',
 },
 {
 path: './Roboto\-Italic.woff2',
 weight: '400',
 style: 'italic',
 },
 {
 path: './Roboto\-Bold.woff2',
 weight: '700',
 style: 'normal',
 },
 {
 path: './Roboto\-BoldItalic.woff2',
 weight: '700',
 style: 'italic',
 },
 ],
})
\`\`\`## API Reference

Learn more about the features mentioned in this page by reading the API Reference.[### Font

Optimizing loading web fonts with the built\-in \`next/font\` loaders.](/docs/app/api-reference/components/font)[### \

Optimize Images in your Next.js Application using the built\-in \`next/image\` Component.](/docs/app/api-reference/components/image)Was this helpful?



## File Conventions: middleware.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)middleware.js# middleware.js

The `middleware.js|ts` file is used to write [Middleware](/docs/app/building-your-application/routing/middleware) and run code on the server before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

Middleware executes before routes are rendered. It's particularly useful for implementing custom server\-side logic like authentication, logging, or handling redirects.

Use the file `middleware.ts` (or .js) in the root of your project to define Middleware. For example, at the same level as `app` or `pages`, or inside `src` if applicable.

middleware.tsTypeScriptJavaScriptTypeScript\`\`\`
import { NextResponse, NextRequest } from 'next/server'

// This function can be marked \`async\` if using \`await\` inside
export function middleware(request: NextRequest) {
 return NextResponse.redirect(new URL('/home', request.url))
}

export const config = {
 matcher: '/about/:path\*',
}
\`\`\`

## [Exports](#exports)

### [Middleware function](#middleware-function)

The file must export a single function, either as a default export or named `middleware`. Note that multiple middleware from the same file are not supported.

middleware.js\`\`\`
// Example of default export
export default function middleware(request) {
 // Middleware logic
}
\`\`\`
### [Config object (optional)](#config-object-optional)

Optionally, a config object can be exported alongside the Middleware function. This object includes the [matcher](#matcher) to specify paths where the Middleware applies.

#### [Matcher](#matcher)

The `matcher` option allows you to target specific paths for the Middleware to run on. You can specify these paths in several ways:

* For a single path: Directly use a string to define the path, like `'/about'`.
* For multiple paths: Use an array to list multiple paths, such as `matcher: ['/about', '/contact']`, which applies the Middleware to both `/about` and `/contact`.

Additionally, `matcher` supports complex path specifications through regular expressions, such as `matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)']`, enabling precise control over which paths to include or exclude.

The `matcher` option also accepts an array of objects with the following keys:

* `source`: The path or pattern used to match the request paths. It can be a string for direct path matching or a pattern for more complex matching.
* `regexp` (optional): A regular expression string that fine\-tunes the matching based on the source. It provides additional control over which paths are included or excluded.
* `locale` (optional): A boolean that, when set to `false`, ignores locale\-based routing in path matching.
* `has` (optional): Specifies conditions based on the presence of specific request elements such as headers, query parameters, or cookies.
* `missing` (optional): Focuses on conditions where certain request elements are absent, like missing headers or cookies.

middleware.js\`\`\`
export const config = {
 matcher: \[
 {
 source: '/api/\*',
 regexp: '^/api/(.\*)',
 locale: false,
 has: \[
 { type: 'header', key: 'Authorization', value: 'Bearer Token' },
 { type: 'query', key: 'userId', value: '123' },
 ],
 missing: \[{ type: 'cookie', key: 'session', value: 'active' }],
 },
 ],
}
\`\`\`
## [Params](#params)

### [`request`](#request)

When defining Middleware, the default export function accepts a single parameter, `request`. This parameter is an instance of `NextRequest`, which represents the incoming HTTP request.

middleware.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
 // Middleware logic goes here
}
\`\`\`

> **Good to know**:
> 
> 
> * `NextRequest` is a type that represents incoming HTTP requests in Next.js Middleware, whereas [`NextResponse`](#nextresponse) is a class used to manipulate and send back HTTP responses.

## [NextResponse](#nextresponse)

Middleware can use the [`NextResponse`](/docs/app/building-your-application/routing/middleware#nextresponse) object which extends the [Web Response API](https://developer.mozilla.org/en-US/docs/Web/API/Response). By returning a `NextResponse` object, you can directly manipulate cookies, set headers, implement redirects, and rewrite paths.

> **Good to know**: For redirects, you can also use `Response.redirect` instead of `NextResponse.redirect`.

## [Runtime](#runtime)

Middleware only supports the [Edge runtime](/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes). The Node.js runtime cannot be used.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.1.0` | Advanced Middleware flags added |
| `v13.0.0` | Middleware can modify request headers, response headers, and send responses |
| `v12.2.0` | Middleware is stable, please see the [upgrade guide](/docs/messages/middleware-upgrade-guide) |
| `v12.0.9` | Enforce absolute URLs in Edge Runtime ([PR](https://github.com/vercel/next.js/pull/33410)) |
| `v12.0.0` | Middleware (Beta) added |

## Learn more about Middleware

[### Middleware

Learn how to use Middleware to run code before a request is completed.](/docs/app/building-your-application/routing/middleware)Was this helpful?



## Functions: unstable_noStore | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)unstable\_noStore# unstable\_noStore

This is a legacy API and no longer recommended. It's still supported for backward compatibility.**In version 15, we recommend using [`connection`](/docs/app/api-reference/functions/connection) instead of `unstable_noStore`.**

`unstable_noStore` can be used to declaratively opt out of static rendering and indicate a particular component should not be cached.

\`\`\`
import { unstable\_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
 noStore();
 const result = await db.query(...);
 ...
}
\`\`\`

> **Good to know**:
> 
> 
> * `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
> * `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per\-component basis

* Using `unstable_noStore` inside [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache) will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.

## [Usage](#usage)

If you prefer not to pass additional options to `fetch`, like `cache: 'no-store'`, `next: { revalidate: 0 }` or in cases where `fetch` is not available, you can use `noStore()` as a replacement for all of these use cases.

\`\`\`
import { unstable\_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
 noStore();
 const result = await db.query(...);
 ...
}
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `unstable_noStore` deprecated for `connection`. |
| `v14.0.0` | `unstable_noStore` introduced. |

Was this helpful?



## App Router: Getting Started | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[Introduction](/docs)[App Router](/docs/app)Getting Started# Getting Started

[### Installation

Create a new Next.js application with the \`create\-next\-app\` CLI, and set up TypeScript, ESLint, and Module Path Aliases.](/docs/app/getting-started/installation)[### Project Structure

An overview of the folder and file conventions in Next.js, and how to organize your project.](/docs/app/getting-started/project-structure)[### Layouts and Pages

Create your first pages and layouts, and link between them.](/docs/app/getting-started/layouts-and-pages)[### Images and Fonts

Learn how to optimize images and fonts.](/docs/app/getting-started/images-and-fonts)[### CSS and Styling

Learn about the different ways to add CSS to your application, including CSS Modules, Global CSS, Tailwind CSS, and more.](/docs/app/getting-started/css-and-styling)[### Fetching data and streaming

Start fetching data and streaming content in your application.](/docs/app/getting-started/data-fetching-and-streaming)Was this helpful?



## API Reference: Turbopack | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/turbopack)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)Turbopack# Turbopack

[Turbopack](https://turbo.build/pack) is an incremental bundler optimized for JavaScript and TypeScript, written in Rust, and built into Next.js. Turbopack can be used in Next.js in both the `pages` and `app` directories for faster local development.

To enable Turbopack, use the `--turbopack` flag when running the Next.js development server.

package.json\`\`\`
{
 "scripts": {
 "dev": "next dev \-\-turbopack",
 "build": "next build",
 "start": "next start",
 "lint": "next lint"
 }
}
\`\`\`
## [Reference](#reference)

### [Supported features](#supported-features)

Turbopack in Next.js requires zero\-configuration for most users and can be extended for more advanced use cases. To learn more about the currently supported features for Turbopack, view the [API Reference](/docs/app/api-reference/config/next-config-js/turbo).

### [Unsupported features](#unsupported-features)

Turbopack currently only supports `next dev` and does not support `next build`. We are currently working on support for builds as we move closer towards stability.

These features are currently not supported:

* Turbopack leverages [Lightning CSS](https://lightningcss.dev/) which doesn't support some low usage CSS Modules features
	+ `:local` and `:global` as standalone pseudo classes. Only the function variant is supported, for example: `:global(a)`.
	+ The @value rule which has been superseded by CSS variables.
	+ `:import` and `:export` ICSS rules.
* [Invalid CSS comment syntax](https://stackoverflow.com/questions/51843506/are-double-slash-comments-valid-in-css) such as `//`
	+ CSS comments should be written as `/* comment */` per the specification.
	+ Preprocessors such as Sass do support this alternative syntax for comments.
* [`webpack()`](/docs/app/api-reference/config/next-config-js/webpack) configuration in `next.config.js`
	+ Turbopack replaces Webpack, this means that webpack configuration is not supported.
	+ To configure Turbopack, [see the documentation](/docs/app/api-reference/config/next-config-js/turbo).
	+ A subset of [Webpack loaders](/docs/app/api-reference/config/next-config-js/turbo#configuring-webpack-loaders) are supported in Turbopack.
* Babel (`.babelrc`)
	+ Turbopack leverages the [SWC](/docs/architecture/nextjs-compiler#why-swc) compiler for all transpilation and optimizations. This means that Babel is not included by default.
	+ If you have a `.babelrc` file, you might no longer need it because Next.js includes common Babel plugins as SWC transforms that can be enabled. You can read more about this in the [compiler documentation](/docs/architecture/nextjs-compiler#supported-features).
	+ If you still need to use Babel after verifying your particular use case is not covered, you can leverage Turbopack's [support for custom webpack loaders](/docs/app/api-reference/config/next-config-js/turbo#configuring-webpack-loaders) to include `babel-loader`.
* Creating a root layout automatically in App Router.
	+ This behavior is currently not supported since it changes input files, instead, an error will be shown for you to manually add a root layout in the desired location.
* `@next/font` (legacy font support).
	+ `@next/font` is deprecated in favor of `next/font`. [`next/font`](/docs/app/building-your-application/optimizing/fonts) is fully supported with Turbopack.
* [Relay transforms](/docs/architecture/nextjs-compiler#relay)
	+ We are planning to implement this in the future.
* Blocking `.css` imports in `pages/_document.tsx`
	+ Currently with webpack Next.js blocks importing `.css` files in `pages/_document.tsx`
	+ We are planning to implement this warning in the future.
* [`experimental.typedRoutes`](/docs/app/api-reference/config/next-config-js/typedRoutes)
	+ We are planning to implement this in the future.
* `experimental.nextScriptWorkers`
	+ We are planning to implement this in the future.
* `experimental.sri.algorithm`
	+ We are planning to implement this in the future.
* `experimental.fallbackNodePolyfills`
	+ We are planning to implement this in the future.
* `experimental.esmExternals`
	+ We are currently not planning to support the legacy esmExternals configuration in Next.js with Turbopack.
* [AMP](/docs/pages/building-your-application/configuring/amp).
	+ We are currently not planning to support AMP in Next.js with Turbopack.
* Yarn PnP
	+ We are currently not planning to support Yarn PnP in Next.js with Turbopack.
* [`experimental.urlImports`](/docs/app/api-reference/config/next-config-js/urlImports)
	+ We are currently not planning to support `experimental.urlImports` in Next.js with Turbopack.
* [`:import` and `:export` ICSS rules](https://github.com/css-modules/icss)
	+ We are currently not planning to support `:import` and `:export` ICSS rules in Next.js with Turbopack as [Lightning CSS](https://lightningcss.dev/css-modules.html) the CSS parser Turbopack uses does not support these rules.
* `unstable_allowDynamic` configuration in edge runtime

## [Examples](#examples)

### [Generating Trace Files](#generating-trace-files)

Trace files allow the Next.js team to investigate and improve performance metrics and memory usage. To generate a trace file, append `NEXT_TURBOPACK_TRACING=1` to the `next dev --turbopack` command, this will generate a `.next/trace-turbopack` file.

When reporting issues related to Turbopack performance and memory usage, please include the trace file in your [GitHub](https://github.com/vercel/next.js) issue.

Was this helpful?



## Functions: after | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unstable_after)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)after# after

`after` allows you to schedule work to be executed after a response (or prerender) is finished. This is useful for tasks and other side effects that should not block the response, such as logging and analytics.

It can be used in [Server Components](/docs/app/building-your-application/rendering/server-components) (including [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)), [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations), [Route Handlers](/docs/app/building-your-application/routing/route-handlers), and [Middleware](/docs/app/building-your-application/routing/middleware).

The function accepts a callback that will be executed after the response (or prerender) is finished:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { after } from 'next/server'
// Custom logging function
import { log } from '@/app/utils'

export default function Layout({ children }: { children: React.ReactNode }) {
 after(() =\> {
 // Execute after the layout is rendered and sent to the user
 log()
 })
 return \{children}\
}
\`\`\`

> **Good to know:** `after` is not a [Dynamic API](/docs/app/building-your-application/rendering/server-components#dynamic-apis) and calling it does not cause a route to become dynamic. If it's used within a static page, the callback will execute at build time, or whenever a page is revalidated.

## [Reference](#reference)

### [Parameters](#parameters)

* A callback function which will be executed after the response (or prerender) is finished.

### [Duration](#duration)

`after` will run for the platform's default or configured max duration of your route. If your platform supports it, you can configure the timeout limit using the [`maxDuration`](/docs/app/api-reference/file-conventions/route-segment-config#maxduration) route segment config.

## [Good to know](#good-to-know)

* `after` will be executed even if the response didn't complete successfully. Including when an error is thrown or when `notFound` or `redirect` is called.
* You can use React `cache` to deduplicate functions called inside `after`.
* `after` can be nested inside other `after` calls, for example, you can create utility functions that wrap `after` calls to add additional functionality.

## [Alternatives](#alternatives)

The use case for `after` is to process secondary tasks without blocking the primary response. It's similar to using the platform's [`waitUntil()`](https://vercel.com/docs/functions/functions-api-reference) or removing `await` from a promise, but with the following differences:

* **`waitUntil()`**: accepts a promise and enqueues a task to be executed during the lifecycle of the request, whereas `after` accepts a callback that will be executed **after** the response is finished.
* **Removing `await`**: starts executing during the response, which uses resources. It's also not reliable in serverless environments as the function stops computation immediately after the response is sent, potentially interrupting the task.

We recommend using `after` as it has been designed to consider other Next.js APIs and contexts.

## [Examples](#examples)

### [With request APIs](#with-request-apis)

You can use request APIs such as [`cookies`](/docs/app/api-reference/functions/cookies) and [`headers`](/docs/app/api-reference/functions/headers) inside `after` in [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) and [Route Handlers](/docs/app/api-reference/file-conventions/route). This is useful for logging activity after a mutation. For example:

app/api/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'

export async function POST(request: Request) {
 // Perform mutation
 // ...

 // Log user activity for analytics
 after(async () =\> {
 const userAgent = (await headers().get('user\-agent')) \|\| 'unknown'
 const sessionCookie =
 (await cookies().get('session\-id'))?.value \|\| 'anonymous'

 logUserAction({ sessionCookie, userAgent })
 })

 return new Response(JSON.stringify({ status: 'success' }), {
 status: 200,
 headers: { 'Content\-Type': 'application/json' },
 })
}
\`\`\`

However, you cannot use these request APIs inside `after` in [Server Components](/docs/app/building-your-application/rendering/server-components). This is because Next.js needs to know which part of the tree access the request APIs to support [Partial Prerendering](/docs/app/building-your-application/rendering/partial-prerendering), but `after` runs after React's rendering lifecycle.

| Version History | Description |
| --- | --- |
| `v15.1.0` | `after` became stable. |
| `v15.0.0-rc` | `unstable_after` introduced. |

Was this helpful?



## CLI: create-next-app | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/cli/create-next-app)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[CLI](/docs/app/api-reference/cli)create\-next\-app# create\-next\-app

The `create-next-app` CLI allow you to create a new Next.js application using the default template or an [example](https://github.com/vercel/next.js/tree/canary/examples) from a public GitHub repository. It is the easiest way to get started with Next.js.

Basic usage:

Terminal\`\`\`
npx create\-next\-app@latest \[project\-name] \[options]
\`\`\`
## [Reference](#reference)

The following options are available:

| Options | Description |
| --- | --- |
| `-h` or `--help` | Show all available options |
| `-v` or `--version` | Output the version number |
| `--no-*` | Negate default options. E.g. `--no-eslint` |
| `--ts` or `--typescript` | Initialize as a TypeScript project (default) |
| `--js` or `--javascript` | Initialize as a JavaScript project |
| `--tailwind` | Initialize with Tailwind CSS config (default) |
| `--eslint` | Initialize with ESLint config |
| `--app` | Initialize as an App Router project |
| `--src-dir` | Initialize inside a `src/` directory |
| `--turbopack` | Enable Turbopack by default for development |
| `--import-alias ` | Specify import alias to use (default "@/\*") |
| `--empty` | Initialize an empty project |
| `--use-npm` | Explicitly tell the CLI to bootstrap the application using npm |
| `--use-pnpm` | Explicitly tell the CLI to bootstrap the application using pnpm |
| `--use-yarn` | Explicitly tell the CLI to bootstrap the application using Yarn |
| `--use-bun` | Explicitly tell the CLI to bootstrap the application using Bun |
| `-e` or `--example [name] [github-url]` | An example to bootstrap the app with |
| `--example-path ` | Specify the path to the example separately |
| `--reset-preferences` | Explicitly tell the CLI to reset any stored preferences |
| `--skip-install` | Explicitly tell the CLI to skip installing packages |
| `--yes` | Use previous preferences or defaults for all options |

## [Examples](#examples)

### [With the default template](#with-the-default-template)

To create a new app using the default template, run the following command in your terminal:

Terminal\`\`\`
npx create\-next\-app@latest
\`\`\`
You will then be asked the following prompts:

Terminal\`\`\`
What is your project named? my\-app
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a \`src/\` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack for \`next dev\`? No / Yes
Would you like to customize the import alias (\`@/\*\` by default)? No / Yes
\`\`\`
Once you've answered the prompts, a new project will be created with your chosen configuration.

### [With an official Next.js example](#with-an-official-nextjs-example)

To create a new app using an official Next.js example, use the `--example` flag. For example:

Terminal\`\`\`
npx create\-next\-app@latest \-\-example \[example\-name] \[your\-project\-name]
\`\`\`
You can view a list of all available examples along with setup instructions in the [Next.js repository](https://github.com/vercel/next.js/tree/canary/examples).

### [With any public GitHub example](#with-any-public-github-example)

To create a new app using any public GitHub example, use the `--example` option with the GitHub repo's URL. For example:

Terminal\`\`\`
npx create\-next\-app@latest \-\-example "https://github.com/.../" \[your\-project\-name]
\`\`\`Was this helpful?



## Functions: forbidden | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/forbidden)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)forbidden# forbidden

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The `forbidden` function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`forbidden.js` file](/docs/app/api-reference/file-conventions/forbidden).

To start using `forbidden`, enable the experimental [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 experimental: {
 authInterrupts: true,
 },
}

export default nextConfig
\`\`\`

`forbidden` can be invoked in [Server Components](/docs/app/building-your-application/rendering/server-components), [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations), and [Route Handlers](/docs/app/building-your-application/routing/route-handlers).

app/auth/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
 const session = await verifySession()

 // Check if the user has the 'admin' role
 if (session.role !== 'admin') {
 forbidden()
 }

 // Render the admin page for authorized users
 return \\
}
\`\`\`

## [Good to know](#good-to-know)

* The `forbidden` function cannot be called in the [root layout](/docs/app/building-your-application/routing/layouts-and-templates#root-layout-required).

## [Examples](#examples)

### [Role\-based route protection](#role-based-route-protection)

You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.

app/admin/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
 const session = await verifySession()

 // Check if the user has the 'admin' role
 if (session.role !== 'admin') {
 forbidden()
 }

 // Render the admin page for authorized users
 return (
 \
 \Admin Dashboard\
 \Welcome, {session.user.name}!\
 \
 )
}
\`\`\`

### [Mutations with Server Actions](#mutations-with-server-actions)

When implementing mutations in Server Actions, you can use `forbidden` to only allow users with a specific role to update sensitive data.

app/actions/update\-role.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateRole(formData: FormData) {
 const session = await verifySession()

 // Ensure only admins can update roles
 if (session.role !== 'admin') {
 forbidden()
 }

 // Perform the role update for authorized users
 // ...
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.1.0` | `forbidden` introduced. |

## Next Steps

[### forbidden.js

API reference for the forbidden.js special file.](/docs/app/api-reference/file-conventions/forbidden)Was this helpful?



## Metadata Files: robots.txt | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[File Conventions](/docs/app/api-reference/file-conventions)[Metadata Files](/docs/app/api-reference/file-conventions/metadata)robots.txt# robots.txt

Add or generate a `robots.txt` file that matches the [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots.txt#Standard) in the **root** of `app` directory to tell search engine crawlers which URLs they can access on your site.

## [Static `robots.txt`](#static-robotstxt)

app/robots.txt\`\`\`
User\-Agent: \*
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
\`\`\`
## [Generate a Robots file](#generate-a-robots-file)

Add a `robots.js` or `robots.ts` file that returns a [`Robots` object](#robots-object).

> **Good to know**: `robots.js` is a special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/building-your-application/caching#dynamic-apis) or [dynamic config](/docs/app/building-your-application/caching#segment-config-options) option.

app/robots.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
 return {
 rules: {
 userAgent: '\*',
 allow: '/',
 disallow: '/private/',
 },
 sitemap: 'https://acme.com/sitemap.xml',
 }
}
\`\`\`

Output:

\`\`\`
User\-Agent: \*
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
\`\`\`
### [Customizing specific user agents](#customizing-specific-user-agents)

You can customise how individual search engine bots crawl your site by passing an array of user agents to the `rules` property. For example:

app/robots.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
 return {
 rules: \[
 {
 userAgent: 'Googlebot',
 allow: \['/'],
 disallow: '/private/',
 },
 {
 userAgent: \['Applebot', 'Bingbot'],
 disallow: \['/'],
 },
 ],
 sitemap: 'https://acme.com/sitemap.xml',
 }
}
\`\`\`

Output:

\`\`\`
User\-Agent: Googlebot
Allow: /
Disallow: /private/

User\-Agent: Applebot
Disallow: /

User\-Agent: Bingbot
Disallow: /

Sitemap: https://acme.com/sitemap.xml
\`\`\`
### [Robots object](#robots-object)

\`\`\`
type Robots = {
 rules:
 \| {
 userAgent?: string \| string\[]
 allow?: string \| string\[]
 disallow?: string \| string\[]
 crawlDelay?: number
 }
 \| Array\
 sitemap?: string \| string\[]
 host?: string
}
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `robots` introduced. |

Was this helpful?



## CLI: next CLI | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/cli/next)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[CLI](/docs/app/api-reference/cli)next CLI# next CLI

The Next.js CLI allows you to develop, build, start your application, and more.

Basic usage:

Terminal\`\`\`
npx next \[command] \[options]
\`\`\`
## [Reference](#reference)

The following options are available:

| Options | Description |
| --- | --- |
| `-h` or `--help` | Shows all available options |
| `-v` or `--version` | Outputs the Next.js version number |

### [Commands](#commands)

The following commands are available:

| Command | Description |
| --- | --- |
| [`dev`](#next-dev-options) | Starts Next.js in development mode with Hot Module Reloading, error reporting, and more. |
| [`build`](#next-build-options) | Creates an optimized production build of your application. Displaying information about each route. |
| [`start`](#next-start-options) | Starts Next.js in production mode. The application should be compiled with `next build` first. |
| [`info`](#next-info-options) | Prints relevant details about the current system which can be used to report Next.js bugs. |
| [`lint`](#next-lint-options) | Runs ESLint for all files in the `/src`, `/app`, `/pages`, `/components`, and `/lib` directories. It also provides a guided setup to install any required dependencies if ESLint it is not already configured in your application. |
| [`telemetry`](#next-telemetry-options) | Allows you to enable or disable Next.js' completely anonymous telemetry collection. |

> **Good to know**: Running `next` without a command is an alias for `next dev`.

### [`next dev` options](#next-dev-options)

`next dev` starts the application in development mode with Hot Module Reloading (HMR), error reporting, and more. The following options are available when running `next dev`:

| Option | Description |
| --- | --- |
| `-h, --help` | Show all available options. |
| `[directory]` | A directory in which to build the application. If not provided, current directory is used. |
| `--turbopack` | Starts development mode using [Turbopack](/docs/app/api-reference/turbopack). |
| `-p` or `--port ` | Specify a port number on which to start the application. Default: 3000, env: PORT |
| `-H`or `--hostname ` | Specify a hostname on which to start the application. Useful for making the application available for other devices on the network. Default: 0\.0\.0\.0 |
| `--experimental-https` | Starts the server with HTTPS and generates a self\-signed certificate. |
| `--experimental-https-key ` | Path to a HTTPS key file. |
| `--experimental-https-cert ` | Path to a HTTPS certificate file. |
| `--experimental-https-ca ` | Path to a HTTPS certificate authority file. |
| `--experimental-upload-trace ` | Reports a subset of the debugging trace to a remote HTTP URL. |

### [`next build` options](#next-build-options)

`next build` creates an optimized production build of your application. The output displays information about each route. For example:

Terminal\`\`\`
Route (app) Size First Load JS
┌ ○ /\_not\-found 0 B 0 kB
└ ƒ /products/\[id] 0 B 0 kB

○ (Static) prerendered as static content
ƒ (Dynamic) server\-rendered on demand
\`\`\`
* **Size**: The size of assets downloaded when navigating to the page client\-side. The size for each route only includes its dependencies.
* **First Load JS**: The size of assets downloaded when visiting the page from the server. The amount of JS shared by all is shown as a separate metric.

Both of these values are [**compressed with gzip**](/docs/app/api-reference/config/next-config-js/compress). The first load is indicated by green, yellow, or red. Aim for green for performant applications.

The following options are available for the `next build` command:

| Option | Description |
| --- | --- |
| `-h, --help` | Show all available options. |
| `[directory]` | A directory on which to build the application. If not provided, the current directory will be used. |
| `-d` or `--debug` | Enables a more verbose build output. With this flag enabled additional build output like rewrites, redirects, and headers will be shown. |
|  |  |
| `--profile` | Enables production [profiling for React](https://react.dev/reference/react/Profiler). |
| `--no-lint` | Disables linting. |
| `--no-mangling` | Disables [mangling](https://en.wikipedia.org/wiki/Name_mangling). This may affect performance and should only be used for debugging purposes. |
| `--experimental-app-only` | Builds only App Router routes. |
| `--experimental-build-mode [mode]` | Uses an experimental build mode. (choices: "compile", "generate", default: "default") |

### [`next start` options](#next-start-options)

`next start` starts the application in production mode. The application should be compiled with [`next build`](#next-build-options) first.

The following options are available for the `next start` command:

| Option | Description |
| --- | --- |
| `-h` or `--help` | Show all available options. |
| `[directory]` | A directory on which to start the application. If no directory is provided, the current directory will be used. |
| `-p` or `--port ` | Specify a port number on which to start the application. (default: 3000, env: PORT) |
| `-H` or `--hostname ` | Specify a hostname on which to start the application (default: 0\.0\.0\.0\). |
| `--keepAliveTimeout ` | Specify the maximum amount of milliseconds to wait before closing the inactive connections. |

### [`next info` options](#next-info-options)

`next info` prints relevant details about the current system which can be used to report Next.js bugs when opening a [GitHub issue](https://github.com/vercel/next.js/issues). This information includes Operating System platform/arch/version, Binaries (Node.js, npm, Yarn, pnpm), package versions (`next`, `react`, `react-dom`), and more.

The output should look like this:

Terminal\`\`\`
Operating System:
 Platform: darwin
 Arch: arm64
 Version: Darwin Kernel Version 23\.6\.0
 Available memory (MB): 65536
 Available CPU cores: 10
Binaries:
 Node: 20\.12\.0
 npm: 10\.5\.0
 Yarn: 1\.22\.19
 pnpm: 9\.6\.0
Relevant Packages:
 next: 15\.0\.0\-canary.115 // Latest available version is detected (15\.0\.0\-canary.115\).
 eslint\-config\-next: 14\.2\.5
 react: 19\.0\.0\-rc
 react\-dom: 19\.0\.0
 typescript: 5\.5\.4
Next.js Config:
 output: N/A
\`\`\`
The following options are available for the `next info` command:

| Option | Description |
| --- | --- |
| `-h` or `--help` | Show all available options |
| `--verbose` | Collects additional information for debugging. |

### [`next lint` options](#next-lint-options)

`next lint` runs ESLint for all files in the `pages/`, `app/`, `components/`, `lib/`, and `src/` directories. It also provides a guided setup to install any required dependencies if ESLint is not already configured in your application.

The following options are available for the `next lint` command:

| Option | Description |
| --- | --- |
| `[directory]` | A base directory on which to lint the application. If not provided, the current directory will be used. |
| `-d, --dir, ` | Include directory, or directories, to run ESLint. |
| `--file, ` | Include file, or files, to run ESLint. |
| `--ext, [exts...]` | Specify JavaScript file extensions. (default: \[".js", ".mjs", ".cjs", ".jsx", ".ts", ".mts", ".cts", ".tsx"]) |
| `-c, --config, ` | Uses this configuration file, overriding all other configuration options. |
| `--resolve-plugins-relative-to, ` | Specify a directory where plugins should be resolved from. |
| `--strict` | Creates a `.eslintrc.json` file using the Next.js strict configuration. |
| `--rulesdir, ` | Uses additional rules from this directory(s). |
| `--fix` | Automatically fix linting issues. |
| `--fix-type ` | Specify the types of fixes to apply (e.g., problem, suggestion, layout). |
| `--ignore-path ` | Specify a file to ignore. |
| `--no-ignore ` | Disables the `--ignore-path` option. |
| `--quiet` | Reports errors only. |
| `--max-warnings [maxWarnings]` | Specify the number of warnings before triggering a non\-zero exit code. (default: \-1\) |
| `-o, --output-file, ` | Specify a file to write report to. |
| `-f, --format, ` | Uses a specific output format. |
| `--no-inline-config` | Prevents comments from changing config or rules. |
| `--report-unused-disable-directives-severity ` | Specify severity level for unused eslint\-disable directives. (choices: "error", "off", "warn") |
| `--no-cache` | Disables caching. |
| `--cache-location, ` | Specify a location for cache. |
| `--cache-strategy, [cacheStrategy]` | Specify a strategy to use for detecting changed files in the cache. (default: "metadata") |
| `--error-on-unmatched-pattern` | Reports errors when any file patterns are unmatched. |
| `-h, --help` | Displays this message. |

### [`next telemetry` options](#next-telemetry-options)

Next.js collects **completely anonymous** telemetry data about general usage. Participation in this anonymous program is optional, and you can opt\-out if you prefer not to share information.

The following options are available for the `next telemetry` command:

| Option | Description |
| --- | --- |
| `-h, --help` | Show all available options. |
| `--enable` | Enables Next.js' telemetry collection. |
| `--disable` | Disables Next.js' telemetry collection. |

Learn more about [Telemetry](/telemetry).

## [Examples](#examples)

### [Changing the default port](#changing-the-default-port)

By default, Next.js uses `http://localhost:3000` during development and with `next start`. The default port can be changed with the `-p` option, like so:

Terminal\`\`\`
next dev \-p 4000
\`\`\`
Or using the `PORT` environment variable:

Terminal\`\`\`
PORT=4000 next dev
\`\`\`

> **Good to know**: `PORT` cannot be set in `.env` as booting up the HTTP server happens before any other code is initialized.

### [Using HTTPS during development](#using-https-during-development)

For certain use cases like webhooks or authentication, you can use [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS) to have a secure environment on `localhost`. Next.js can generate a self\-signed certificate with `next dev` using the `--experimental-https` flag:

Terminal\`\`\`
next dev \-\-experimental\-https
\`\`\`
With the generated certificate, the Next.js development server will exist at `https://localhost:3000`. The default port `3000` is used unless a port is specified with `-p`, `--port`, or `PORT`.

You can also provide a custom certificate and key with `--experimental-https-key` and `--experimental-https-cert`. Optionally, you can provide a custom CA certificate with `--experimental-https-ca` as well.

Terminal\`\`\`
next dev \-\-experimental\-https \-\-experimental\-https\-key ./certificates/localhost\-key.pem \-\-experimental\-https\-cert ./certificates/localhost.pem
\`\`\`
`next dev --experimental-https` is only intended for development and creates a locally trusted certificate with [`mkcert`](https://github.com/FiloSottile/mkcert). In production, use properly issued certificates from trusted authorities.

> **Good to know**: When deploying to Vercel, HTTPS is [automatically configured](https://vercel.com/docs/security/encryption) for your Next.js application.

### [Configuring a timeout for downstream proxies](#configuring-a-timeout-for-downstream-proxies)

When deploying Next.js behind a downstream proxy (e.g. a load\-balancer like AWS ELB/ALB), it's important to configure Next's underlying HTTP server with [keep\-alive timeouts](https://nodejs.org/api/http.html#http_server_keepalivetimeout) that are *larger* than the downstream proxy's timeouts. Otherwise, once a keep\-alive timeout is reached for a given TCP connection, Node.js will immediately terminate that connection without notifying the downstream proxy. This results in a proxy error whenever it attempts to reuse a connection that Node.js has already terminated.

To configure the timeout values for the production Next.js server, pass `--keepAliveTimeout` (in milliseconds) to `next start`, like so:

Terminal\`\`\`
next start \-\-keepAliveTimeout 70000
\`\`\`
### [Passing Node.js arguments](#passing-nodejs-arguments)

You can pass any [node arguments](https://nodejs.org/api/cli.html#cli_node_options_options) to `next` commands. For example:

Terminal\`\`\`
NODE\_OPTIONS='\-\-throw\-deprecation' next
NODE\_OPTIONS='\-r esm' next
NODE\_OPTIONS='\-\-inspect' next
\`\`\`Was this helpful?



## API Reference: File Conventions | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)File Conventions# File Conventions

[### default.js

API Reference for the default.js file.](/docs/app/api-reference/file-conventions/default)[### error.js

API reference for the error.js special file.](/docs/app/api-reference/file-conventions/error)[### forbidden.js

API reference for the forbidden.js special file.](/docs/app/api-reference/file-conventions/forbidden)[### instrumentation.js

API reference for the instrumentation.js file.](/docs/app/api-reference/file-conventions/instrumentation)[### layout.js

API reference for the layout.js file.](/docs/app/api-reference/file-conventions/layout)[### loading.js

API reference for the loading.js file.](/docs/app/api-reference/file-conventions/loading)[### mdx\-components.js

API reference for the mdx\-components.js file.](/docs/app/api-reference/file-conventions/mdx-components)[### middleware.js

API reference for the middleware.js file.](/docs/app/api-reference/file-conventions/middleware)[### not\-found.js

API reference for the not\-found.js file.](/docs/app/api-reference/file-conventions/not-found)[### page.js

API reference for the page.js file.](/docs/app/api-reference/file-conventions/page)[### route.js

API reference for the route.js special file.](/docs/app/api-reference/file-conventions/route)[### Route Segment Config

Learn about how to configure options for Next.js route segments.](/docs/app/api-reference/file-conventions/route-segment-config)[### template.js

API Reference for the template.js file.](/docs/app/api-reference/file-conventions/template)[### unauthorized.js

API reference for the unauthorized.js special file.](/docs/app/api-reference/file-conventions/unauthorized)[### Metadata Files

API documentation for the metadata file conventions.](/docs/app/api-reference/file-conventions/metadata)Was this helpful?



## File Conventions: instrumentation.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)instrumentation.js# instrumentation.js

The `instrumentation.js|ts` file is used to integrate observability tools into your application, allowing you to track the performance and behavior, and to debug issues in production.

To use it, place the file in the **root** of your application or inside a [`src` folder](/docs/app/building-your-application/configuring/src-directory) if using one.

## [Exports](#exports)

### [`register` (optional)](#register-optional)

The file exports a `register` function that is called **once** when a new Next.js server instance is initiated. `register` can be an async function.

instrumentation.tsTypeScriptJavaScriptTypeScript\`\`\`
import { registerOTel } from '@vercel/otel'

export function register() {
 registerOTel('next\-app')
}
\`\`\`

### [`onRequestError` (optional)](#onrequesterror-optional)

You can optionally export an `onRequestError` function to track **server** errors to any custom observability provider.

* If you're running any async tasks in `onRequestError`, make sure they're awaited. `onRequestError` will be triggered when the Next.js server captures the error.
* The `error` instance might not be the original error instance thrown, as it may be processed by React if encountered during Server Components rendering. If this happens, you can use `digest` property on an error to identify the actual error type.

instrumentation.tsTypeScriptJavaScriptTypeScript\`\`\`
import { type Instrumentation } from 'next'

export const onRequestError: Instrumentation.onRequestError = async (
 err,
 request,
 context
) =\> {
 await fetch('https://.../report\-error', {
 method: 'POST',
 body: JSON.stringify({
 message: err.message,
 request,
 context,
 }),
 headers: {
 'Content\-Type': 'application/json',
 },
 })
}
\`\`\`

#### [Parameters](#parameters)

The function accepts three parameters: `error`, `request`, and `context`.

Types\`\`\`
export function onRequestError(
 error: { digest: string } \& Error,
 request: {
 path: string // resource path, e.g. /blog?name=foo
 method: string // request method. e.g. GET, POST, etc
 headers: { \[key: string]: string }
 },
 context: {
 routerKind: 'Pages Router' \| 'App Router' // the router type
 routePath: string // the route file path, e.g. /app/blog/\[dynamic]
 routeType: 'render' \| 'route' \| 'action' \| 'middleware' // the context in which the error occurred
 renderSource:
 \| 'react\-server\-components'
 \| 'react\-server\-components\-payload'
 \| 'server\-rendering'
 revalidateReason: 'on\-demand' \| 'stale' \| undefined // undefined is a normal request without revalidation
 renderType: 'dynamic' \| 'dynamic\-resume' // 'dynamic\-resume' for PPR
 }
): void \| Promise\
\`\`\`
* `error`: The caught error itself (type is always `Error`), and a `digest` property which is the unique ID of the error.
* `request`: Read\-only request information associated with the error.
* `context`: The context in which the error occurred. This can be the type of router (App or Pages Router), and/or (Server Components (`'render'`), Route Handlers (`'route'`), Server Actions (`'action'`), or Middleware (`'middleware'`)).

### [Specifying the runtime](#specifying-the-runtime)

The `instrumentation.js` file works in both the Node.js and Edge runtime, however, you can use `process.env.NEXT_RUNTIME` to target a specific runtime.

instrumentation.js\`\`\`
export function register() {
 if (process.env.NEXT\_RUNTIME === 'edge') {
 return require('./register.edge')
 } else {
 return require('./register.node')
 }
}

export function onRequestError() {
 if (process.env.NEXT\_RUNTIME === 'edge') {
 return require('./on\-request\-error.edge')
 } else {
 return require('./on\-request\-error.node')
 }
}
\`\`\`
## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `onRequestError` introduced, `instrumentation` stable |
| `v14.0.4` | Turbopack support for `instrumentation` |
| `v13.2.0` | `instrumentation` introduced as an experimental feature |

## Learn more about Instrumentation

[### Instrumentation

Learn how to use instrumentation to run code at server startup in your Next.js app](/docs/app/building-your-application/optimizing/instrumentation)Was this helpful?



## Metadata Files: manifest.json | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[File Conventions](/docs/app/api-reference/file-conventions)[Metadata Files](/docs/app/api-reference/file-conventions/metadata)manifest.json# manifest.json

Add or generate a `manifest.(json|webmanifest)` file that matches the [Web Manifest Specification](https://developer.mozilla.org/docs/Web/Manifest) in the **root** of `app` directory to provide information about your web application for the browser.

## [Static Manifest file](#static-manifest-file)

app/manifest.json \| app/manifest.webmanifest\`\`\`
{
 "name": "My Next.js Application",
 "short\_name": "Next.js App",
 "description": "An application built with Next.js",
 "start\_url": "/"
 // ...
}
\`\`\`
## [Generate a Manifest file](#generate-a-manifest-file)

Add a `manifest.js` or `manifest.ts` file that returns a [`Manifest` object](#manifest-object).

> Good to know: `manifest.js` is special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/building-your-application/caching#dynamic-apis) or [dynamic config](/docs/app/building-your-application/caching#segment-config-options) option.

app/manifest.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
 return {
 name: 'Next.js App',
 short\_name: 'Next.js App',
 description: 'Next.js App',
 start\_url: '/',
 display: 'standalone',
 background\_color: '\#fff',
 theme\_color: '\#fff',
 icons: \[
 {
 src: '/favicon.ico',
 sizes: 'any',
 type: 'image/x\-icon',
 },
 ],
 }
}
\`\`\`

### [Manifest Object](#manifest-object)

The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the `MetadataRoute.Manifest` type in your code editor if using [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin) or see the [MDN](https://developer.mozilla.org/docs/Web/Manifest) docs.

Was this helpful?



## Getting Started: Fetching data and streaming | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started/data-fetching-and-streaming)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Fetching data and streaming# How to fetch data and stream

This page will walk you through how you can fetch data in [Server Components](#server-components) and [Client Components](#client-components). As well as how to to [stream](#streaming) content that depends on data.

## [Fetching data](#fetching-data)

### [Server Components](#server-components)

You can fetch data in Server Components using:

1. The [`fetch` API](#with-the-fetch-api)
2. An [ORM or database](#with-an-orm-or-database)

#### [With the `fetch` API](#with-the-fetch-api)

To fetch data with the `fetch` API, turn your component into an asynchronous function, and await the `fetch` call. For example:

app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page() {
 const data = await fetch('https://api.vercel.app/blog')
 const posts = await data.json()
 return (
 \
 {posts.map((post) =\> (
 \{post.title}\
 ))}
 \
 )
}
\`\`\`

#### [With an ORM or database](#with-an-orm-or-database)

You can fetch data with an ORM or database by turning your component into an asynchronous function, and awaiting the call:

app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { db, posts } from '@/lib/db'

export default async function Page() {
 const allPosts = await db.select().from(posts)
 return (
 \
 {allPosts.map((post) =\> (
 \{post.title}\
 ))}
 \
 )
}
\`\`\`

### [Client Components](#client-components)

There are two ways to fetch data in Client Components, using:

1. React's [`use` hook](https://react.dev/reference/react/use)
2. A community library like [SWR](https://swr.vercel.app/) or [React Query](https://tanstack.com/query/latest)

#### [With the `use` hook](#with-the-use-hook)

You can use React's [`use` hook](https://react.dev/reference/react/use) to [stream](#streaming) data from the server to client. Start by fetching data in your Server component, and pass the promise to your Client Component as prop:

app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Posts from '@/app/ui/posts
import { Suspense } from 'react'

export default function Page() {
 // Don't await the data fetching function
 const posts = getPosts()

 return (
 \Loading...\}\>
 \
 \
 )
}
\`\`\`

Then, in your Client Component, use the `use` hook read the promise:

app/ui/posts.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'
import { use } from 'react'

export default function Posts({
 posts,
}: {
 posts: Promise\
}) {
 const posts = use(posts)

 return (
 \
 {posts.map((post) =\> (
 \{post.title}\
 ))}
 \
 )
}
\`\`\`

In the example above, you need to wrap the `` component in a [`` boundary](https://react.dev/reference/react/Suspense). This means the fallback will be shown while the promise is being resolved. Learn more about [streaming](#streaming).

#### [Community libraries](#community-libraries)

You can use a community library like [SWR](https://swr.vercel.app/) or [React Query](https://tanstack.com/query/latest) to fetch data in Client Components. These libraries have their own semantics for caching, streaming, and other features. For example, with SWR:

app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'
import useSWR from 'swr'

const fetcher = (url) =\> fetch(url).then((r) =\> r.json())

export default function BlogPage() {
 const { data, error, isLoading } = useSWR(
 'https://api.vercel.app/blog',
 fetcher
 )

 if (isLoading) return \Loading...\
 if (error) return \Error: {error.message}\

 return (
 \
 {data.map((post: { id: string; title: string }) =\> (
 \{post.title}\
 ))}
 \
 )
}
\`\`\`

## [Streaming](#streaming)

> **Warning:** The content below assumes the [`dynamicIO` config option](/docs/app/api-reference/config/next-config-js/dynamicIO) is enabled in your application. The flag was introduced in Next.js 15 canary.

When using `async/await` in Server Components, Next.js will opt into **dynamic rendering**. This means the data will be fetched and rendered on the server for every user request. If there are any slow data requests, the whole route will be blocked from rendering.

To improve the initial load time and user experience, you can use streaming to break up the page's HTML into smaller chunks and progressively send those chunks from the server to the client.


There are two ways you can implement streaming in your application:

1. With the [`loading.js` file](#with-loadingjs)
2. With React's [`` component](#with-suspense)

### [With `loading.js`](#with-loadingjs)

You can create a `loading.js` file in the same folder as your page to stream the **entire page** while the data is being fetched. For example, to stream `app/blog/page.js`, add the file inside the `app/blog` folder.


app/blog/loading.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Loading() {
 // Define the Loading UI here
 return \Loading...\
}
\`\`\`

On navigation, the user will immediately see the layout and a [loading state](#creating-meaningful-loading-states) while the page is being rendered. The new content will then be automatically swapped in once rendering is complete.


Behind\-the\-scenes, `loading.js` will be nested inside `layout.js`, and will automatically wrap the `page.js` file and any children below in a `` boundary.


This approach works well for route segments (layouts and pages), but for more granular streaming, you can use ``.

### [With ``](#with-suspense)

`` allows you to be more granular about what parts of the page to stream. For example, you can immediately show any page content that falls outside of the `` boundary, and stream in the list of blog posts inside the boundary.

app/blog/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { Suspense } from 'react'
import BlogList from '@/components/BlogList'
import BlogListSkeleton from '@/components/BlogListSkeleton'

export default function BlogPage() {
 return (
 \
 {/\* This content will be sent to the client immediately \*/}
 \
 \Welcome to the Blog\
 \Read the latest posts below.\
 \
 \
 {/\* Any content wrapped in a \ boundary will be streamed \*/}
 \}\>
 \
 \
 \
 \
 )
}
\`\`\`

### [Creating meaningful loading states](#creating-meaningful-loading-states)

An instant loading state is fallback UI that is shown immediately to the user after navigation. For the best user experience, we recommend designing loading states that are meaningful and help users understand the app is responding. For example, you can use skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc.

In development, you can preview and inspect the loading state of your components using the [React Devtools](https://react.dev/learn/react-developer-tools).

## API Reference

Learn more about the features mentioned in this page by reading the API Reference.[### fetch

API reference for the extended fetch function.](/docs/app/api-reference/functions/fetch)[### loading.js

API reference for the loading.js file.](/docs/app/api-reference/file-conventions/loading)Was this helpful?



## Functions: useRouter | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-router)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)useRouter# useRouter

The `useRouter` hook allows you to programmatically change routes inside [Client Components](/docs/app/building-your-application/rendering/client-components).

> **Recommendation:** Use the [`` component](/docs/app/building-your-application/routing/linking-and-navigating#link-component) for navigation unless you have a specific requirement for using `useRouter`.

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
 const router = useRouter()

 return (
 \ router.push('/dashboard')}\>
 Dashboard
 \
 )
}
\`\`\`

## [`useRouter()`](#userouter)

* `router.push(href: string, { scroll: boolean })`: Perform a client\-side navigation to the provided route. Adds a new entry into the [browser’s history](https://developer.mozilla.org/docs/Web/API/History_API) stack.
* `router.replace(href: string, { scroll: boolean })`: Perform a client\-side navigation to the provided route without adding a new entry into the [browser’s history stack](https://developer.mozilla.org/docs/Web/API/History_API).
* `router.refresh()`: Refresh the current route. Making a new request to the server, re\-fetching data requests, and re\-rendering Server Components. The client will merge the updated React Server Component payload without losing unaffected client\-side React (e.g. `useState`) or browser state (e.g. scroll position).
* `router.prefetch(href: string)`: [Prefetch](/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching) the provided route for faster client\-side transitions.
* `router.back()`: Navigate back to the previous route in the browser’s history stack.
* `router.forward()`: Navigate forwards to the next page in the browser’s history stack.

> **Good to know**:
> 
> 
> * You must not send untrusted or unsanitized URLs to `router.push` or `router.replace`, as this can open your site to cross\-site scripting (XSS) vulnerabilities. For example, `javascript:` URLs sent to `router.push` or `router.replace` will be executed in the context of your page.
> * The `` component automatically prefetch routes as they become visible in the viewport.
> * `refresh()` could re\-produce the same result if fetch requests are cached. Other Dynamic APIs like `cookies` and `headers` could also change the response.

### [Migrating from `next/router`](#migrating-from-nextrouter)

* The `useRouter` hook should be imported from `next/navigation` and not `next/router` when using the App Router
* The `pathname` string has been removed and is replaced by [`usePathname()`](/docs/app/api-reference/functions/use-pathname)
* The `query` object has been removed and is replaced by [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params)
* `router.events` has been replaced. [See below.](#router-events)

[View the full migration guide](/docs/app/building-your-application/upgrading/app-router-migration).

## [Examples](#examples)

### [Router events](#router-events)

You can listen for page changes by composing other Client Component hooks like `usePathname` and `useSearchParams`.

app/components/navigation\-events.js\`\`\`
'use client'

import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'

export function NavigationEvents() {
 const pathname = usePathname()
 const searchParams = useSearchParams()

 useEffect(() =\> {
 const url = \`${pathname}?${searchParams}\`
 console.log(url)
 // You can now use the current URL
 // ...
 }, \[pathname, searchParams])

 return '...'
}
\`\`\`
Which can be imported into a layout.

app/layout.js\`\`\`
import { Suspense } from 'react'
import { NavigationEvents } from './components/navigation\-events'

export default function Layout({ children }) {
 return (
 \
 \
 {children}

 \
 \
 \
 \
 \
 )
}
\`\`\`

> **Good to know**: `` is wrapped in a [`Suspense` boundary](/docs/app/building-your-application/routing/loading-ui-and-streaming#example) because[`useSearchParams()`](/docs/app/api-reference/functions/use-search-params) causes client\-side rendering up to the closest `Suspense` boundary during [static rendering](/docs/app/building-your-application/rendering/server-components#static-rendering-default). [Learn more](/docs/app/api-reference/functions/use-search-params#behavior).

### [Disabling scroll to top](#disabling-scroll-to-top)

By default, Next.js will scroll to the top of the page when navigating to a new route. You can disable this behavior by passing `scroll: false` to `router.push()` or `router.replace()`.

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
 const router = useRouter()

 return (
 \ router.push('/dashboard', { scroll: false })}
 \>
 Dashboard
 \
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `useRouter` from `next/navigation` introduced. |

Was this helpful?



## File Conventions: default.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/default)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)default.js# default.js

The `default.js` file is used to render a fallback within [Parallel Routes](/docs/app/building-your-application/routing/parallel-routes) when Next.js cannot recover a [slot's](/docs/app/building-your-application/routing/parallel-routes#slots) active state after a full\-page load.

During [soft navigation](/docs/app/building-your-application/routing/linking-and-navigating#5-soft-navigation), Next.js keeps track of the active *state* (subpage) for each slot. However, for hard navigations (full\-page load), Next.js cannot recover the active state. In this case, a `default.js` file can be rendered for subpages that don't match the current URL.

Consider the following folder structure. The `@team` slot has a `settings` page, but `@analytics` does not.


When navigating to `/settings`, the `@team` slot will render the `settings` page while maintaining the currently active page for the `@analytics` slot.

On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, a `404` is rendered instead.

Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page.

## [Reference](#reference)

### [`params` (optional)](#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) from the root segment down to the slot's subpages. For example:

app/\[artist]/@sidebar/default.jsTypeScriptJavaScriptTypeScript\`\`\`
export default async function Default({
 params,
}: {
 params: Promise\
}) {
 const artist = (await params).artist
}
\`\`\`

| Example | URL | `params` |
| --- | --- | --- |
| `app/[artist]/@sidebar/default.js` | `/zack` | `Promise` |
| `app/[artist]/[album]/@sidebar/default.js` | `/zack/next` | `Promise` |

* Since the `params` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
	+ In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
## Learn more about Parallel Routes

[### Parallel Routes

Simultaneously render one or more pages in the same view that can be navigated independently. A pattern for highly dynamic applications.](/docs/app/building-your-application/routing/parallel-routes)Was this helpful?



## Functions: userAgent | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/userAgent)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)userAgent# userAgent

The `userAgent` helper extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional properties and methods to interact with the user agent object from the request.

middleware.tsTypeScriptJavaScriptTypeScript\`\`\`
import { NextRequest, NextResponse, userAgent } from 'next/server'

export function middleware(request: NextRequest) {
 const url = request.nextUrl
 const { device } = userAgent(request)
 const viewport = device.type === 'mobile' ? 'mobile' : 'desktop'
 url.searchParams.set('viewport', viewport)
 return NextResponse.rewrite(url)
}
\`\`\`

## [`isBot`](#isbot)

A boolean indicating whether the request comes from a known bot.

## [`browser`](#browser)

An object containing information about the browser used in the request.

* `name`: A string representing the browser's name, or `undefined` if not identifiable.
* `version`: A string representing the browser's version, or `undefined`.

## [`device`](#device)

An object containing information about the device used in the request.

* `model`: A string representing the model of the device, or `undefined`.
* `type`: A string representing the type of the device, such as `console`, `mobile`, `tablet`, `smarttv`, `wearable`, `embedded`, or `undefined`.
* `vendor`: A string representing the vendor of the device, or `undefined`.

## [`engine`](#engine)

An object containing information about the browser's engine.

* `name`: A string representing the engine's name. Possible values include: `Amaya`, `Blink`, `EdgeHTML`, `Flow`, `Gecko`, `Goanna`, `iCab`, `KHTML`, `Links`, `Lynx`, `NetFront`, `NetSurf`, `Presto`, `Tasman`, `Trident`, `w3m`, `WebKit` or `undefined`.
* `version`: A string representing the engine's version, or `undefined`.

## [`os`](#os)

An object containing information about the operating system.

* `name`: A string representing the name of the OS, or `undefined`.
* `version`: A string representing the version of the OS, or `undefined`.

## [`cpu`](#cpu)

An object containing information about the CPU architecture.

* `architecture`: A string representing the architecture of the CPU. Possible values include: `68k`, `amd64`, `arm`, `arm64`, `armhf`, `avr`, `ia32`, `ia64`, `irix`, `irix64`, `mips`, `mips64`, `pa-risc`, `ppc`, `sparc`, `sparc64` or `undefined`
Was this helpful?



## Components: Font | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/components/font)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Components](/docs/app/api-reference/components)Font# Font Module

This API reference will help you understand how to use [`next/font/google`](/docs/app/building-your-application/optimizing/fonts#google-fonts) and [`next/font/local`](/docs/app/building-your-application/optimizing/fonts#local-fonts). For features and usage, please see the [Optimizing Fonts](/docs/app/building-your-application/optimizing/fonts) page.

### [Font Function Arguments](#font-function-arguments)

For usage, review [Google Fonts](/docs/app/building-your-application/optimizing/fonts#google-fonts) and [Local Fonts](/docs/app/building-your-application/optimizing/fonts#local-fonts).

| Key | `font/google` | `font/local` | Type | Required |
| --- | --- | --- | --- | --- |
| [`src`](#src) |  |  | String or Array of Objects | Yes |
| [`weight`](#weight) |  |  | String or Array | Required/Optional |
| [`style`](#style) |  |  | String or Array | \- |
| [`subsets`](#subsets) |  |  | Array of Strings | \- |
| [`axes`](#axes) |  |  | Array of Strings | \- |
| [`display`](#display) |  |  | String | \- |
| [`preload`](#preload) |  |  | Boolean | \- |
| [`fallback`](#fallback) |  |  | Array of Strings | \- |
| [`adjustFontFallback`](#adjustfontfallback) |  |  | Boolean or String | \- |
| [`variable`](#variable) |  |  | String | \- |
| [`declarations`](#declarations) |  |  | Array of Objects | \- |

### [`src`](#src)

The path of the font file as a string or an array of objects (with type `Array`) relative to the directory where the font loader function is called.

Used in `next/font/local`

* Required

Examples:

* `src:'./fonts/my-font.woff2'` where `my-font.woff2` is placed in a directory named `fonts` inside the `app` directory
* `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
* if the font loader function is called in `app/page.tsx` using `src:'../styles/fonts/my-font.ttf'`, then `my-font.ttf` is placed in `styles/fonts` at the root of the project

### [`weight`](#weight)

The font [`weight`](https://fonts.google.com/knowledge/glossary/weight) with the following possibilities:

* A string with possible values of the weights available for the specific font or a range of values if it's a [variable](https://fonts.google.com/variablefonts) font
* An array of weight values if the font is not a [variable google font](https://fonts.google.com/variablefonts). It applies to `next/font/google` only.

Used in `next/font/google` and `next/font/local`

* Required if the font being used is **not** [variable](https://fonts.google.com/variablefonts)

Examples:

* `weight: '400'`: A string for a single weight value \- for the font [`Inter`](https://fonts.google.com/specimen/Inter?query=inter), the possible values are `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'` or `'variable'` where `'variable'` is the default)
* `weight: '100 900'`: A string for the range between `100` and `900` for a variable font
* `weight: ['100','400','900']`: An array of 3 possible values for a non variable font

### [`style`](#style)

The font [`style`](https://developer.mozilla.org/docs/Web/CSS/font-style) with the following possibilities:

* A string [value](https://developer.mozilla.org/docs/Web/CSS/font-style#values) with default value of `'normal'`
* An array of style values if the font is not a [variable google font](https://fonts.google.com/variablefonts). It applies to `next/font/google` only.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `style: 'italic'`: A string \- it can be `normal` or `italic` for `next/font/google`
* `style: 'oblique'`: A string \- it can take any value for `next/font/local` but is expected to come from [standard font styles](https://developer.mozilla.org/docs/Web/CSS/font-style)
* `style: ['italic','normal']`: An array of 2 values for `next/font/google` \- the values are from `normal` and `italic`

### [`subsets`](#subsets)

The font [`subsets`](https://fonts.google.com/knowledge/glossary/subsetting) defined by an array of string values with the names of each subset you would like to be [preloaded](/docs/app/building-your-application/optimizing/fonts#specifying-a-subset). Fonts specified via `subsets` will have a link preload tag injected into the head when the [`preload`](#preload) option is true, which is the default.

Used in `next/font/google`

* Optional

Examples:

* `subsets: ['latin']`: An array with the subset `latin`

You can find a list of all subsets on the Google Fonts page for your font.

### [`axes`](#axes)

Some variable fonts have extra `axes` that can be included. By default, only the font weight is included to keep the file size down. The possible values of `axes` depend on the specific font.

Used in `next/font/google`

* Optional

Examples:

* `axes: ['slnt']`: An array with value `slnt` for the `Inter` variable font which has `slnt` as additional `axes` as shown [here](https://fonts.google.com/variablefonts?vfquery=inter#font-families). You can find the possible `axes` values for your font by using the filter on the [Google variable fonts page](https://fonts.google.com/variablefonts#font-families) and looking for axes other than `wght`

### [`display`](#display)

The font [`display`](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display) with possible string [values](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display#values) of `'auto'`, `'block'`, `'swap'`, `'fallback'` or `'optional'` with default value of `'swap'`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `display: 'optional'`: A string assigned to the `optional` value

### [`preload`](#preload)

A boolean value that specifies whether the font should be [preloaded](/docs/app/building-your-application/optimizing/fonts#preloading) or not. The default is `true`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `preload: false`

### [`fallback`](#fallback)

The fallback font to use if the font cannot be loaded. An array of strings of fallback fonts with no default.

* Optional

Used in `next/font/google` and `next/font/local`

Examples:

* `fallback: ['system-ui', 'arial']`: An array setting the fallback fonts to `system-ui` or `arial`

### [`adjustFontFallback`](#adjustfontfallback)

* For `next/font/google`: A boolean value that sets whether an automatic fallback font should be used to reduce [Cumulative Layout Shift](https://web.dev/cls/). The default is `true`.
* For `next/font/local`: A string or boolean `false` value that sets whether an automatic fallback font should be used to reduce [Cumulative Layout Shift](https://web.dev/cls/). The possible values are `'Arial'`, `'Times New Roman'` or `false`. The default is `'Arial'`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `adjustFontFallback: false`: for `next/font/google`
* `adjustFontFallback: 'Times New Roman'`: for `next/font/local`

### [`variable`](#variable)

A string value to define the CSS variable name to be used if the style is applied with the [CSS variable method](#css-variables).

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `variable: '--my-font'`: The CSS variable `--my-font` is declared

### [`declarations`](#declarations)

An array of font face [descriptor](https://developer.mozilla.org/docs/Web/CSS/@font-face#descriptors) key\-value pairs that define the generated `@font-face` further.

Used in `next/font/local`

* Optional

Examples:

* `declarations: [{ prop: 'ascent-override', value: '90%' }]`

## [Applying Styles](#applying-styles)

You can apply the font styles in three ways:

* [`className`](#classname)
* [`style`](#style-1)
* [CSS Variables](#css-variables)

### [`className`](#classname)

Returns a read\-only CSS `className` for the loaded font to be passed to an HTML element.

\`\`\`
\Hello, Next.js!\
\`\`\`
### [`style`](#style-1)

Returns a read\-only CSS `style` object for the loaded font to be passed to an HTML element, including `style.fontFamily` to access the font family name and fallback fonts.

\`\`\`
\Hello World\
\`\`\`
### [CSS Variables](#css-variables)

If you would like to set your styles in an external style sheet and specify additional options there, use the CSS variable method.

In addition to importing the font, also import the CSS file where the CSS variable is defined and set the variable option of the font loader object as follows:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { Inter } from 'next/font/google'
import styles from '../styles/component.module.css'

const inter = Inter({
 variable: '\-\-font\-inter',
})
\`\`\`

To use the font, set the `className` of the parent container of the text you would like to style to the font loader's `variable` value and the `className` of the text to the `styles` property from the external CSS file.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
\
 \Hello World\
\
\`\`\`

Define the `text` selector class in the `component.module.css` CSS file as follows:

styles/component.module.css\`\`\`
.text {
 font\-family: var(\-\-font\-inter);
 font\-weight: 200;
 font\-style: italic;
}
\`\`\`
In the example above, the text `Hello World` is styled using the `Inter` font and the generated font fallback with `font-weight: 200` and `font-style: italic`.

## [Using a font definitions file](#using-a-font-definitions-file)

Every time you call the `localFont` or Google font function, that font will be hosted as one instance in your application. Therefore, if you need to use the same font in multiple places, you should load it in one place and import the related font object where you need it. This is done using a font definitions file.

For example, create a `fonts.ts` file in a `styles` folder at the root of your app directory.

Then, specify your font definitions as follows:

styles/fonts.tsTypeScriptJavaScriptTypeScript\`\`\`
import { Inter, Lora, Source\_Sans\_3 } from 'next/font/google'
import localFont from 'next/font/local'

// define your variable fonts
const inter = Inter()
const lora = Lora()
// define 2 weights of a non\-variable font
const sourceCodePro400 = Source\_Sans\_3({ weight: '400' })
const sourceCodePro700 = Source\_Sans\_3({ weight: '700' })
// define a custom local font where GreatVibes\-Regular.ttf is stored in the styles folder
const greatVibes = localFont({ src: './GreatVibes\-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
\`\`\`

You can now use these definitions in your code as follows:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

export default function Page() {
 return (
 \
 \Hello world using Inter font\
 \Hello world using Lora font\
 \
 Hello world using Source\_Sans\_3 font with weight 700
 \
 \My title in Great Vibes font\
 \
 )
}
\`\`\`

To make it easier to access the font definitions in your code, you can define a path alias in your `tsconfig.json` or `jsconfig.json` files as follows:

tsconfig.json\`\`\`
{
 "compilerOptions": {
 "paths": {
 "@/fonts": \["./styles/fonts"]
 }
 }
}
\`\`\`
You can now import any font definition as follows:

app/about/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { greatVibes, sourceCodePro400 } from '@/fonts'
\`\`\`

## [Version Changes](#version-changes)

| Version | Changes |
| --- | --- |
| `v13.2.0` | `@next/font` renamed to `next/font`. Installation no longer required. |
| `v13.0.0` | `@next/font` was added. |

Was this helpful?



## File Conventions: unauthorized.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)unauthorized.js# unauthorized.js

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The **unauthorized** file is used to render UI when the [`unauthorized`](/docs/app/api-reference/functions/unauthorized) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `401` status code.

app/unauthorized.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Login from '@/app/components/Login'

export default function Unauthorized() {
 return (
 \
 \401 \- Unauthorized\
 \Please log in to access this page.\
 \
 \
 )
}
\`\`\`

## [Reference](#reference)

### [Props](#props)

`unauthorized.js` components do not accept any props.

## [Examples](#examples)

### [Displaying login UI to unauthenticated users](#displaying-login-ui-to-unauthenticated-users)

You can use [`unauthorized`](/docs/app/api-reference/functions/unauthorized) function to render the `unauthorized.js` file with a login UI.

app/dashboard/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/server'

export default async function DashboardPage() {
 const session = await verifySession()

 if (!session) {
 unauthorized()
 }

 return \Dashboard\
}
\`\`\`

app/unauthorized.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
 return (
 \
 \401 \- Unauthorized\
 \Please log in to access this page.\
 \
 \
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.1.0` | `unauthorized.js` introduced. |

## Next Steps

[### unauthorized

API Reference for the unauthorized function.](/docs/app/api-reference/functions/unauthorized)Was this helpful?



## Functions: draftMode | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/draft-mode)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)draftMode# draftMode

`draftMode` is an **async** function allows you to enable and disable [Draft Mode](/docs/app/building-your-application/configuring/draft-mode), as well as check if Draft Mode is enabled in a [Server Component](/docs/app/building-your-application/rendering/server-components).

app/page.tsTypeScriptJavaScriptTypeScript\`\`\`
import { draftMode } from 'next/headers'

export default async function Page() {
 const { isEnabled } = await draftMode()
}
\`\`\`

## [Reference](#reference)

The following methods and properties are available:

| Method | Description |
| --- | --- |
| `isEnabled` | A boolean value that indicates if Draft Mode is enabled. |
| `enable()` | Enables Draft Mode in a Route Handler by setting a cookie (`__prerender_bypass`). |
| `disable()` | Disables Draft Mode in a Route Handler by deleting a cookie. |

## [Good to know](#good-to-know)

* `draftMode` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
	+ In version 14 and earlier, `draftMode` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* A new bypass cookie value will be generated each time you run `next build`. This ensures that the bypass cookie can’t be guessed.
* To test Draft Mode locally over HTTP, your browser will need to allow third\-party cookies and local storage access.

## [Examples](#examples)

### [Enabling Draft Mode](#enabling-draft-mode)

To enable Draft Mode, create a new [Route Handler](/docs/app/building-your-application/routing/route-handlers) and call the `enable()` method:

app/draft/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
 const draft = await draftMode()
 draft().enable()
 return new Response('Draft mode is enabled')
}
\`\`\`

### [Disabling Draft Mode](#disabling-draft-mode)

By default, the Draft Mode session ends when the browser is closed.

To disable Draft Mode manually, call the `disable()` method in your [Route Handler](/docs/app/building-your-application/routing/route-handlers):

app/draft/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
 const draft = await draftMode()
 draft().disable()
 return new Response('Draft mode is disabled')
}
\`\`\`

Then, send a request to invoke the Route Handler. If calling the route using the [`` component](/docs/app/api-reference/components/link), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.

### [Checking if Draft Mode is enabled](#checking-if-draft-mode-is-enabled)

You can check if Draft Mode is enabled in a Server Component with the `isEnabled` property:

app/page.tsTypeScriptJavaScriptTypeScript\`\`\`
import { draftMode } from 'next/headers'

export default async function Page() {
 const { isEnabled } = await draftMode()
 return (
 \
 \My Blog Post\
 \Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}\
 \
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `draftMode` is now an async function. A [codemod](/docs/app/building-your-application/upgrading/codemods#150) is available. |
| `v13.4.0` | `draftMode` introduced. |

## Next Steps

Learn how to use Draft Mode with this step\-by\-step guide.[### Draft Mode

Next.js has draft mode to toggle between static and dynamic pages. You can learn how it works with App Router here.](/docs/app/building-your-application/configuring/draft-mode)Was this helpful?



## Functions: revalidateTag | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)revalidateTag# revalidateTag

`revalidateTag` allows you to purge [cached data](/docs/app/building-your-application/caching) on\-demand for a specific cache tag.

> **Good to know**:
> 
> 
> * `revalidateTag` is available in both [Node.js and Edge runtimes](/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes).
> * `revalidateTag` only invalidates the cache when the path is next visited. This means calling `revalidateTag` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.

## [Parameters](#parameters)

\`\`\`
revalidateTag(tag: string): void;
\`\`\`
* `tag`: A string representing the cache tag associated with the data you want to revalidate. Must be less than or equal to 256 characters. This value is case\-sensitive.

You can add tags to `fetch` as follows:

\`\`\`
fetch(url, { next: { tags: \[...] } });
\`\`\`
## [Returns](#returns)

`revalidateTag` does not return a value.

## [Examples](#examples)

### [Server Action](#server-action)

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
 await addPost()
 revalidateTag('posts')
}
\`\`\`

### [Route Handler](#route-handler)

app/api/revalidate/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextRequest } from 'next/server'
import { revalidateTag } from 'next/cache'

export async function GET(request: NextRequest) {
 const tag = request.nextUrl.searchParams.get('tag')
 revalidateTag(tag)
 return Response.json({ revalidated: true, now: Date.now() })
}
\`\`\`
Was this helpful?



## Functions: permanentRedirect | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)permanentRedirect# permanentRedirect

The `permanentRedirect` function allows you to redirect the user to another URL. `permanentRedirect` can be used in Server Components, Client Components, [Route Handlers](/docs/app/building-your-application/routing/route-handlers), and [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations).

When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 308 (Permanent) HTTP redirect response to the caller.

If a resource doesn't exist, you can use the [`notFound` function](/docs/app/api-reference/functions/not-found) instead.

> **Good to know**: If you prefer to return a 307 (Temporary) HTTP redirect instead of 308 (Permanent), you can use the [`redirect` function](/docs/app/api-reference/functions/redirect) instead.

## [Parameters](#parameters)

The `permanentRedirect` function accepts two arguments:

\`\`\`
permanentRedirect(path, type)
\`\`\`

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | The URL to redirect to. Can be a relative or absolute path. |
| `type` | `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform. |

By default, `permanentRedirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.

The `type` parameter has no effect when used in Server Components.

## [Returns](#returns)

`permanentRedirect` does not return a value.

## [Example](#example)

Invoking the `permanentRedirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.

app/team/\[id]/page.js\`\`\`
import { permanentRedirect } from 'next/navigation'

async function fetchTeam(id) {
 const res = await fetch('https://...')
 if (!res.ok) return undefined
 return res.json()
}

export default async function Profile({ params }) {
 const team = await fetchTeam(params.id)
 if (!team) {
 permanentRedirect('/login')
 }

 // ...
}
\`\`\`

> **Good to know**: `permanentRedirect` does not require you to use `return permanentRedirect()` as it uses the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

## Next Steps

[### redirect

API Reference for the redirect function.](/docs/app/api-reference/functions/redirect)Was this helpful?



## Metadata Files: favicon, icon, and apple-icon | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[File Conventions](/docs/app/api-reference/file-conventions)[Metadata Files](/docs/app/api-reference/file-conventions/metadata)favicon, icon, and apple\-icon# favicon, icon, and apple\-icon

The `favicon`, `icon`, or `apple-icon` file conventions allow you to set icons for your application.

They are useful for adding app icons that appear in places like web browser tabs, phone home screens, and search engine results.

There are two ways to set app icons:

* [Using image files (.ico, .jpg, .png)](#image-files-ico-jpg-png)
* [Using code to generate an icon (.js, .ts, .tsx)](#generate-icons-using-code-js-ts-tsx)

## [Image files (.ico, .jpg, .png)](#image-files-ico-jpg-png)

Use an image file to set an app icon by placing a `favicon`, `icon`, or `apple-icon` image file within your `/app` directory.
The `favicon` image can only be located in the top level of `app/`.

Next.js will evaluate the file and automatically add the appropriate tags to your app's `` element.

| File convention | Supported file types | Valid locations |
| --- | --- | --- |
| [`favicon`](#favicon) | `.ico` | `app/` |
| [`icon`](#icon) | `.ico`, `.jpg`, `.jpeg`, `.png`, `.svg` | `app/**/*` |
| [`apple-icon`](#apple-icon) | `.jpg`, `.jpeg`, `.png` | `app/**/*` |

### [`favicon`](#favicon)

Add a `favicon.ico` image file to the root `/app` route segment.

\ output\`\`\`
\
\`\`\`
### [`icon`](#icon)

Add an `icon.(ico|jpg|jpeg|png|svg)` image file.

\ output\`\`\`
\"
 type="image/\"
 sizes="\"
/\>
\`\`\`
### [`apple-icon`](#apple-icon)

Add an `apple-icon.(jpg|jpeg|png)` image file.

\ output\`\`\`
\"
 type="image/\"
 sizes="\"
/\>
\`\`\`

> **Good to know**:
> 
> 
> * You can set multiple icons by adding a number suffix to the file name. For example, `icon1.png`, `icon2.png`, etc. Numbered files will sort lexically.
> * Favicons can only be set in the root `/app` segment. If you need more granularity, you can use [`icon`](#icon).
> * The appropriate `` tags and attributes such as `rel`, `href`, `type`, and `sizes` are determined by the icon type and metadata of the evaluated file.
> * For example, a 32 by 32px `.png` file will have `type="image/png"` and `sizes="32x32"` attributes.
> * `sizes="any"` is added to icons when the extension is `.svg` or the image size of the file is not determined. More details in this [favicon handbook](https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs).

## [Generate icons using code (.js, .ts, .tsx)](#generate-icons-using-code-js-ts-tsx)

In addition to using [literal image files](#image-files-ico-jpg-png), you can programmatically **generate** icons using code.

Generate an app icon by creating an `icon` or `apple-icon` route that default exports a function.

| File convention | Supported file types |
| --- | --- |
| `icon` | `.js`, `.ts`, `.tsx` |
| `apple-icon` | `.js`, `.ts`, `.tsx` |

The easiest way to generate an icon is to use the [`ImageResponse`](/docs/app/api-reference/functions/image-response) API from `next/og`.

app/icon.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ImageResponse } from 'next/og'

// Image metadata
export const size = {
 width: 32,
 height: 32,
}
export const contentType = 'image/png'

// Image generation
export default function Icon() {
 return new ImageResponse(
 (
 // ImageResponse JSX element
 \
 A
 \
 ),
 // ImageResponse options
 {
 // For convenience, we can re\-use the exported icons size metadata
 // config to also set the ImageResponse's width and height.
 ...size,
 }
 )
}
\`\`\`

\ output\`\`\`
\" type="image/png" sizes="32x32" /\>
\`\`\`

> **Good to know**:
> 
> 
> * By default, generated icons are [**statically optimized**](/docs/app/building-your-application/rendering/server-components#static-rendering-default) (generated at build time and cached) unless they use [Dynamic APIs](/docs/app/building-your-application/rendering/server-components#server-rendering-strategies#dynamic-apis) or uncached data.
> * You can generate multiple icons in the same file using [`generateImageMetadata`](/docs/app/api-reference/functions/generate-image-metadata).
> * You cannot generate a `favicon` icon. Use [`icon`](#icon) or a [favicon.ico](#favicon) file instead.
> * App icons are special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/building-your-application/caching#dynamic-apis) or [dynamic config](/docs/app/building-your-application/caching#segment-config-options) option.

### [Props](#props)

The default export function receives the following props:

#### [`params` (optional)](#params-optional)

An object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) object from the root segment down to the segment `icon` or `apple-icon` is colocated in.

app/shop/\[slug]/icon.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Icon({ params }: { params: { slug: string } }) {
 // ...
}
\`\`\`

| Route | URL | `params` |
| --- | --- | --- |
| `app/shop/icon.js` | `/shop` | `undefined` |
| `app/shop/[slug]/icon.js` | `/shop/1` | `{ slug: '1' }` |
| `app/shop/[tag]/[item]/icon.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |

### [Returns](#returns)

The default export function should return a `Blob` \| `ArrayBuffer` \| `TypedArray` \| `DataView` \| `ReadableStream` \| `Response`.

> **Good to know**: `ImageResponse` satisfies this return type.

### [Config exports](#config-exports)

You can optionally configure the icon's metadata by exporting `size` and `contentType` variables from the `icon` or `apple-icon` route.

| Option | Type |
| --- | --- |
| [`size`](#size) | `{ width: number; height: number }` |
| [`contentType`](#contenttype) | `string` \- [image MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types) |

#### [`size`](#size)

icon.tsx \| apple\-icon.tsxTypeScriptJavaScriptTypeScript\`\`\`
export const size = { width: 32, height: 32 }

export default function Icon() {}
\`\`\`

\ output\`\`\`
\
\`\`\`
#### [`contentType`](#contenttype)

icon.tsx \| apple\-icon.tsxTypeScriptJavaScriptTypeScript\`\`\`
export const contentType = 'image/png'

export default function Icon() {}
\`\`\`

\ output\`\`\`
\
\`\`\`
#### [Route Segment Config](#route-segment-config)

`icon` and `apple-icon` are specialized [Route Handlers](/docs/app/building-your-application/routing/route-handlers) that can use the same [route segment configuration](/docs/app/api-reference/file-conventions/route-segment-config) options as Pages and Layouts.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.3.0` | `favicon` `icon` and `apple-icon` introduced |

Was this helpful?



## API Reference: Edge Runtime | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/edge)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)Edge Runtime# Edge Runtime

The Next.js Edge Runtime is used for Middleware and supports the following APIs:

## [Network APIs](#network-apis)

| API | Description |
| --- | --- |
| [`Blob`](https://developer.mozilla.org/docs/Web/API/Blob) | Represents a blob |
| [`fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API) | Fetches a resource |
| [`FetchEvent`](https://developer.mozilla.org/docs/Web/API/FetchEvent) | Represents a fetch event |
| [`File`](https://developer.mozilla.org/docs/Web/API/File) | Represents a file |
| [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData) | Represents form data |
| [`Headers`](https://developer.mozilla.org/docs/Web/API/Headers) | Represents HTTP headers |
| [`Request`](https://developer.mozilla.org/docs/Web/API/Request) | Represents an HTTP request |
| [`Response`](https://developer.mozilla.org/docs/Web/API/Response) | Represents an HTTP response |
| [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) | Represents URL search parameters |
| [`WebSocket`](https://developer.mozilla.org/docs/Web/API/WebSocket) | Represents a websocket connection |

## [Encoding APIs](#encoding-apis)

| API | Description |
| --- | --- |
| [`atob`](https://developer.mozilla.org/en-US/docs/Web/API/atob) | Decodes a base\-64 encoded string |
| [`btoa`](https://developer.mozilla.org/en-US/docs/Web/API/btoa) | Encodes a string in base\-64 |
| [`TextDecoder`](https://developer.mozilla.org/docs/Web/API/TextDecoder) | Decodes a Uint8Array into a string |
| [`TextDecoderStream`](https://developer.mozilla.org/docs/Web/API/TextDecoderStream) | Chainable decoder for streams |
| [`TextEncoder`](https://developer.mozilla.org/docs/Web/API/TextEncoder) | Encodes a string into a Uint8Array |
| [`TextEncoderStream`](https://developer.mozilla.org/docs/Web/API/TextEncoderStream) | Chainable encoder for streams |

## [Stream APIs](#stream-apis)

| API | Description |
| --- | --- |
| [`ReadableStream`](https://developer.mozilla.org/docs/Web/API/ReadableStream) | Represents a readable stream |
| [`ReadableStreamBYOBReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader) | Represents a reader of a ReadableStream |
| [`ReadableStreamDefaultReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamDefaultReader) | Represents a reader of a ReadableStream |
| [`TransformStream`](https://developer.mozilla.org/docs/Web/API/TransformStream) | Represents a transform stream |
| [`WritableStream`](https://developer.mozilla.org/docs/Web/API/WritableStream) | Represents a writable stream |
| [`WritableStreamDefaultWriter`](https://developer.mozilla.org/docs/Web/API/WritableStreamDefaultWriter) | Represents a writer of a WritableStream |

## [Crypto APIs](#crypto-apis)

| API | Description |
| --- | --- |
| [`crypto`](https://developer.mozilla.org/docs/Web/API/Window/crypto) | Provides access to the cryptographic functionality of the platform |
| [`CryptoKey`](https://developer.mozilla.org/docs/Web/API/CryptoKey) | Represents a cryptographic key |
| [`SubtleCrypto`](https://developer.mozilla.org/docs/Web/API/SubtleCrypto) | Provides access to common cryptographic primitives, like hashing, signing, encryption or decryption |

## [Web Standard APIs](#web-standard-apis)

| API | Description |
| --- | --- |
| [`AbortController`](https://developer.mozilla.org/docs/Web/API/AbortController) | Allows you to abort one or more DOM requests as and when desired |
| [`Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) | Represents an array of values |
| [`ArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) | Represents a generic, fixed\-length raw binary data buffer |
| [`Atomics`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Atomics) | Provides atomic operations as static methods |
| [`BigInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt) | Represents a whole number with arbitrary precision |
| [`BigInt64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array) | Represents a typed array of 64\-bit signed integers |
| [`BigUint64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array) | Represents a typed array of 64\-bit unsigned integers |
| [`Boolean`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean) | Represents a logical entity and can have two values: `true` and `false` |
| [`clearInterval`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearInterval) | Cancels a timed, repeating action which was previously established by a call to `setInterval()` |
| [`clearTimeout`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearTimeout) | Cancels a timed, repeating action which was previously established by a call to `setTimeout()` |
| [`console`](https://developer.mozilla.org/docs/Web/API/Console) | Provides access to the browser's debugging console |
| [`DataView`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/DataView) | Represents a generic view of an `ArrayBuffer` |
| [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | Represents a single moment in time in a platform\-independent format |
| [`decodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) | Decodes a Uniform Resource Identifier (URI) previously created by `encodeURI` or by a similar routine |
| [`decodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) | Decodes a Uniform Resource Identifier (URI) component previously created by `encodeURIComponent` or by a similar routine |
| [`DOMException`](https://developer.mozilla.org/docs/Web/API/DOMException) | Represents an error that occurs in the DOM |
| [`encodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) | Encodes a Uniform Resource Identifier (URI) by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF\-8 encoding of the character |
| [`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) | Encodes a Uniform Resource Identifier (URI) component by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF\-8 encoding of the character |
| [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error) | Represents an error when trying to execute a statement or accessing a property |
| [`EvalError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/EvalError) | Represents an error that occurs regarding the global function `eval()` |
| [`Float32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) | Represents a typed array of 32\-bit floating point numbers |
| [`Float64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) | Represents a typed array of 64\-bit floating point numbers |
| [`Function`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function) | Represents a function |
| [`Infinity`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Infinity) | Represents the mathematical Infinity value |
| [`Int8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) | Represents a typed array of 8\-bit signed integers |
| [`Int16Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) | Represents a typed array of 16\-bit signed integers |
| [`Int32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) | Represents a typed array of 32\-bit signed integers |
| [`Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl) | Provides access to internationalization and localization functionality |
| [`isFinite`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isFinite) | Determines whether a value is a finite number |
| [`isNaN`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isNaN) | Determines whether a value is `NaN` or not |
| [`JSON`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON) | Provides functionality to convert JavaScript values to and from the JSON format |
| [`Map`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map) | Represents a collection of values, where each value may occur only once |
| [`Math`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Math) | Provides access to mathematical functions and constants |
| [`Number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) | Represents a numeric value |
| [`Object`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object) | Represents the object that is the base of all JavaScript objects |
| [`parseFloat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseFloat) | Parses a string argument and returns a floating point number |
| [`parseInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseInt) | Parses a string argument and returns an integer of the specified radix |
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) | Represents the eventual completion (or failure) of an asynchronous operation, and its resulting value |
| [`Proxy`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Proxy) | Represents an object that is used to define custom behavior for fundamental operations (e.g. property lookup, assignment, enumeration, function invocation, etc) |
| [`queueMicrotask`](https://developer.mozilla.org/docs/Web/API/queueMicrotask) | Queues a microtask to be executed |
| [`RangeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RangeError) | Represents an error when a value is not in the set or range of allowed values |
| [`ReferenceError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError) | Represents an error when a non\-existent variable is referenced |
| [`Reflect`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Reflect) | Provides methods for interceptable JavaScript operations |
| [`RegExp`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RegExp) | Represents a regular expression, allowing you to match combinations of characters |
| [`Set`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Set) | Represents a collection of values, where each value may occur only once |
| [`setInterval`](https://developer.mozilla.org/docs/Web/API/setInterval) | Repeatedly calls a function, with a fixed time delay between each call |
| [`setTimeout`](https://developer.mozilla.org/docs/Web/API/setTimeout) | Calls a function or evaluates an expression after a specified number of milliseconds |
| [`SharedArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) | Represents a generic, fixed\-length raw binary data buffer |
| [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | Represents a sequence of characters |
| [`structuredClone`](https://developer.mozilla.org/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) | Creates a deep copy of a value |
| [`Symbol`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Symbol) | Represents a unique and immutable data type that is used as the key of an object property |
| [`SyntaxError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError) | Represents an error when trying to interpret syntactically invalid code |
| [`TypeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/TypeError) | Represents an error when a value is not of the expected type |
| [`Uint8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | Represents a typed array of 8\-bit unsigned integers |
| [`Uint8ClampedArray`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) | Represents a typed array of 8\-bit unsigned integers clamped to 0\-255 |
| [`Uint32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) | Represents a typed array of 32\-bit unsigned integers |
| [`URIError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/URIError) | Represents an error when a global URI handling function was used in a wrong way |
| [`URL`](https://developer.mozilla.org/docs/Web/API/URL) | Represents an object providing static methods used for creating object URLs |
| [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern) | Represents a URL pattern |
| [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) | Represents a collection of key/value pairs |
| [`WeakMap`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) | Represents a collection of key/value pairs in which the keys are weakly referenced |
| [`WeakSet`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) | Represents a collection of objects in which each object may occur only once |
| [`WebAssembly`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly) | Provides access to WebAssembly |

## [Next.js Specific Polyfills](#nextjs-specific-polyfills)

* [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage)

## [Environment Variables](#environment-variables)

You can use `process.env` to access [Environment Variables](/docs/app/building-your-application/configuring/environment-variables) for both `next dev` and `next build`.

## [Unsupported APIs](#unsupported-apis)

The Edge Runtime has some restrictions including:

* Native Node.js APIs **are not supported**. For example, you can't read or write to the filesystem.
* `node_modules` *can* be used, as long as they implement ES Modules and do not use native Node.js APIs.
* Calling `require` directly is **not allowed**. Use ES Modules instead.

The following JavaScript language features are disabled, and **will not work:**

| API | Description |
| --- | --- |
| [`eval`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/eval) | Evaluates JavaScript code represented as a string |
| [`new Function(evalString)`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function) | Creates a new function with the code provided as an argument |
| [`WebAssembly.compile`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/compile) | Compiles a WebAssembly module from a buffer source |
| [`WebAssembly.instantiate`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate) | Compiles and instantiates a WebAssembly module from a buffer source |

In rare cases, your code could contain (or import) some dynamic code evaluation statements which *can not be reached at runtime* and which can not be removed by treeshaking.
You can relax the check to allow specific files with your Middleware configuration:

middleware.ts\`\`\`
export const config = {
 unstable\_allowDynamic: \[
 // allows a single file
 '/lib/utilities.js',
 // use a glob to allow anything in the function\-bind 3rd party module
 '\*\*/node\_modules/function\-bind/\*\*',
 ],
}
\`\`\`
`unstable_allowDynamic` is a [glob](https://github.com/micromatch/micromatch#matching-features), or an array of globs, ignoring dynamic code evaluation for specific files. The globs are relative to your application root folder.

Be warned that if these statements are executed on the Edge, *they will throw and cause a runtime error*.

Was this helpful?



## Functions: redirect | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/redirect)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)redirect# redirect

The `redirect` function allows you to redirect the user to another URL. `redirect` can be used in [Server Components](/docs/app/building-your-application/rendering/server-components), [Route Handlers](/docs/app/building-your-application/routing/route-handlers), and [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations).

When used in a [streaming context](/docs/app/building-your-application/routing/loading-ui-and-streaming#what-is-streaming), this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.

If a resource doesn't exist, you can use the [`notFound` function](/docs/app/api-reference/functions/not-found) instead.

> **Good to know**:
> 
> 
> * In Server Actions and Route Handlers, `redirect` should be called after the `try/catch` block.
> * If you prefer to return a 308 (Permanent) HTTP redirect instead of 307 (Temporary), you can use the [`permanentRedirect` function](/docs/app/api-reference/functions/permanentRedirect) instead.

## [Parameters](#parameters)

The `redirect` function accepts two arguments:

\`\`\`
redirect(path, type)
\`\`\`

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | The URL to redirect to. Can be a relative or absolute path. |
| `type` | `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform. |

By default, `redirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.

The `type` parameter has no effect when used in Server Components.

## [Returns](#returns)

`redirect` does not return a value.

## [Example](#example)

### [Server Component](#server-component)

Invoking the `redirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.

app/team/\[id]/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { redirect } from 'next/navigation'

async function fetchTeam(id: string) {
 const res = await fetch('https://...')
 if (!res.ok) return undefined
 return res.json()
}

export default async function Profile({
 params,
}: {
 params: Promise\
}) {
 const { id } = await params
 const team = await fetchTeam(id)

 if (!team) {
 redirect('/login')
 }

 // ...
}
\`\`\`

> **Good to know**: `redirect` does not require you to use `return redirect()` as it uses the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

### [Client Component](#client-component)

`redirect` can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the [`useRouter`](/docs/app/api-reference/functions/use-router) hook.

app/client\-redirect.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { navigate } from './actions'

export function ClientRedirect() {
 return (
 \
 \
 \Submit\
 \
 )
}
\`\`\`

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { redirect } from 'next/navigation'

export async function navigate(data: FormData) {
 redirect(\`/posts/${data.get('id')}\`)
}
\`\`\`

## [FAQ](#faq)

### [Why does `redirect` use 307 and 308?](#why-does-redirect-use-307-and-308)

When using `redirect()` you may notice that the status codes used are `307` for a temporary redirect, and `308` for a permanent redirect. While traditionally a `302` was used for a temporary redirect, and a `301` for a permanent redirect, many browsers changed the request method of the redirect, from a `POST` to `GET` request when using a `302`, regardless of the origins request method.

Taking the following example of a redirect from `/users` to `/people`, if you make a `POST` request to `/users` to create a new user, and are conforming to a `302` temporary redirect, the request method will be changed from a `POST` to a `GET` request. This doesn't make sense, as to create a new user, you should be making a `POST` request to `/people`, and not a `GET` request.

The introduction of the `307` status code means that the request method is preserved as `POST`.

* `302` \- Temporary redirect, will change the request method from `POST` to `GET`
* `307` \- Temporary redirect, will preserve the request method as `POST`

The `redirect()` method uses a `307` by default, instead of a `302` temporary redirect, meaning your requests will *always* be preserved as `POST` requests.

[Learn more](https://developer.mozilla.org/docs/Web/HTTP/Redirections) about HTTP Redirects.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `redirect` introduced. |

## Next Steps

[### permanentRedirect

API Reference for the permanentRedirect function.](/docs/app/api-reference/functions/permanentRedirect)Was this helpful?



## API Reference: Functions | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)Functions# Functions

[### after

API Reference for the after function.](/docs/app/api-reference/functions/after)[### cacheLife

Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.](/docs/app/api-reference/functions/cacheLife)[### cacheTag

Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.](/docs/app/api-reference/functions/cacheTag)[### connection

API Reference for the connection function.](/docs/app/api-reference/functions/connection)[### cookies

API Reference for the cookies function.](/docs/app/api-reference/functions/cookies)[### draftMode

API Reference for the draftMode function.](/docs/app/api-reference/functions/draft-mode)[### fetch

API reference for the extended fetch function.](/docs/app/api-reference/functions/fetch)[### forbidden

API Reference for the forbidden function.](/docs/app/api-reference/functions/forbidden)[### generateImageMetadata

Learn how to generate multiple images in a single Metadata API special file.](/docs/app/api-reference/functions/generate-image-metadata)[### generateMetadata

Learn how to add Metadata to your Next.js application for improved search engine optimization (SEO) and web shareability.](/docs/app/api-reference/functions/generate-metadata)[### generateSitemaps

Learn how to use the generateSiteMaps function to create multiple sitemaps for your application.](/docs/app/api-reference/functions/generate-sitemaps)[### generateStaticParams

API reference for the generateStaticParams function.](/docs/app/api-reference/functions/generate-static-params)[### generateViewport

API Reference for the generateViewport function.](/docs/app/api-reference/functions/generate-viewport)[### headers

API reference for the headers function.](/docs/app/api-reference/functions/headers)[### ImageResponse

API Reference for the ImageResponse constructor.](/docs/app/api-reference/functions/image-response)[### NextRequest

API Reference for NextRequest.](/docs/app/api-reference/functions/next-request)[### NextResponse

API Reference for NextResponse.](/docs/app/api-reference/functions/next-response)[### notFound

API Reference for the notFound function.](/docs/app/api-reference/functions/not-found)[### permanentRedirect

API Reference for the permanentRedirect function.](/docs/app/api-reference/functions/permanentRedirect)[### redirect

API Reference for the redirect function.](/docs/app/api-reference/functions/redirect)[### revalidatePath

API Reference for the revalidatePath function.](/docs/app/api-reference/functions/revalidatePath)[### revalidateTag

API Reference for the revalidateTag function.](/docs/app/api-reference/functions/revalidateTag)[### unauthorized

API Reference for the unauthorized function.](/docs/app/api-reference/functions/unauthorized)[### unstable\_cache

API Reference for the unstable\_cache function.](/docs/app/api-reference/functions/unstable_cache)[### unstable\_expirePath

API Reference for the unstable\_expirePath function.](/docs/app/api-reference/functions/unstable_expirePath)[### unstable\_expireTag

API Reference for the unstable\_expireTag function.](/docs/app/api-reference/functions/unstable_expireTag)[### unstable\_noStore

API Reference for the unstable\_noStore function.](/docs/app/api-reference/functions/unstable_noStore)[### unstable\_rethrow

API Reference for the unstable\_rethrow function.](/docs/app/api-reference/functions/unstable_rethrow)[### useParams

API Reference for the useParams hook.](/docs/app/api-reference/functions/use-params)[### usePathname

API Reference for the usePathname hook.](/docs/app/api-reference/functions/use-pathname)[### useReportWebVitals

API Reference for the useReportWebVitals function.](/docs/app/api-reference/functions/use-report-web-vitals)[### useRouter

API reference for the useRouter hook.](/docs/app/api-reference/functions/use-router)[### useSearchParams

API Reference for the useSearchParams hook.](/docs/app/api-reference/functions/use-search-params)[### useSelectedLayoutSegment

API Reference for the useSelectedLayoutSegment hook.](/docs/app/api-reference/functions/use-selected-layout-segment)[### useSelectedLayoutSegments

API Reference for the useSelectedLayoutSegments hook.](/docs/app/api-reference/functions/use-selected-layout-segments)[### userAgent

The userAgent helper extends the Web Request API with additional properties and methods to interact with the user agent object from the request.](/docs/app/api-reference/functions/userAgent)Was this helpful?



## App Router: Examples | Next.js

[Read the full article](https://nextjs.org/docs/app/examples)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[Introduction](/docs)[App Router](/docs/app)Examples# Examples

### [Data Fetching](#data-fetching)

* [Using the `fetch` API](/docs/app/building-your-application/data-fetching/fetching#fetching-data-on-the-server-with-the-fetch-api)
* [Using an ORM or database client](/docs/app/building-your-application/data-fetching/fetching#fetching-data-on-the-server-with-an-orm-or-database)
* [Reading search params on the server](/docs/app/api-reference/file-conventions/page)
* [Reading search params on the client](/docs/app/api-reference/functions/use-search-params)

### [Revalidating Data](#revalidating-data)

* [Using ISR to revalidate data after a certain time](/docs/app/building-your-application/data-fetching/incremental-static-regeneration#time-based-revalidation)
* [Using ISR to revalidate data on\-demand](/docs/app/building-your-application/data-fetching/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)

### [Forms](#forms)

* [Showing a pending state while submitting a form](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#pending-states)
* [Server\-side form validation](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#server-side-form-validation)
* [Handling expected errors](/docs/app/building-your-application/routing/error-handling#handling-expected-errors-from-server-actions)
* [Handling unexpected exceptions](/docs/app/building-your-application/routing/error-handling#uncaught-exceptions)
* [Showing optimistic UI updates](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#optimistic-updates)
* [Programmatic form submission](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#programmatic-form-submission)

### [Server Actions](#server-actions)

* [Passing additional values](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#passing-additional-arguments)
* [Revalidating data](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#revalidating-data)
* [Redirecting](/docs/app/building-your-application/data-fetching/server-actions-and-mutations#redirecting)
* [Setting cookies](/docs/app/api-reference/functions/cookies#setting-a-cookie)
* [Deleting cookies](/docs/app/api-reference/functions/cookies#deleting-cookies)

### [Metadata](#metadata)

* [Creating an RSS feed](/docs/app/building-your-application/routing/route-handlers#non-ui-responses)
* [Creating an Open Graph image](/docs/app/api-reference/file-conventions/metadata/opengraph-image)
* [Creating a sitemap](/docs/app/api-reference/file-conventions/metadata/sitemap)
* [Creating a robots.txt file](/docs/app/api-reference/file-conventions/metadata/robots)
* [Creating a custom 404 page](/docs/app/api-reference/file-conventions/not-found)
* [Creating a custom 500 page](/docs/app/api-reference/file-conventions/error)

### [Auth](#auth)

* [Creating a sign\-up form](/docs/app/building-your-application/authentication#sign-up-and-login-functionality)
* [Stateless, cookie\-based session management](/docs/app/building-your-application/authentication#stateless-sessions)
* [Stateful, database\-backed session management](/docs/app/building-your-application/authentication#database-sessions)
* [Managing authorization](/docs/app/building-your-application/authentication#authorization)

### [Testing](#testing)

* [Vitest](/docs/app/building-your-application/testing/vitest)
* [Jest](/docs/app/building-your-application/testing/jest)
* [Playwright](/docs/app/building-your-application/testing/playwright)
* [Cypress](/docs/app/building-your-application/testing/cypress)

### [Deployment](#deployment)

* [Creating a Dockerfile](/docs/app/building-your-application/deploying#docker-image)
* [Creating a static export (SPA)](/docs/app/building-your-application/deploying/static-exports)
* [Configuring caching when self\-hosting](/docs/app/building-your-application/deploying#configuring-caching)
* [Configuring Image Optimization when self\-hosting](/docs/app/building-your-application/deploying#image-optimization)
Was this helpful?



## Functions: cacheLife | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/cacheLife)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)cacheLife# cacheLife

This feature is currently available in the canary channel and subject to change. Try it out by [upgrading Next.js](/docs/app/building-your-application/upgrading/canary), and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The `cacheLife` function is used to set the cache lifetime of a function or component. It should be used alongside the [`use cache`](/docs/app/api-reference/directives/use-cache) directive, and within the scope of the function or component.

## [Usage](#usage)

To use `cacheLife`, enable the [`dynamicIO` flag](/docs/app/api-reference/config/next-config-js/dynamicIO) in your `next.config.js` file:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 experimental: {
 dynamicIO: true,
 },
}

export default nextConfig
\`\`\`

Then, import and invoke the `cacheLife` function within the scope of the function or component:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use cache'
import { unstable\_cacheLife as cacheLife } from 'next/cache'

export default async function Page() {
 cacheLife('hours')
 return \Page\
}
\`\`\`

## [Reference](#reference)

### [Default cache profiles](#default-cache-profiles)

Next.js provides a set of named cache profiles modeled on various timescales. If you don't specify a cache profile in the `cacheLife` function alongside the `use cache` directive, Next.js will automatically apply the “default” cache profile.

However, we recommend always adding a cache profile when using the `use cache` directive to explicitly define caching behavior.

| **Profile** | **Stale** | **Revalidate** | **Expire** | **Description** |
| --- | --- | --- | --- | --- |
| `default` | undefined | 15 minutes | INFINITE\_CACHE | Default profile, suitable for content that doesn't need frequent updates |
| `seconds` | undefined | 1 second | 1 minute | For rapidly changing content requiring near real\-time updates |
| `minutes` | 5 minutes | 1 minute | 1 hour | For content that updates frequently within an hour |
| `hours` | 5 minutes | 1 hour | 1 day | For content that updates daily but can be slightly stale |
| `days` | 5 minutes | 1 day | 1 week | For content that updates weekly but can be a day old |
| `weeks` | 5 minutes | 1 week | 1 month | For content that updates monthly but can be a week old |
| `max` | 5 minutes | 1 month | INFINITE\_CACHE | For very stable content that rarely needs updating |

The string values used to reference cache profiles don't carry inherent meaning; instead they serve as semantic labels. This allows you to better understand and manage your cached content within your codebase.

### [Custom cache profiles](#custom-cache-profiles)

You can configure custom cache profiles by adding them to the [`cacheLife`](/docs/app/api-reference/config/next-config-js/cacheLife) option in your `next.config.ts` file.

Cache profiles are objects that contain the following properties:

| **Property** | **Value** | **Description** | **Requirement** |
| --- | --- | --- | --- |
| `stale` | `number` | Duration the client should cache a value without checking the server. | Optional |
| `revalidate` | `number` | Frequency at which the cache should refresh on the server; stale values may be served while revalidating. | Optional |
| `expire` | `number` | Maximum duration for which a value can remain stale before switching to dynamic fetching; must be longer than `revalidate`. | Optional \- Must be longer than `revalidate` |

The "stale" property differs from the [`staleTimes`](/docs/app/api-reference/config/next-config-js/staleTimes) setting in that it specifically controls client\-side router caching. While `staleTimes` is a global setting that affects all instances of both dynamic and static data, the `cacheLife` configuration allows you to define "stale" times on a per\-function or per\-route basis.

> **Good to know**: The “stale” property does not set the `Cache-control: max-age` header. It instead controls the client\-side router cache.

## [Examples](#examples)

### [Defining reusable cache profiles](#defining-reusable-cache-profiles)

You can create a reusable cache profile by defining them in your `next.config.ts` file. Choose a name that suits your use case and set values for the `stale`, `revalidate`, and `expire` properties. You can create as many custom cache profiles as needed. Each profile can be referenced by its name as a string value passed to the `cacheLife` function.

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 experimental: {
 dynamicIO: true,
 cacheLife: {
 biweekly: {
 stale: 60 \* 60 \* 24 \* 14, // 14 days
 revalidate: 60 \* 60 \* 24, // 1 day
 expire: 60 \* 60 \* 24 \* 14, // 14 days
 },
 },
 },
}

module.exports = nextConfig
\`\`\`

The example above caches for 14 days, checks for updates daily, and expires the cache after 14 days. You can then reference this profile throughout your application by its name:

app/page.tsx\`\`\`
'use cache'
import { unstable\_cacheLife as cacheLife } from 'next/cache'

export default async function Page() {
 cacheLife('biweekly')
 return \Page\
}
\`\`\`
### [Overriding the default cache profiles](#overriding-the-default-cache-profiles)

While the default cache profiles provide a useful way to think about how fresh or stale any given part of cacheable output can be, you may prefer different named profiles to better align with your applications caching strategies.

You can override the default named cache profiles by creating a new configuration with the same name as the defaults.

The example below shows how to override the default “days” cache profile:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 dynamicIO: true,
 cacheLife: {
 days: {
 stale: 3600, // 1 hour
 revalidate: 900, // 15 minutes
 expire: 86400, // 1 day
 },
 },
 },
}

module.exports = nextConfig
\`\`\`
### [Defining cache profiles inline](#defining-cache-profiles-inline)

For specific use cases, you can set a custom cache profile by passing an object to the `cacheLife` function:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use cache'
import { unstable\_cacheLife as cacheLife } from 'next/cache'

export default async function Page() {
 cacheLife({
 stale: 3600, // 1 hour
 revalidate: 900, // 15 minutes
 expire: 86400, // 1 day
 })

 return \Page\
}
\`\`\`

This inline cache profile will only be applied to the function or file it was created in. If you want to reuse the same profile throughout your application, you can [add the configuration](#defining-reusable-cache-profiles) to the `cacheLife` property of your `next.config.ts` file.

### [Nested usage of `use cache` and `cacheLife`](#nested-usage-of-use-cache-and-cachelife)

When defining multiple caching behaviors in the same route or component tree, if the inner caches specify their own `cacheLife` profile, the outer cache will respect the shortest cache duration among them. **This applies only if the outer cache does not have its own explicit `cacheLife` profile defined.**

For example, if you add the `use cache` directive to your page, without specifying a cache profile, the default cache profile will be applied implicitly (`cacheLife(”default”)`). If a component imported into the page also uses the `use cache` directive with its own cache profile, the outer and inner cache profiles are compared, and shortest duration set in the profiles will be applied.

app/components/parent.tsx\`\`\`
// Parent component
import { unstable\_cacheLife as cacheLife } from 'next/cache'
import { ChildComponent } from './child'

export async function ParentComponent() {
 'use cache'
 cacheLife('days')

 return (
 \
 \
 \
 )
}
\`\`\`
And in a separate file, we defined the Child component that was imported:

app/components/child.tsx\`\`\`
// Child component
import { unstable\_cacheLife as cacheLife } from 'next/cache'

export async function ChildComponent() {
 'use cache'
 cacheLife('hours')
 return \Child Content\

 // This component's cache will respect the shorter 'hours' profile
}
\`\`\`## Related

View related API references.[### dynamicIO

Learn how to enable the dynamicIO flag in Next.js.](/docs/app/api-reference/config/next-config-js/dynamicIO)[### use cache

Learn how to use the use cache directive to cache data in your Next.js application.](/docs/app/api-reference/directives/use-cache)[### revalidateTag

API Reference for the revalidateTag function.](/docs/app/api-reference/functions/revalidateTag)[### cacheTag

Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.](/docs/app/api-reference/functions/cacheTag)Was this helpful?



## Functions: revalidatePath | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unstable_expirePath)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)revalidatePath# revalidatePath

`revalidatePath` allows you to purge [cached data](/docs/app/building-your-application/caching) on\-demand for a specific path.

> **Good to know**:
> 
> 
> * `revalidatePath` is available in both [Node.js and Edge runtimes](/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes).
> * `revalidatePath` only invalidates the cache when the included path is next visited. This means calling `revalidatePath` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.
> * Currently, `revalidatePath` invalidates all the routes in the [client\-side Router Cache](/docs/app/building-your-application/caching#client-side-router-cache) when used in a server action. This behavior is temporary and will be updated in the future to apply only to the specific path.
> * Using `revalidatePath` invalidates **only the specific path** in the [server\-side Route Cache](/docs/app/building-your-application/caching#full-route-cache).

## [Parameters](#parameters)

\`\`\`
revalidatePath(path: string, type?: 'page' \| 'layout'): void;
\`\`\`
* `path`: Either a string representing the filesystem path associated with the data you want to revalidate (for example, `/product/[slug]/page`), or the literal route segment (for example, `/product/123`). Must be less than 1024 characters. This value is case\-sensitive.
* `type`: (optional) `'page'` or `'layout'` string to change the type of path to revalidate. If `path` contains a dynamic segment (for example, `/product/[slug]/page`), this parameter is required. If path refers to the literal route segment, e.g., `/product/1` for a dynamic page (e.g., `/product/[slug]/page`), you should not provide `type`.

## [Returns](#returns)

`revalidatePath` does not return a value.

## [Examples](#examples)

### [Revalidating A Specific URL](#revalidating-a-specific-url)

\`\`\`
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/post\-1')
\`\`\`
This will revalidate one specific URL on the next page visit.

### [Revalidating A Page Path](#revalidating-a-page-path)

\`\`\`
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/\[slug]', 'page')
// or with route groups
revalidatePath('/(main)/blog/\[slug]', 'page')
\`\`\`
This will revalidate any URL that matches the provided `page` file on the next page visit. This will *not* invalidate pages beneath the specific page. For example, `/blog/[slug]` won't invalidate `/blog/[slug]/[author]`.

### [Revalidating A Layout Path](#revalidating-a-layout-path)

\`\`\`
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/\[slug]', 'layout')
// or with route groups
revalidatePath('/(main)/post/\[slug]', 'layout')
\`\`\`
This will revalidate any URL that matches the provided `layout` file on the next page visit. This will cause pages beneath with the same layout to revalidate on the next visit. For example, in the above case, `/blog/[slug]/[another]` would also revalidate on the next visit.

### [Revalidating All Data](#revalidating-all-data)

\`\`\`
import { revalidatePath } from 'next/cache'

revalidatePath('/', 'layout')
\`\`\`
This will purge the Client\-side Router Cache, and revalidate the Data Cache on the next page visit.

### [Server Action](#server-action)

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { revalidatePath } from 'next/cache'

export default async function submit() {
 await submitForm()
 revalidatePath('/')
}
\`\`\`
### [Route Handler](#route-handler)

app/api/revalidate/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { revalidatePath } from 'next/cache'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
 const path = request.nextUrl.searchParams.get('path')

 if (path) {
 revalidatePath(path)
 return Response.json({ revalidated: true, now: Date.now() })
 }

 return Response.json({
 revalidated: false,
 now: Date.now(),
 message: 'Missing path to revalidate',
 })
}
\`\`\`
Was this helpful?



## Functions: useReportWebVitals | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)useReportWebVitals# useReportWebVitals

The `useReportWebVitals` hook allows you to report [Core Web Vitals](https://web.dev/vitals/), and can be used in combination with your analytics service.

app/\_components/web\-vitals.js\`\`\`
'use client'

import { useReportWebVitals } from 'next/web\-vitals'

export function WebVitals() {
 useReportWebVitals((metric) =\> {
 console.log(metric)
 })

 return null
}
\`\`\`app/layout.js\`\`\`
import { WebVitals } from './\_components/web\-vitals'

export default function Layout({ children }) {
 return (
 \
 \
 \
 {children}
 \
 \
 )
}
\`\`\`
> Since the `useReportWebVitals` hook requires the `"use client"` directive, the most performant approach is to create a separate component that the root layout imports. This confines the client boundary exclusively to the `WebVitals` component.

## [useReportWebVitals](#usereportwebvitals)

The `metric` object passed as the hook's argument consists of a number of properties:

* `id`: Unique identifier for the metric in the context of the current page load
* `name`: The name of the performance metric. Possible values include names of [Web Vitals](#web-vitals) metrics (TTFB, FCP, LCP, FID, CLS) specific to a web application.
* `delta`: The difference between the current value and the previous value of the metric. The value is typically in milliseconds and represents the change in the metric's value over time.
* `entries`: An array of [Performance Entries](https://developer.mozilla.org/docs/Web/API/PerformanceEntry) associated with the metric. These entries provide detailed information about the performance events related to the metric.
* `navigationType`: Indicates the [type of navigation](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming/type) that triggered the metric collection. Possible values include `"navigate"`, `"reload"`, `"back_forward"`, and `"prerender"`.
* `rating`: A qualitative rating of the metric value, providing an assessment of the performance. Possible values are `"good"`, `"needs-improvement"`, and `"poor"`. The rating is typically determined by comparing the metric value against predefined thresholds that indicate acceptable or suboptimal performance.
* `value`: The actual value or duration of the performance entry, typically in milliseconds. The value provides a quantitative measure of the performance aspect being tracked by the metric. The source of the value depends on the specific metric being measured and can come from various [Performance API](https://developer.mozilla.org/docs/Web/API/Performance_API)s.

## [Web Vitals](#web-vitals)

[Web Vitals](https://web.dev/vitals/) are a set of useful metrics that aim to capture the user
experience of a web page. The following web vitals are all included:

* [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
* [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
* [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
* [First Input Delay](https://web.dev/fid/) (FID)
* [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
* [Interaction to Next Paint](https://web.dev/inp/) (INP)

You can handle all the results of these metrics using the `name` property.

app/components/web\-vitals.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useReportWebVitals } from 'next/web\-vitals'

export function WebVitals() {
 useReportWebVitals((metric) =\> {
 switch (metric.name) {
 case 'FCP': {
 // handle FCP results
 }
 case 'LCP': {
 // handle LCP results
 }
 // ...
 }
 })
}
\`\`\`

## [Usage on Vercel](#usage-on-vercel)

[Vercel Speed Insights](https://vercel.com/docs/speed-insights/quickstart) does not `useReportWebVitals`, but `@vercel/speed-insights` package instead.
`useReportWebVitals` hook is useful in local development, or if you're using a different service for collecting Web Vitals.

## [Sending results to external systems](#sending-results-to-external-systems)

You can send results to any endpoint to measure and track
real user performance on your site. For example:

\`\`\`
useReportWebVitals((metric) =\> {
 const body = JSON.stringify(metric)
 const url = 'https://example.com/analytics'

 // Use \`navigator.sendBeacon()\` if available, falling back to \`fetch()\`.
 if (navigator.sendBeacon) {
 navigator.sendBeacon(url, body)
 } else {
 fetch(url, { body, method: 'POST', keepalive: true })
 }
})
\`\`\`

> **Good to know**: If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the
> `id` value can allow you to construct metric distributions manually (to calculate percentiles,
> etc.)

> \`\`\`
> useReportWebVitals(metric =\> {
>  // Use \`window.gtag\` if you initialized Google Analytics as this example:
>  // https://github.com/vercel/next.js/blob/canary/examples/with\-google\-analytics
>  window.gtag('event', metric.name, {
>  value: Math.round(metric.name === 'CLS' ? metric.value \* 1000 : metric.value), // values must be integers
>  event\_label: metric.id, // id unique to current page load
>  non\_interaction: true, // avoids affecting bounce rate.
>  });
> }
> \`\`\`
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).

Was this helpful?



## File Conventions: route.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/route)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)route.js# route.js

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

route.tsTypeScriptJavaScriptTypeScript\`\`\`
export async function GET() {
 return Response.json({ message: 'Hello World' })
}
\`\`\`

## [Reference](#reference)

### [HTTP Methods](#http-methods)

A **route** file allows you to create custom request handlers for a given route. The following [HTTP methods](https://developer.mozilla.org/docs/Web/HTTP/Methods) are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`.

route.tsTypeScriptJavaScriptTypeScript\`\`\`
export async function GET(request: Request) {}

export async function HEAD(request: Request) {}

export async function POST(request: Request) {}

export async function PUT(request: Request) {}

export async function DELETE(request: Request) {}

export async function PATCH(request: Request) {}

// If \`OPTIONS\` is not defined, Next.js will automatically implement \`OPTIONS\` and set the appropriate Response \`Allow\` header depending on the other methods defined in the Route Handler.
export async function OPTIONS(request: Request) {}
\`\`\`

### [Parameters](#parameters)

#### [`request` (optional)](#request-optional)

The `request` object is a [NextRequest](/docs/app/api-reference/functions/next-request) object, which is an extension of the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) API. `NextRequest` gives you further control over the incoming request, including easily accessing `cookies` and an extended, parsed, URL object `nextUrl`.

route.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
 const url = request.nextUrl
}
\`\`\`

#### [`context` (optional)](#context-optional)

* **`params`**: a promise that resolves to an object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) for the current route.

app/dashboard/\[team]/route.tsTypeScriptJavaScriptTypeScript\`\`\`
export async function GET(
 request: Request,
 { params }: { params: Promise\ }
) {
 const team = (await params).team
}
\`\`\`

| Example | URL | `params` |
| --- | --- | --- |
| `app/dashboard/[team]/route.js` | `/dashboard/1` | `Promise` |
| `app/shop/[tag]/[item]/route.js` | `/shop/1/2` | `Promise` |
| `app/blog/[...slug]/route.js` | `/blog/1/2` | `Promise` |

## [Examples](#examples)

### [Handling cookies](#handling-cookies)

route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { cookies } from 'next/headers'

export async function GET(request: NextRequest) {
 const cookieStore = await cookies()

 const a = cookieStore.get('a')
 const b = cookieStore.set('b', '1')
 const c = cookieStore.delete('c')
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `context.params` is now a promise. A [codemod](/docs/app/building-your-application/upgrading/codemods#150) is available |
| `v15.0.0-RC` | The default caching for `GET` handlers was changed from static to dynamic |
| `v13.2.0` | Route Handlers are introduced. |

Was this helpful?



## API Reference: CLI | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/cli)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)CLI# CLI

Next.js comes with **two** Command Line Interface (CLI) tools:

* **`create-next-app`**: Quickly create a new Next.js application using the default template or an [example](https://github.com/vercel/next.js/tree/canary/examples) from a public GitHub repository.
* **`next`**: Run the Next.js development server, build your application, and more.
[### create\-next\-app

Create Next.js apps using one command with the create\-next\-app CLI.](/docs/app/api-reference/cli/create-next-app)[### next CLI

Learn how to run and build your application with the Next.js CLI.](/docs/app/api-reference/cli/next)Was this helpful?



## Getting Started: Installation | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started/installation)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Installation# How to set up a new Next.js project

## [System requirements](#system-requirements)

* [Node.js 18\.18](https://nodejs.org/) or later.
* macOS, Windows (including WSL), and Linux are supported.

## [Automatic installation](#automatic-installation)

We recommend starting a new Next.js app using [`create-next-app`](/docs/app/api-reference/cli/create-next-app), which sets up everything automatically for you. To create a project, run:

Terminal\`\`\`
npx create\-next\-app@latest
\`\`\`
On installation, you'll see the following prompts:

Terminal\`\`\`
What is your project named? my\-app
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a \`src/\` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack for \`next dev\`? No / Yes
Would you like to customize the import alias (\`@/\*\` by default)? No / Yes
What import alias would you like configured? @/\*
\`\`\`
After the prompts, [`create-next-app`](/docs/app/api-reference/cli/create-next-app) will create a folder with your project name and install the required dependencies.

## [Manual installation](#manual-installation)

To manually create a new Next.js app, install the required packages:

Terminal\`\`\`
npm install next@latest react@latest react\-dom@latest
\`\`\`
Open your `package.json` file and add the following `scripts`:

package.json\`\`\`
{
 "scripts": {
 "dev": "next dev",
 "build": "next build",
 "start": "next start",
 "lint": "next lint"
 }
}
\`\`\`
These scripts refer to the different stages of developing an application:

* `dev`: runs [`next dev`](/docs/app/api-reference/cli/next#next-dev-options) to start Next.js in development mode.
* `build`: runs [`next build`](/docs/app/api-reference/cli/next#next-build-options) to build the application for production usage.
* `start`: runs [`next start`](/docs/app/api-reference/cli/next#next-start-options) to start a Next.js production server.
* `lint`: runs [`next lint`](/docs/app/api-reference/cli/next#next-lint-options) to set up Next.js' built\-in ESLint configuration.

### [Create the `app` directory](#create-the-app-directory)

Next.js uses file\-system routing, which means the routes in your application are determined by how you structure your files.

Create an `app` folder, then add a `layout.tsx` and `page.tsx` file. These will be rendered when the user visits the root of your application (`/`).

Create a [root layout](/docs/app/building-your-application/routing/layouts-and-templates#root-layout-required) inside `app/layout.tsx` with the required `` and `` tags:

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`Finally, create a home page `app/page.tsx` with some initial content:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function Page() {
 return \Hello, Next.js!\
}
\`\`\`
> **Good to know**:
> 
> 
> * If you forget to create `layout.tsx`, Next.js will automatically create this file when running the development server with `next dev`.
> * You can optionally use a [`src` directory](/docs/app/building-your-application/configuring/src-directory) in the root of your project to separate your application's code from configuration files.

### [Create the `public` folder (optional)](#create-the-public-folder-optional)

You can optionally create a [`public` folder](/docs/app/building-your-application/optimizing/static-assets) at the root of your project to store static assets such as images, fonts, etc. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

## [Run the development server](#run-the-development-server)

1. Run `npm run dev` to start the development server.
2. Visit `http://localhost:3000` to view your application.
3. Edit the`app/page.tsx`  file and save it to see the updated result in your browser.

## [Set up TypeScript](#set-up-typescript)

> Minimum TypeScript version: `v4.5.2`

Next.js comes with built\-in TypeScript support. To add TypeScript to your project, rename a file to `.ts` / `.tsx`. Run `next dev`, Next.js will automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

### [IDE Plugin](#ide-plugin)

Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type\-checking and auto\-completion.

You can enable the plugin in VS Code by:

1. Opening the command palette (`Ctrl/⌘` \+ `Shift` \+ `P`)
2. Searching for "TypeScript: Select TypeScript Version"
3. Selecting "Use Workspace Version"

Now, when editing files, the custom plugin will be enabled. When running `next build`, the custom type checker will be used.

See the [TypeScript configuration](/docs/app/api-reference/config/next-config-js/typescript) page for more information on how to use TypeScript in your project.

## [Set up ESLint](#set-up-eslint)

Next.js comes with built\-in ESLint, automatically installing the necessary packages and configuring the proper settings when you create a new project with `create-next-app`.

To add ESLint to an existing project, add `next lint` as a script to `package.json`:

package.json\`\`\`
{
 "scripts": {
 "lint": "next lint"
 }
}
\`\`\`
Then, run `npm run lint` and you will be guided through the installation and configuration process.

Terminal\`\`\`
pnpm lint
\`\`\`
You'll see a prompt like this:

> ? How would you like to configure ESLint?
> 
> 
> ❯ Strict (recommended)  
> 
> Base  
> 
> Cancel

* **Strict**: Includes Next.js' base ESLint configuration along with a stricter Core Web Vitals rule\-set. This is the recommended configuration for developers setting up ESLint for the first time.
* **Base**: Includes Next.js' base ESLint configuration.
* **Cancel**: Does not include any ESLint configuration. Only select this option if you plan on setting up your own custom ESLint configuration.

If either of the two configuration options are selected, Next.js will automatically install `eslint` and `eslint-config-next` as dependencies in your application and create an `.eslintrc.json` file in the root of your project that includes your selected configuration.

You can now run `next lint` every time you want to run ESLint to catch errors. Once ESLint has been set up, it will also automatically run during every build (`next build`). Errors will fail the build, while warnings will not.

See the [ESLint Plugin](/docs/app/api-reference/config/next-config-js/eslint) page for more information on how to configure ESLint in your project.

## [Set up Absolute Imports and Module Path Aliases](#set-up-absolute-imports-and-module-path-aliases)

Next.js has in\-built support for the `"paths"` and `"baseUrl"` options of `tsconfig.json` and `jsconfig.json` files. These options allow you to alias project directories to absolute paths, making it easier to import modules. For example:

\`\`\`
// Before
import { Button } from '../../../components/button'

// After
import { Button } from '@/components/button'
\`\`\`
To configure absolute imports, add the `baseUrl` configuration option to your `tsconfig.json` or `jsconfig.json` file. For example:

tsconfig.json or jsconfig.json\`\`\`
{
 "compilerOptions": {
 "baseUrl": "src/"
 }
}
\`\`\`
In addition to configuring the `baseUrl` path, you can use the `"paths"` option to `"alias"` module paths.

For example, the following configuration maps `@/components/*` to `components/*`:

tsconfig.json or jsconfig.json\`\`\`
{
 "compilerOptions": {
 "baseUrl": "src/",
 "paths": {
 "@/styles/\*": \["styles/\*"],
 "@/components/\*": \["components/\*"]
 }
 }
}
\`\`\`
Each of the `"paths"` are relative to the `baseUrl` location. For example:

src/app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Button from '@/components/button'
import '@/styles/styles.css'

export default function HomePage() {
 return (
 \
 \Hello World\
 \
 \
 )
}
\`\`\`
Was this helpful?



## File Conventions: layout.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/layout)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)layout.js# layout.js

The `layout` file is used to define a layout in your Next.js application.

app/dashboard/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function DashboardLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return \{children}\
}
\`\`\`

A **root layout** is the top\-most layout in the root `app` directory. It is used to define the `` and `` tags and other globally shared UI.

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

## [Reference](#reference)

### [Props](#props)

#### [`children` (required)](#children-required)

Layout components should accept and use a `children` prop. During rendering, `children` will be populated with the route segments the layout is wrapping. These will primarily be the component of a child [Layout](/docs/app/api-reference/file-conventions/page) (if it exists) or [Page](/docs/app/api-reference/file-conventions/page), but could also be other special files like [Loading](/docs/app/building-your-application/routing/loading-ui-and-streaming) or [Error](/docs/app/building-your-application/routing/error-handling) when applicable.

#### [`params` (optional)](#params-optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/building-your-application/routing/dynamic-routes) object from the root segment down to that layout.

app/dashboard/\[team]/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Layout({
 params,
}: {
 params: Promise\
}) {
 const team = (await params).team
}
\`\`\`

| Example Route | URL | `params` |
| --- | --- | --- |
| `app/dashboard/[team]/layout.js` | `/dashboard/1` | `Promise` |
| `app/shop/[tag]/[item]/layout.js` | `/shop/1/2` | `Promise` |
| `app/blog/[...slug]/layout.js` | `/blog/1/2` | `Promise` |

* Since the `params` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
	+ In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.

### [Root Layouts](#root-layouts)

The `app` directory **must** include a root `app/layout.js`.

app/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default function RootLayout({
 children,
}: {
 children: React.ReactNode
}) {
 return (
 \
 \{children}\
 \
 )
}
\`\`\`

* The root layout **must** define `` and `` tags.
	+ You should **not** manually add `` tags such as `` and `` to root layouts. Instead, you should use the [Metadata API](/docs/app/building-your-application/optimizing/metadata) which automatically handles advanced requirements such as streaming and de\-duplicating `` elements.
* You can use [route groups](/docs/app/building-your-application/routing/route-groups) to create multiple root layouts.
	+ Navigating **across multiple root layouts** will cause a **full page load** (as opposed to a client\-side navigation). For example, navigating from `/cart` that uses `app/(shop)/layout.js` to `/blog` that uses `app/(marketing)/layout.js` will cause a full page load. This **only** applies to multiple root layouts.

## [Caveats](#caveats)

### [Layouts do not receive `searchParams`](#layouts-do-not-receive-searchparams)

Unlike [Pages](/docs/app/api-reference/file-conventions/page), Layout components **do not** receive the `searchParams` prop. This is because a shared layout is [not re\-rendered during navigation](/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering) which could lead to stale `searchParams` between navigations.

When using client\-side navigation, Next.js automatically only renders the part of the page below the common layout between two routes.

For example, in the following directory structure, `dashboard/layout.tsx` is the common layout for both `/dashboard/settings` and `/dashboard/analytics`:


When navigating from `/dashboard/settings` to `/dashboard/analytics`, `page.tsx` in `/dashboard/analytics` will rerender on the server, while `dashboard/layout.tsx` will **not** rerender because it's a common UI shared between the two routes.

This performance optimization allows navigation between pages that share a layout to be quicker as only the data fetching and rendering for the page has to run, instead of the entire route that could include shared layouts that fetch their own data.

Because `dashboard/layout.tsx` doesn't re\-render, the `searchParams` prop in the layout Server Component might become **stale** after navigation.

Instead, use the Page [`searchParams`](/docs/app/api-reference/file-conventions/page#searchparams-optional) prop or the [`useSearchParams`](/docs/app/api-reference/functions/use-search-params) hook in a Client Component within the layout, which is rerendered on the client with the latest `searchParams`.

### [Layouts cannot access `pathname`](#layouts-cannot-access-pathname)

Layouts cannot access `pathname`. This is because layouts are Server Components by default, and [don't rerender during client\-side navigation](/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering), which could lead to `pathname` becoming stale between navigations. To prevent staleness, Next.js would need to refetch all segments of a route, losing the benefits of caching and increasing the [RSC payload](/docs/app/building-your-application/rendering/server-components#what-is-the-react-server-component-payload-rsc) size on navigation.

Instead, you can extract the logic that depends on pathname into a Client Component and import it into your layouts. Since Client Components rerender (but are not refetched) during navigation, you can use Next.js hooks such as [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) to access the current pathname and prevent staleness.

app/dashboard/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { ClientComponent } from '@/app/ui/ClientComponent'

export default function Layout({ children }: { children: React.ReactNode }) {
 return (
 \
 \
 {/\* Other Layout UI \*/}
 \{children}\
 \
 )
}
\`\`\`

Common `pathname` patterns can also be implemented with [`params`](#params-optional) prop.

See the [examples](/docs/app/building-your-application/routing/layouts-and-templates#examples) section for more information.

## [Examples](#examples)

### [Displaying content based on `params`](#displaying-content-based-on-params)

Using [dynamic route segments](/docs/app/building-your-application/routing/dynamic-routes), you can display or fetch specific content based on the `params` prop.

app/dashboard/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function DashboardLayout({
 children,
 params,
}: {
 children: React.ReactNode
 params: Promise\
}) {
 const { team } = await params

 return (
 \
 \
 \Welcome to {team}'s Dashboard\
 \
 \{children}\
 \
 )
}
\`\`\`

### [Reading `params` in Client Components](#reading-params-in-client-components)

To use `params` in a Client Component (which cannot be `async`), you can use React's [`use`](https://react.dev/reference/react/use) function to read the promise:

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { use } from 'react'

export default function Page({
 params,
}: {
 params: Promise\
}) {
 const { slug } = use(params)
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0-RC` | `params` is now a promise. A [codemod](/docs/app/building-your-application/upgrading/codemods#150) is available. |
| `v13.0.0` | `layout` introduced. |

Was this helpful?



## Directives: use client | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/directives/use-client)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Directives](/docs/app/api-reference/directives)use client# use client

The `use client` directive designates a component to be rendered on the **client side** and should be used when creating interactive user interfaces (UI) that require client\-side JavaScript capabilities, such as state management, event handling, and access to browser APIs. This is a React feature.

## [Usage](#usage)

To designate a component as a Client Component, add the `use client` directive **at the top of the file**, before any imports:

app/components/counter.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useState } from 'react'

export default function Counter() {
 const \[count, setCount] = useState(0\)

 return (
 \
 \Count: {count}\
 \ setCount(count \+ 1\)}\>Increment\
 \
 )
}
\`\`\`

## [Nesting Client Components within Server Components](#nesting-client-components-within-server-components)

Combining Server and Client Components allows you to build applications that are both performant and interactive:

1. **Server Components**: Use for static content, data fetching, and SEO\-friendly elements.
2. **Client Components**: Use for interactive elements that require state, effects, or browser APIs.
3. **Component composition**: Nest Client Components within Server Components as needed for a clear separation of server and client logic.

In the following example:

* `Header` is a Server Component handling static content.
* `Counter` is a Client Component enabling interactivity within the page.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Header from './header'
import Counter from './counter' // This is a Client Component

export default function Page() {
 return (
 \
 \
 \
 \
 )
}
\`\`\`

## [Reference](#reference)

See the [React documentation](https://react.dev/reference/rsc/use-client) for more information on `use client`.

Was this helpful?



## API Reference: Directives | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/directives)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[API Reference](/docs/app/api-reference)Directives# Directives

The following directives are available:

[### use cache

Learn how to use the use cache directive to cache data in your Next.js application.](/docs/app/api-reference/directives/use-cache)[### use client

Learn how to use the use client directive to render a component on the client.](/docs/app/api-reference/directives/use-client)[### use server

Learn how to use the use server directive to execute code on the server.](/docs/app/api-reference/directives/use-server)Was this helpful?



## Functions: connection | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/connection)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)connection# connection

The `connection()` function allows you to indicate rendering should wait for an incoming user request before continuing.

It's useful when a component doesn’t use [Dynamic APIs](/docs/app/building-your-application/rendering/server-components#dynamic-apis), but you want it to be dynamically rendered at runtime and not statically rendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as `Math.random()` or `new Date()`.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { connection } from 'next/server'

export default async function Page() {
 await connection()
 // Everything below will be excluded from prerendering
 const rand = Math.random()
 return \{rand}\
}
\`\`\`

## [Reference](#reference)

### [Type](#type)

\`\`\`
function connection(): Promise\
\`\`\`
### [Parameters](#parameters)

* The function does not accept any parameters.

### [Returns](#returns)

* The function returns a `void` Promise. It is not meant to be consumed.

## [Good to know](#good-to-know)

* `connection` replaces [`unstable_noStore`](/docs/app/api-reference/functions/unstable_noStore) to better align with the future of Next.js.
* The function is only necessary when dynamic rendering is required and common Dynamic APIs are not used.

### [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `connection` stabilized. |
| `v15.0.0-RC` | `connection` introduced. |

Was this helpful?



## Functions: revalidatePath | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)revalidatePath# revalidatePath

`revalidatePath` allows you to purge [cached data](/docs/app/building-your-application/caching) on\-demand for a specific path.

> **Good to know**:
> 
> 
> * `revalidatePath` is available in both [Node.js and Edge runtimes](/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes).
> * `revalidatePath` only invalidates the cache when the included path is next visited. This means calling `revalidatePath` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.
> * Currently, `revalidatePath` invalidates all the routes in the [client\-side Router Cache](/docs/app/building-your-application/caching#client-side-router-cache) when used in a server action. This behavior is temporary and will be updated in the future to apply only to the specific path.
> * Using `revalidatePath` invalidates **only the specific path** in the [server\-side Route Cache](/docs/app/building-your-application/caching#full-route-cache).

## [Parameters](#parameters)

\`\`\`
revalidatePath(path: string, type?: 'page' \| 'layout'): void;
\`\`\`
* `path`: Either a string representing the filesystem path associated with the data you want to revalidate (for example, `/product/[slug]/page`), or the literal route segment (for example, `/product/123`). Must be less than 1024 characters. This value is case\-sensitive.
* `type`: (optional) `'page'` or `'layout'` string to change the type of path to revalidate. If `path` contains a dynamic segment (for example, `/product/[slug]/page`), this parameter is required. If path refers to the literal route segment, e.g., `/product/1` for a dynamic page (e.g., `/product/[slug]/page`), you should not provide `type`.

## [Returns](#returns)

`revalidatePath` does not return a value.

## [Examples](#examples)

### [Revalidating A Specific URL](#revalidating-a-specific-url)

\`\`\`
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/post\-1')
\`\`\`
This will revalidate one specific URL on the next page visit.

### [Revalidating A Page Path](#revalidating-a-page-path)

\`\`\`
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/\[slug]', 'page')
// or with route groups
revalidatePath('/(main)/blog/\[slug]', 'page')
\`\`\`
This will revalidate any URL that matches the provided `page` file on the next page visit. This will *not* invalidate pages beneath the specific page. For example, `/blog/[slug]` won't invalidate `/blog/[slug]/[author]`.

### [Revalidating A Layout Path](#revalidating-a-layout-path)

\`\`\`
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/\[slug]', 'layout')
// or with route groups
revalidatePath('/(main)/post/\[slug]', 'layout')
\`\`\`
This will revalidate any URL that matches the provided `layout` file on the next page visit. This will cause pages beneath with the same layout to revalidate on the next visit. For example, in the above case, `/blog/[slug]/[another]` would also revalidate on the next visit.

### [Revalidating All Data](#revalidating-all-data)

\`\`\`
import { revalidatePath } from 'next/cache'

revalidatePath('/', 'layout')
\`\`\`
This will purge the Client\-side Router Cache, and revalidate the Data Cache on the next page visit.

### [Server Action](#server-action)

app/actions.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { revalidatePath } from 'next/cache'

export default async function submit() {
 await submitForm()
 revalidatePath('/')
}
\`\`\`
### [Route Handler](#route-handler)

app/api/revalidate/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { revalidatePath } from 'next/cache'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
 const path = request.nextUrl.searchParams.get('path')

 if (path) {
 revalidatePath(path)
 return Response.json({ revalidated: true, now: Date.now() })
 }

 return Response.json({
 revalidated: false,
 now: Date.now(),
 message: 'Missing path to revalidate',
 })
}
\`\`\`
Was this helpful?



## Functions: unstable_rethrow | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)unstable\_rethrow# unstable\_rethrow

This feature is currently unstable and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).`unstable_rethrow` can be used to avoid catching internal errors thrown by Next.js when attempting to handle errors thrown in your application code.

For example, calling the `notFound` function will throw an internal Next.js error and render the [`not-found.js`](/docs/app/api-reference/file-conventions/not-found) component. However, if used inside a `try/catch` block, the error will be caught, preventing `not-found.js` from rendering:

@/app/ui/component.tsx\`\`\`
import { notFound } from 'next/navigation'

export default async function Page() {
 try {
 const post = await fetch('https://.../posts/1').then((res) =\> {
 if (res.status === 404\) notFound()
 if (!res.ok) throw new Error(res.statusText)
 return res.json()
 })
 } catch (err) {
 console.error(err)
 }
}
\`\`\`
You can use `unstable_rethrow` API to re\-throw the internal error and continue with the expected behavior:

@/app/ui/component.tsx\`\`\`
import { notFound, unstable\_rethrow } from 'next/navigation'

export default async function Page() {
 try {
 const post = await fetch('https://.../posts/1').then((res) =\> {
 if (res.status === 404\) notFound()
 if (!res.ok) throw new Error(res.statusText)
 return res.json()
 })
 } catch (err) {
 unstable\_rethrow(err)
 console.error(err)
 }
}
\`\`\`
The following Next.js APIs rely on throwing an error which should be rethrown and handled by Next.js itself:

* [`notFound()`](/docs/app/api-reference/functions/not-found)
* [`redirect()`](/docs/app/building-your-application/routing/redirecting#redirect-function)
* [`permanentRedirect()`](/docs/app/building-your-application/routing/redirecting#permanentredirect-function)

If a route segment is marked to throw an error unless it's static, a Dynamic API call will also throw an error that should similarly not be caught by the developer. Note that Partial Prerendering (PPR) affects this behavior as well. These APIs are:

* [`cookies`](/docs/app/api-reference/functions/cookies)
* [`headers`](/docs/app/api-reference/functions/headers)
* [`searchParams`](/docs/app/api-reference/file-conventions/page#searchparams-optional)
* `fetch(..., { cache: 'no-store' })`
* `fetch(..., { next: { revalidate: 0 } })`

> **Good to know**:
> 
> 
> * This method should be called at the top of the catch block, passing the error object as its only argument. It can also be used within a `.catch` handler of a promise.
> * If you ensure that your calls to APIs that throw are not wrapped in a try/catch then you don't need to use `unstable_rethrow`
> * Any resource cleanup (like clearing intervals, timers, etc) would have to either happen prior to the call to `unstable_rethrow` or within a `finally` block.

Was this helpful?



## Functions: unstable_cache | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)unstable\_cache# unstable\_cache

This is a legacy API and no longer recommended. It's still supported for backward compatibility.In version 15, we recommend using the [`use cache`](/docs/app/api-reference/directives/use-cache) directive instead.

`unstable_cache` allows you to cache the results of expensive operations, like database queries, and reuse them across multiple requests.

\`\`\`
import { getUser } from './data';
import { unstable\_cache } from 'next/cache';

const getCachedUser = unstable\_cache(
 async (id) =\> getUser(id),
 \['my\-app\-user']
);

export default async function Component({ userID }) {
 const user = await getCachedUser(userID);
 ...
}
\`\`\`

> **Good to know**:
> 
> 
> * Accessing dynamic data sources such as `headers` or `cookies` inside a cache scope is not supported. If you need this data inside a cached function use `headers` outside of the cached function and pass the required dynamic data in as an argument.
> * This API uses Next.js' built\-in [Data Cache](/docs/app/building-your-application/caching#data-cache) to persist the result across requests and deployments.

> **Warning**: This API is unstable and may change in the future. We will provide migration documentation and codemods, if needed, as this API stabilizes.

## [Parameters](#parameters)

\`\`\`
const data = unstable\_cache(fetchData, keyParts, options)()
\`\`\`
* `fetchData`: This is an asynchronous function that fetches the data you want to cache. It must be a function that returns a `Promise`.
* `keyParts`: This is an extra array of keys that further adds identification to the cache. By default, `unstable_cache` already uses the arguments and the stringified version of your function as the cache key. It is optional in most cases; the only time you need to use it is when you use external variables without passing them as parameters. However, it is important to add closures used within the function if you do not pass them as parameters.
* `options`: This is an object that controls how the cache behaves. It can contain the following properties:
	+ `tags`: An array of tags that can be used to control cache invalidation. Next.js will not use this to uniquely identify the function.
	+ `revalidate`: The number of seconds after which the cache should be revalidated. Omit or pass `false` to cache indefinitely or until matching `revalidateTag()` or `revalidatePath()` methods are called.

## [Returns](#returns)

`unstable_cache` returns a function that when invoked, returns a Promise that resolves to the cached data. If the data is not in the cache, the provided function will be invoked, and its result will be cached and returned.

## [Example](#example)

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { unstable\_cache } from 'next/cache'

export default async function Page({ params }: { params: { userId: string } }) {
 const getCachedUser = unstable\_cache(
 async () =\> {
 return { id: params.userId }
 },
 \[params.userId], // add the user ID to the cache key
 {
 tags: \['users'],
 revalidate: 60,
 }
 )

 //...
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v14.0.0` | `unstable_cache` introduced. |

Was this helpful?



## Functions: unauthorized | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/unauthorized)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)unauthorized# unauthorized

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The `unauthorized` function throws an error that renders a Next.js 401 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`unauthorized.js` file](/docs/app/api-reference/file-conventions/unauthorized).

To start using `unauthorized`, enable the experimental [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:

next.config.tsTypeScriptJavaScriptTypeScript\`\`\`
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
 experimental: {
 authInterrupts: true,
 },
}

export default nextConfig
\`\`\`

`unauthorized` can be invoked in [Server Components](/docs/app/building-your-application/rendering/server-components), [Server Actions](/docs/app/building-your-application/data-fetching/server-actions-and-mutations), and [Route Handlers](/docs/app/building-your-application/routing/route-handlers).

app/dashboard/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
 const session = await verifySession()

 if (!session) {
 unauthorized()
 }

 // Render the dashboard for authenticated users
 return (
 \
 \Welcome to the Dashboard\
 \Hi, {session.user.name}.\
 \
 )
}
\`\`\`

## [Good to know](#good-to-know)

* The `unauthorized` function cannot be called in the [root layout](/docs/app/building-your-application/routing/layouts-and-templates#root-layout-required).

## [Examples](#examples)

### [Displaying login UI to unauthenticated users](#displaying-login-ui-to-unauthenticated-users)

You can use `unauthorized` function to display the `unauthorized.js` file with a login UI.

app/dashboard/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
 const session = await verifySession()

 if (!session) {
 unauthorized()
 }

 return \Dashboard\
}
\`\`\`

app/unauthorized.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
 return (
 \
 \401 \- Unauthorized\
 \Please log in to access this page.\
 \
 \
 )
}
\`\`\`

### [Mutations with Server Actions](#mutations-with-server-actions)

You can invoke `unauthorized` in Server Actions to ensure only authenticated users can perform specific mutations.

app/actions/update\-profile.tsTypeScriptJavaScriptTypeScript\`\`\`
'use server'

import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateProfile(data: FormData) {
 const session = await verifySession()

 // If the user is not authenticated, return a 401
 if (!session) {
 unauthorized()
 }

 // Proceed with mutation
 // ...
}
\`\`\`

### [Fetching data with Route Handlers](#fetching-data-with-route-handlers)

You can use `unauthorized` in Route Handlers to ensure only authenticated users can access the endpoint.

app/api/profile/route.tsTypeScriptJavaScriptTypeScript\`\`\`
import { NextRequest, NextResponse } from 'next/server'
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export async function GET(req: NextRequest): Promise\ {
 // Verify the user's session
 const session = await verifySession()

 // If no session exists, return a 401 and render unauthorized.tsx
 if (!session) {
 unauthorized()
 }

 // Fetch data
 // ...
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.1.0` | `unauthorized` introduced. |

## Next Steps

[### unauthorized.js

API reference for the unauthorized.js special file.](/docs/app/api-reference/file-conventions/unauthorized)Was this helpful?



## File Conventions: forbidden.js | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[File Conventions](/docs/app/api-reference/file-conventions)forbidden.js# forbidden.js

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).The **forbidden** file is used to render UI when the [`forbidden`](/docs/app/api-reference/functions/forbidden) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `403` status code.

app/forbidden.tsxTypeScriptJavaScriptTypeScript\`\`\`
import Link from 'next/link'

export default function Forbidden() {
 return (
 \
 \Forbidden\
 \You are not authorized to access this resource.\
 \Return Home\
 \
 )
}
\`\`\`

## [Reference](#reference)

### [Props](#props)

`forbidden.js` components do not accept any props.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.1.0` | `forbidden.js` introduced. |

## Next Steps

[### forbidden

API Reference for the forbidden function.](/docs/app/api-reference/functions/forbidden)Was this helpful?



## Components: <Image> | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/components/image)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Components](/docs/app/api-reference/components)\# \

Examples* [Image Component](https://github.com/vercel/next.js/tree/canary/examples/image-component)

This API reference will help you understand how to use [props](#props) and [configuration options](#configuration-options) available for the Image Component. For features and usage, please see the [Image Component](/docs/app/building-your-application/optimizing/images) page.

app/page.js\`\`\`
import Image from 'next/image'

export default function Page() {
 return (
 \
 )
}
\`\`\`
## [Props](#props)

Here's a summary of the props available for the Image Component:

| Prop | Example | Type | Status |
| --- | --- | --- | --- |
| [`src`](#src) | `src="/profile.png"` | String | Required |
| [`width`](#width) | `width={500}` | Integer (px) | Required |
| [`height`](#height) | `height={500}` | Integer (px) | Required |
| [`alt`](#alt) | `alt="Picture of the author"` | String | Required |
| [`loader`](#loader) | `loader={imageLoader}` | Function | \- |
| [`fill`](#fill) | `fill={true}` | Boolean | \- |
| [`sizes`](#sizes) | `sizes="(max-width: 768px) 100vw, 33vw"` | String | \- |
| [`quality`](#quality) | `quality={80}` | Integer (1\-100\) | \- |
| [`priority`](#priority) | `priority={true}` | Boolean | \- |
| [`placeholder`](#placeholder) | `placeholder="blur"` | String | \- |
| [`style`](#style) | `style={{objectFit: "contain"}}` | Object | \- |
| [`onLoadingComplete`](#onloadingcomplete) | `onLoadingComplete={img => done())}` | Function | Deprecated |
| [`onLoad`](#onload) | `onLoad={event => done())}` | Function | \- |
| [`onError`](#onerror) | `onError(event => fail()}` | Function | \- |
| [`loading`](#loading) | `loading="lazy"` | String | \- |
| [`blurDataURL`](#blurdataurl) | `blurDataURL="data:image/jpeg..."` | String | \- |
| [`overrideSrc`](#overridesrc) | `overrideSrc="/seo.png"` | String | \- |

## [Required Props](#required-props)

The Image Component requires the following properties: `src`, `alt`, `width` and `height` (or `fill`).

app/page.js\`\`\`
import Image from 'next/image'

export default function Page() {
 return (
 \
 \
 \
 )
}
\`\`\`
### [`src`](#src)

Must be one of the following:

* A [statically imported](/docs/app/building-your-application/optimizing/images#local-images) image file
* A path string. This can be either an absolute external URL, or an internal path depending on the [loader](#loader) prop.

When using the default [loader](#loader), also consider the following for source images:

* When src is an external URL, you must also configure [remotePatterns](#remotepatterns)
* When src is [animated](#animated-images) or not a known format (JPEG, PNG, WebP, AVIF, GIF, TIFF) the image will be served as\-is
* When src is SVG format, it will be blocked unless [`unoptimized`](#unoptimized) or [`dangerouslyAllowSVG`](#dangerouslyallowsvg) is enabled

### [`width`](#width)

The `width` property represents the *intrinsic* image width in pixels. This property is used to infer the correct aspect ratio of the image and avoid layout shift during loading. It does not determine the rendered size of the image, which is controlled by CSS, similar to the `width` attribute in the HTML `` tag.

Required, except for [statically imported images](/docs/app/building-your-application/optimizing/images#local-images) or images with the [`fill` property](#fill).

### [`height`](#height)

The `height` property represents the *intrinsic* image height in pixels. This property is used to infer the correct aspect ratio of the image and avoid layout shift during loading. It does not determine the rendered size of the image, which is controlled by CSS, similar to the `height` attribute in the HTML `` tag.

Required, except for [statically imported images](/docs/app/building-your-application/optimizing/images#local-images) or images with the [`fill` property](#fill).

> **Good to know:**
> 
> 
> * Combined, both `width` and `height` properties are used to determine the aspect ratio of the image which used by browsers to reserve space for the image before it loads.
> * The intrinsic size does not always mean the rendered size in the browser, which will be determined by the parent container. For example, if the parent container is smaller than the intrinsic size, the image will be scaled down to fit the container.
> * You can use the [`fill`](#fill) property when the width and height are unknown.

### [`alt`](#alt)

The `alt` property is used to describe the image for screen readers and search engines. It is also the fallback text if images have been disabled or an error occurs while loading the image.

It should contain text that could replace the image [without changing the meaning of the page](https://html.spec.whatwg.org/multipage/images.html#general-guidelines). It is not meant to supplement the image and should not repeat information that is already provided in the captions above or below the image.

If the image is [purely decorative](https://html.spec.whatwg.org/multipage/images.html#a-purely-decorative-image-that-doesn't-add-any-information) or [not intended for the user](https://html.spec.whatwg.org/multipage/images.html#an-image-not-intended-for-the-user), the `alt` property should be an empty string (`alt=""`).

[Learn more](https://html.spec.whatwg.org/multipage/images.html#alt)

## [Optional Props](#optional-props)

The `` component accepts a number of additional properties beyond those which are required. This section describes the most commonly\-used properties of the Image component. Find details about more rarely\-used properties in the [Advanced Props](#advanced-props) section.

### [`loader`](#loader)

A custom function used to resolve image URLs.

A `loader` is a function returning a URL string for the image, given the following parameters:

* [`src`](#src)
* [`width`](#width)
* [`quality`](#quality)

Here is an example of using a custom loader:

\`\`\`
'use client'

import Image from 'next/image'

const imageLoader = ({ src, width, quality }) =\> {
 return \`https://example.com/${src}?w=${width}\&q=${quality \|\| 75}\`
}

export default function Page() {
 return (
 \
 )
}
\`\`\`
> **Good to know**: Using props like `loader`, which accept a function, requires using [Client Components](/docs/app/building-your-application/rendering/client-components) to serialize the provided function.

Alternatively, you can use the [loaderFile](#loaderfile) configuration in `next.config.js` to configure every instance of `next/image` in your application, without passing a prop.

### [`fill`](#fill)

\`\`\`
fill={true} // {true} \| {false}
\`\`\`
A boolean that causes the image to fill the parent element, which is useful when the [`width`](#width) and [`height`](#height) are unknown.

The parent element *must* assign `position: "relative"`, `position: "fixed"`, or `position: "absolute"` style.

By default, the img element will automatically be assigned the `position: "absolute"` style.

If no styles are applied to the image, the image will stretch to fit the container. You may prefer to set `object-fit: "contain"` for an image which is letterboxed to fit the container and preserve aspect ratio.

Alternatively, `object-fit: "cover"` will cause the image to fill the entire container and be cropped to preserve aspect ratio.

For more information, see also:

* [`position`](https://developer.mozilla.org/docs/Web/CSS/position)
* [`object-fit`](https://developer.mozilla.org/docs/Web/CSS/object-fit)
* [`object-position`](https://developer.mozilla.org/docs/Web/CSS/object-position)

### [`sizes`](#sizes)

A string, similar to a media query, that provides information about how wide the image will be at different breakpoints. The value of `sizes` will greatly affect performance for images using [`fill`](#fill) or which are [styled to have a responsive size](#responsive-images).

The `sizes` property serves two important purposes related to image performance:

* First, the value of `sizes` is used by the browser to determine which size of the image to download, from `next/image`'s automatically generated `srcset`. When the browser chooses, it does not yet know the size of the image on the page, so it selects an image that is the same size or larger than the viewport. The `sizes` property allows you to tell the browser that the image will actually be smaller than full screen. If you don't specify a `sizes` value in an image with the `fill` property, a default value of `100vw` (full screen width) is used.
* Second, the `sizes` property changes the behavior of the automatically generated `srcset` value. If no `sizes` value is present, a small `srcset` is generated, suitable for a fixed\-size image (1x/2x/etc). If `sizes` is defined, a large `srcset` is generated, suitable for a responsive image (640w/750w/etc). If the `sizes` property includes sizes such as `50vw`, which represent a percentage of the viewport width, then the `srcset` is trimmed to not include any values which are too small to ever be necessary.

For example, if you know your styling will cause an image to be full\-width on mobile devices, in a 2\-column layout on tablets, and a 3\-column layout on desktop displays, you should include a sizes property such as the following:

\`\`\`
import Image from 'next/image'

export default function Page() {
 return (
 \
 \
 \
 )
}
\`\`\`
This example `sizes` could have a dramatic effect on performance metrics. Without the `33vw` sizes, the image selected from the server would be 3 times as wide as it needs to be. Because file size is proportional to the square of the width, without `sizes` the user would download an image that's 9 times larger than necessary.

Learn more about `srcset` and `sizes`:

* [web.dev](https://web.dev/learn/design/responsive-images/#sizes)
* [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#sizes)

### [`quality`](#quality)

\`\`\`
quality={75} // {number 1\-100}
\`\`\`
The quality of the optimized image, an integer between `1` and `100`, where `100` is the best quality and therefore largest file size. Defaults to `75`.

### [`priority`](#priority)

\`\`\`
priority={false} // {false} \| {true}
\`\`\`
When true, the image will be considered high priority and
[preload](https://web.dev/preload-responsive-images/). Lazy loading is automatically disabled for images using `priority`. If the [`loading`](#loading) property is also used and set to `lazy`, the `priority` property can't be used. The [`loading`](#loading) property is only meant for advanced use cases. Remove `loading` when `priority` is needed.

You should use the `priority` property on any image detected as the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element. It may be appropriate to have multiple priority images, as different images may be the LCP element for different viewport sizes.

Should only be used when the image is visible above the fold. Defaults to `false`.

### [`placeholder`](#placeholder)

\`\`\`
placeholder = 'empty' // "empty" \| "blur" \| "data:image/..."
\`\`\`
A placeholder to use while the image is loading. Possible values are `blur`, `empty`, or `data:image/...`. Defaults to `empty`.

When `blur`, the [`blurDataURL`](#blurdataurl) property will be used as the placeholder. If `src` is an object from a [static import](/docs/app/building-your-application/optimizing/images#local-images) and the imported image is `.jpg`, `.png`, `.webp`, or `.avif`, then `blurDataURL` will be automatically populated, except when the image is detected to be animated.

For dynamic images, you must provide the [`blurDataURL`](#blurdataurl) property. Solutions such as [Plaiceholder](https://github.com/joe-bell/plaiceholder) can help with `base64` generation.

When `data:image/...`, the [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) will be used as the placeholder while the image is loading.

When `empty`, there will be no placeholder while the image is loading, only empty space.

Try it out:

* [Demo the `blur` placeholder](https://image-component.nextjs.gallery/placeholder)
* [Demo the shimmer effect with data URL `placeholder` prop](https://image-component.nextjs.gallery/shimmer)
* [Demo the color effect with `blurDataURL` prop](https://image-component.nextjs.gallery/color)

## [Advanced Props](#advanced-props)

In some cases, you may need more advanced usage. The `` component optionally accepts the following advanced properties.

### [`style`](#style)

Allows passing CSS styles to the underlying image element.

components/ProfileImage.js\`\`\`
const imageStyle = {
 borderRadius: '50%',
 border: '1px solid \#fff',
}

export default function ProfileImage() {
 return \
}
\`\`\`
Remember that the required width and height props can interact with your styling. If you use styling to modify an image's width, you should also style its height to `auto` to preserve its intrinsic aspect ratio, or your image will be distorted.

### [`onLoadingComplete`](#onloadingcomplete)

\`\`\`
'use client'

\ console.log(img.naturalWidth)} /\>
\`\`\`

> **Warning**: Deprecated since Next.js 14 in favor of [`onLoad`](#onload).

A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

The callback function will be called with one argument, a reference to the underlying `` element.

> **Good to know**: Using props like `onLoadingComplete`, which accept a function, requires using [Client Components](/docs/app/building-your-application/rendering/client-components) to serialize the provided function.

### [`onLoad`](#onload)

\`\`\`
\ console.log(e.target.naturalWidth)} /\>
\`\`\`
A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

The callback function will be called with one argument, the Event which has a `target` that references the underlying `` element.

> **Good to know**: Using props like `onLoad`, which accept a function, requires using [Client Components](/docs/app/building-your-application/rendering/client-components) to serialize the provided function.

### [`onError`](#onerror)

\`\`\`
\ console.error(e.target.id)} /\>
\`\`\`
A callback function that is invoked if the image fails to load.

> **Good to know**: Using props like `onError`, which accept a function, requires using [Client Components](/docs/app/building-your-application/rendering/client-components) to serialize the provided function.

### [`loading`](#loading)

\`\`\`
loading = 'lazy' // {lazy} \| {eager}
\`\`\`
The loading behavior of the image. Defaults to `lazy`.

When `lazy`, defer loading the image until it reaches a calculated distance from
the viewport.

When `eager`, load the image immediately.

Learn more about the [`loading` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#loading).

### [`blurDataURL`](#blurdataurl)

A [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) to
be used as a placeholder image before the `src` image successfully loads. Only takes effect when combined
with [`placeholder="blur"`](#placeholder).

Must be a base64\-encoded image. It will be enlarged and blurred, so a very small image (10px or
less) is recommended. Including larger images as placeholders may harm your application performance.

Try it out:

* [Demo the default `blurDataURL` prop](https://image-component.nextjs.gallery/placeholder)
* [Demo the color effect with `blurDataURL` prop](https://image-component.nextjs.gallery/color)

You can also [generate a solid color Data URL](https://png-pixel.com) to match the image.

### [`unoptimized`](#unoptimized)

\`\`\`
unoptimized = {false} // {false} \| {true}
\`\`\`
When true, the source image will be served as\-is from the `src` instead of changing quality, size, or format. Defaults to `false`.

This is useful for images that do not benefit from optimization such as small images (less than 1KB), vector images (SVG), or animated images (GIF).

\`\`\`
import Image from 'next/image'

const UnoptimizedImage = (props) =\> {
 return \
}
\`\`\`
Since Next.js 12\.3\.0, this prop can be assigned to all images by updating `next.config.js` with the following configuration:

next.config.js\`\`\`
module.exports = {
 images: {
 unoptimized: true,
 },
}
\`\`\`
### [`overrideSrc`](#overridesrc)

When providing the `src` prop to the `` component, both the `srcset` and `src` attributes are generated automatically for the resulting ``.

input.js\`\`\`
\
\`\`\`
output.html\`\`\`
\
\`\`\`
In some cases, it is not desirable to have the `src` attribute generated and you may wish to override it using the `overrideSrc` prop.

For example, when upgrading an existing website from `` to ``, you may wish to maintain the same `src` attribute for SEO purposes such as image ranking or avoiding recrawl.

input.js\`\`\`
\
\`\`\`
output.html\`\`\`
\
\`\`\`
### [decoding](#decoding)

A hint to the browser indicating if it should wait for the image to be decoded before presenting other content updates or not. Defaults to `async`.

Possible values are the following:

* `async` \- Asynchronously decode the image and allow other content to be rendered before it completes.
* `sync` \- Synchronously decode the image for atomic presentation with other content.
* `auto` \- No preference for the decoding mode; the browser decides what's best.

Learn more about the [`decoding` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#decoding).

### [Other Props](#other-props)

Other properties on the `` component will be passed to the underlying
`img` element with the exception of the following:

* `srcSet`. Use [Device Sizes](#devicesizes) instead.

## [Configuration Options](#configuration-options)

In addition to props, you can configure the Image Component in `next.config.js`. The following options are available:

### [`localPatterns`](#localpatterns)

You can optionally configure `localPatterns` in your `next.config.js` file in order to allow specific paths to be optimized and block all others paths.

next.config.js\`\`\`
module.exports = {
 images: {
 localPatterns: \[
 {
 pathname: '/assets/images/\*\*',
 search: '',
 },
 ],
 },
}
\`\`\`

> **Good to know**: The example above will ensure the `src` property of `next/image` must start with `/assets/images/` and must not have a query string. Attempting to optimize any other path will respond with 400 Bad Request.

### [`remotePatterns`](#remotepatterns)

To protect your application from malicious users, configuration is required in order to use external images. This ensures that only external images from your account can be served from the Next.js Image Optimization API. These external images can be configured with the `remotePatterns` property in your `next.config.js` file, as shown below:

next.config.js\`\`\`
module.exports = {
 images: {
 remotePatterns: \[
 {
 protocol: 'https',
 hostname: 'example.com',
 port: '',
 pathname: '/account123/\*\*',
 search: '',
 },
 ],
 },
}
\`\`\`

> **Good to know**: The example above will ensure the `src` property of `next/image` must start with `https://example.com/account123/` and must not have a query string. Any other protocol, hostname, port, or unmatched path will respond with 400 Bad Request.

Below is an example of the `remotePatterns` property in the `next.config.js` file using a wildcard pattern in the `hostname`:

next.config.js\`\`\`
module.exports = {
 images: {
 remotePatterns: \[
 {
 protocol: 'https',
 hostname: '\*\*.example.com',
 port: '',
 search: '',
 },
 ],
 },
}
\`\`\`

> **Good to know**: The example above will ensure the `src` property of `next/image` must start with `https://img1.example.com` or `https://me.avatar.example.com` or any number of subdomains. It cannot have a port or query string. Any other protocol or unmatched hostname will respond with 400 Bad Request.

Wildcard patterns can be used for both `pathname` and `hostname` and have the following syntax:

* `*` match a single path segment or subdomain
* `**` match any number of path segments at the end or subdomains at the beginning

The `**` syntax does not work in the middle of the pattern.

> **Good to know**: When omitting `protocol`, `port`, `pathname`, or `search` then the wildcard `**` is implied. This is not recommended because it may allow malicious actors to optimize urls you did not intend.

Below is an example of the `remotePatterns` property in the `next.config.js` file using `search`:

next.config.js\`\`\`
module.exports = {
 images: {
 remotePatterns: \[
 {
 protocol: 'https',
 hostname: 'assets.example.com',
 search: '?v=1727111025337',
 },
 ],
 },
}
\`\`\`

> **Good to know**: The example above will ensure the `src` property of `next/image` must start with `https://assets.example.com` and must have the exact query string `?v=1727111025337`. Any other protocol or query string will respond with 400 Bad Request.

### [`domains`](#domains)

> **Warning**: Deprecated since Next.js 14 in favor of strict [`remotePatterns`](#remotepatterns) in order to protect your application from malicious users. Only use `domains` if you own all the content served from the domain.

Similar to [`remotePatterns`](#remotepatterns), the `domains` configuration can be used to provide a list of allowed hostnames for external images.

However, the `domains` configuration does not support wildcard pattern matching and it cannot restrict protocol, port, or pathname.

Below is an example of the `domains` property in the `next.config.js` file:

next.config.js\`\`\`
module.exports = {
 images: {
 domains: \['assets.acme.com'],
 },
}
\`\`\`
### [`loaderFile`](#loaderfile)

If you want to use a cloud provider to optimize images instead of using the Next.js built\-in Image Optimization API, you can configure the `loaderFile` in your `next.config.js` like the following:

next.config.js\`\`\`
module.exports = {
 images: {
 loader: 'custom',
 loaderFile: './my/image/loader.js',
 },
}
\`\`\`
This must point to a file relative to the root of your Next.js application. The file must export a default function that returns a string, for example:

my/image/loader.js\`\`\`
'use client'

export default function myImageLoader({ src, width, quality }) {
 return \`https://example.com/${src}?w=${width}\&q=${quality \|\| 75}\`
}
\`\`\`

Alternatively, you can use the [`loader` prop](#loader) to configure each instance of `next/image`.

Examples:

* [Custom Image Loader Configuration](/docs/app/api-reference/config/next-config-js/images#example-loader-configuration)

> **Good to know**: Customizing the image loader file, which accepts a function, requires using [Client Components](/docs/app/building-your-application/rendering/client-components) to serialize the provided function.

## [Advanced](#advanced)

The following configuration is for advanced use cases and is usually not necessary. If you choose to configure the properties below, you will override any changes to the Next.js defaults in future updates.

### [`deviceSizes`](#devicesizes)

If you know the expected device widths of your users, you can specify a list of device width breakpoints using the `deviceSizes` property in `next.config.js`. These widths are used when the `next/image` component uses [`sizes`](#sizes) prop to ensure the correct image is served for user's device.

If no configuration is provided, the default below is used.

next.config.js\`\`\`
module.exports = {
 images: {
 deviceSizes: \[640, 750, 828, 1080, 1200, 1920, 2048, 3840],
 },
}
\`\`\`
### [`imageSizes`](#imagesizes)

You can specify a list of image widths using the `images.imageSizes` property in your `next.config.js` file. These widths are concatenated with the array of [device sizes](#devicesizes) to form the full array of sizes used to generate image [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset)s.

The reason there are two separate lists is that imageSizes is only used for images which provide a [`sizes`](#sizes) prop, which indicates that the image is less than the full width of the screen. **Therefore, the sizes in imageSizes should all be smaller than the smallest size in deviceSizes.**

If no configuration is provided, the default below is used.

next.config.js\`\`\`
module.exports = {
 images: {
 imageSizes: \[16, 32, 48, 64, 96, 128, 256, 384],
 },
}
\`\`\`
### [`formats`](#formats)

The default [Image Optimization API](#loader) will automatically detect the browser's supported image formats via the request's `Accept` header in order to determine the best output format.

If the `Accept` header matches more than one of the configured formats, the first match in the array is used. Therefore, the array order matters. If there is no match (or the source image is [animated](#animated-images)), the Image Optimization API will fallback to the original image's format.

If no configuration is provided, the default below is used.

next.config.js\`\`\`
module.exports = {
 images: {
 formats: \['image/webp'],
 },
}
\`\`\`
You can enable AVIF support and still fallback to WebP with the following configuration.

next.config.js\`\`\`
module.exports = {
 images: {
 formats: \['image/avif', 'image/webp'],
 },
}
\`\`\`

> **Good to know**:
> 
> 
> * AVIF generally takes 50% longer to encode but it compresses 20% smaller compared to WebP. This means that the first time an image is requested, it will typically be slower and then subsequent requests that are cached will be faster.
> * If you self\-host with a Proxy/CDN in front of Next.js, you must configure the Proxy to forward the `Accept` header.

## [Caching Behavior](#caching-behavior)

The following describes the caching algorithm for the default [loader](#loader). For all other loaders, please refer to your cloud provider's documentation.

Images are optimized dynamically upon request and stored in the `/cache/images` directory. The optimized image file will be served for subsequent requests until the expiration is reached. When a request is made that matches a cached but expired file, the expired image is served stale immediately. Then the image is optimized again in the background (also called revalidation) and saved to the cache with the new expiration date.

The cache status of an image can be determined by reading the value of the `x-nextjs-cache` response header. The possible values are the following:

* `MISS` \- the path is not in the cache (occurs at most once, on the first visit)
* `STALE` \- the path is in the cache but exceeded the revalidate time so it will be updated in the background
* `HIT` \- the path is in the cache and has not exceeded the revalidate time

The expiration (or rather Max Age) is defined by either the [`minimumCacheTTL`](#minimumcachettl) configuration or the upstream image `Cache-Control` header, whichever is larger. Specifically, the `max-age` value of the `Cache-Control` header is used. If both `s-maxage` and `max-age` are found, then `s-maxage` is preferred. The `max-age` is also passed\-through to any downstream clients including CDNs and browsers.

* You can configure [`minimumCacheTTL`](#minimumcachettl) to increase the cache duration when the upstream image does not include `Cache-Control` header or the value is very low.
* You can configure [`deviceSizes`](#devicesizes) and [`imageSizes`](#imagesizes) to reduce the total number of possible generated images.
* You can configure [formats](#formats) to disable multiple formats in favor of a single image format.

### [`minimumCacheTTL`](#minimumcachettl)

You can configure the Time to Live (TTL) in seconds for cached optimized images. In many cases, it's better to use a [Static Image Import](/docs/app/building-your-application/optimizing/images#local-images) which will automatically hash the file contents and cache the image forever with a `Cache-Control` header of `immutable`.

next.config.js\`\`\`
module.exports = {
 images: {
 minimumCacheTTL: 60,
 },
}
\`\`\`
The expiration (or rather Max Age) of the optimized image is defined by either the `minimumCacheTTL` or the upstream image `Cache-Control` header, whichever is larger.

If you need to change the caching behavior per image, you can configure [`headers`](/docs/app/api-reference/config/next-config-js/headers) to set the `Cache-Control` header on the upstream image (e.g. `/some-asset.jpg`, not `/_next/image` itself).

There is no mechanism to invalidate the cache at this time, so its best to keep `minimumCacheTTL` low. Otherwise you may need to manually change the [`src`](#src) prop or delete `/cache/images`.

### [`disableStaticImages`](#disablestaticimages)

The default behavior allows you to import static files such as `import icon from './icon.png'` and then pass that to the `src` property.

In some cases, you may wish to disable this feature if it conflicts with other plugins that expect the import to behave differently.

You can disable static image imports inside your `next.config.js`:

next.config.js\`\`\`
module.exports = {
 images: {
 disableStaticImages: true,
 },
}
\`\`\`
### [`dangerouslyAllowSVG`](#dangerouslyallowsvg)

The default [loader](#loader) does not optimize SVG images for a few reasons. First, SVG is a vector format meaning it can be resized losslessly. Second, SVG has many of the same features as HTML/CSS, which can lead to vulnerabilities without proper [Content Security Policy (CSP) headers](/docs/app/api-reference/config/next-config-js/headers#content-security-policy).

Therefore, we recommended using the [`unoptimized`](#unoptimized) prop when the [`src`](#src) prop is known to be SVG. This happens automatically when `src` ends with `".svg"`.

However, if you need to serve SVG images with the default Image Optimization API, you can set `dangerouslyAllowSVG` inside your `next.config.js`:

next.config.js\`\`\`
module.exports = {
 images: {
 dangerouslyAllowSVG: true,
 contentDispositionType: 'attachment',
 contentSecurityPolicy: "default\-src 'self'; script\-src 'none'; sandbox;",
 },
}
\`\`\`
In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.

### [`contentDispositionType`](#contentdispositiontype)

The default [loader](#loader) sets the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) header to `attachment` for added protection since the API can serve arbitrary remote images.

The default value is `attachment` which forces the browser to download the image when visiting directly. This is particularly important when [`dangerouslyAllowSVG`](#dangerouslyallowsvg) is true.

You can optionally configure `inline` to allow the browser to render the image when visiting directly, without downloading it.

next.config.js\`\`\`
module.exports = {
 images: {
 contentDispositionType: 'inline',
 },
}
\`\`\`
## [Animated Images](#animated-images)

The default [loader](#loader) will automatically bypass Image Optimization for animated images and serve the image as\-is.

Auto\-detection for animated files is best\-effort and supports GIF, APNG, and WebP. If you want to explicitly bypass Image Optimization for a given animated image, use the [unoptimized](#unoptimized) prop.

## [Responsive Images](#responsive-images)

The default generated `srcset` contains `1x` and `2x` images in order to support different device pixel ratios. However, you may wish to render a responsive image that stretches with the viewport. In that case, you'll need to set [`sizes`](#sizes) as well as `style` (or `className`).

You can render a responsive image using one of the following methods below.

### [Responsive image using a static import](#responsive-image-using-a-static-import)

If the source image is not dynamic, you can statically import to create a responsive image:

components/author.js\`\`\`
import Image from 'next/image'
import me from '../photos/me.jpg'

export default function Author() {
 return (
 \
 )
}
\`\`\`
Try it out:

* [Demo the image responsive to viewport](https://image-component.nextjs.gallery/responsive)

### [Responsive image with aspect ratio](#responsive-image-with-aspect-ratio)

If the source image is a dynamic or a remote url, you will also need to provide `width` and `height` to set the correct aspect ratio of the responsive image:

components/page.js\`\`\`
import Image from 'next/image'

export default function Page({ photoUrl }) {
 return (
 \
 )
}
\`\`\`
Try it out:

* [Demo the image responsive to viewport](https://image-component.nextjs.gallery/responsive)

### [Responsive image with `fill`](#responsive-image-with-fill)

If you don't know the aspect ratio, you will need to set the [`fill`](#fill) prop and set `position: relative` on the parent. Optionally, you can set `object-fit` style depending on the desired stretch vs crop behavior:

app/page.js\`\`\`
import Image from 'next/image'

export default function Page({ photoUrl }) {
 return (
 \
 \
 \
 )
}
\`\`\`
Try it out:

* [Demo the `fill` prop](https://image-component.nextjs.gallery/fill)

## [Theme Detection CSS](#theme-detection-css)

If you want to display a different image for light and dark mode, you can create a new component that wraps two `` components and reveals the correct one based on a CSS media query.

components/theme\-image.module.css\`\`\`
.imgDark {
 display: none;
}

@media (prefers\-color\-scheme: dark) {
 .imgLight {
 display: none;
 }
 .imgDark {
 display: unset;
 }
}
\`\`\`
components/theme\-image.tsxTypeScriptJavaScriptTypeScript\`\`\`
import styles from './theme\-image.module.css'
import Image, { ImageProps } from 'next/image'

type Props = Omit\ \& {
 srcLight: string
 srcDark: string
}

const ThemeImage = (props: Props) =\> {
 const { srcLight, srcDark, ...rest } = props

 return (
 \
 \
 \
 \
 )
}
\`\`\`

> **Good to know**: The default behavior of `loading="lazy"` ensures that only the correct image is loaded. You cannot use `priority` or `loading="eager"` because that would cause both images to load. Instead, you can use [`fetchPriority="high"`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/fetchPriority).

Try it out:

* [Demo light/dark mode theme detection](https://image-component.nextjs.gallery/theme)

## [getImageProps](#getimageprops)

For more advanced use cases, you can call `getImageProps()` to get the props that would be passed to the underlying `` element, and instead pass to them to another component, style, canvas, etc.

This also avoid calling React `useState()` so it can lead to better performance, but it cannot be used with the [`placeholder`](#placeholder) prop because the placeholder will never be removed.

### [Theme Detection Picture](#theme-detection-picture)

If you want to display a different image for light and dark mode, you can use the [``](https://developer.mozilla.org/docs/Web/HTML/Element/picture) element to display a different image based on the user's [preferred color scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme).

app/page.js\`\`\`
import { getImageProps } from 'next/image'

export default function Page() {
 const common = { alt: 'Theme Example', width: 800, height: 400 }
 const {
 props: { srcSet: dark },
 } = getImageProps({ ...common, src: '/dark.png' })
 const {
 props: { srcSet: light, ...rest },
 } = getImageProps({ ...common, src: '/light.png' })

 return (
 \
 \
 \
 \
 \
 )
}
\`\`\`
### [Art Direction](#art-direction)

If you want to display a different image for mobile and desktop, sometimes called [Art Direction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction), you can provide different `src`, `width`, `height`, and `quality` props to `getImageProps()`.

app/page.js\`\`\`
import { getImageProps } from 'next/image'

export default function Home() {
 const common = { alt: 'Art Direction Example', sizes: '100vw' }
 const {
 props: { srcSet: desktop },
 } = getImageProps({
 ...common,
 width: 1440,
 height: 875,
 quality: 80,
 src: '/desktop.jpg',
 })
 const {
 props: { srcSet: mobile, ...rest },
 } = getImageProps({
 ...common,
 width: 750,
 height: 1334,
 quality: 70,
 src: '/mobile.jpg',
 })

 return (
 \
 \
 \
 \
 \
 )
}
\`\`\`
### [Background CSS](#background-css)

You can even convert the `srcSet` string to the [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/image/image-set) CSS function to optimize a background image.

app/page.js\`\`\`
import { getImageProps } from 'next/image'

function getBackgroundImage(srcSet = '') {
 const imageSet = srcSet
 .split(', ')
 .map((str) =\> {
 const \[url, dpi] = str.split(' ')
 return \`url("${url}") ${dpi}\`
 })
 .join(', ')
 return \`image\-set(${imageSet})\`
}

export default function Home() {
 const {
 props: { srcSet },
 } = getImageProps({ alt: '', width: 128, height: 128, src: '/img.png' })
 const backgroundImage = getBackgroundImage(srcSet)
 const style = { height: '100vh', width: '100vw', backgroundImage }

 return (
 \
 \Hello World\
 \
 )
}
\`\`\`
## [Known Browser Bugs](#known-browser-bugs)

This `next/image` component uses browser native [lazy loading](https://caniuse.com/loading-lazy-attr), which may fallback to eager loading for older browsers before Safari 15\.4\. When using the blur\-up placeholder, older browsers before Safari 12 will fallback to empty placeholder. When using styles with `width`/`height` of `auto`, it is possible to cause [Layout Shift](https://web.dev/cls/) on older browsers before Safari 15 that don't [preserve the aspect ratio](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes). For more details, see [this MDN video](https://www.youtube.com/watch?v=4-d_SoCHeWE).

* [Safari 15 \- 16\.3](https://bugs.webkit.org/show_bug.cgi?id=243601) display a gray border while loading. Safari 16\.4 [fixed this issue](https://webkit.org/blog/13966/webkit-features-in-safari-16-4/#:~:text=Now%20in%20Safari%2016.4%2C%20a%20gray%20line%20no%20longer%20appears%20to%20mark%20the%20space%20where%20a%20lazy%2Dloaded%20image%20will%20appear%20once%20it%E2%80%99s%20been%20loaded.). Possible solutions:
	+ Use CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }`
	+ Use [`priority`](#priority) if the image is above the fold
* [Firefox 67\+](https://bugzilla.mozilla.org/show_bug.cgi?id=1556156) displays a white background while loading. Possible solutions:
	+ Enable [AVIF `formats`](#formats)
	+ Use [`placeholder`](#placeholder)

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `contentDispositionType` configuration default changed to `attachment`. |
| `v14.2.15` | `decoding` prop added and `localPatterns` configuration added. |
| `v14.2.14` | `remotePatterns.search` prop added. |
| `v14.2.0` | `overrideSrc` prop added. |
| `v14.1.0` | `getImageProps()` is stable. |
| `v14.0.0` | `onLoadingComplete` prop and `domains` config deprecated. |
| `v13.4.14` | `placeholder` prop support for `data:/image...` |
| `v13.2.0` | `contentDispositionType` configuration added. |
| `v13.0.6` | `ref` prop added. |
| `v13.0.0` | The `next/image` import was renamed to `next/legacy/image`. The `next/future/image` import was renamed to `next/image`. A [codemod is available](/docs/app/building-your-application/upgrading/codemods#next-image-to-legacy-image) to safely and automatically rename your imports. `` wrapper removed. `layout`, `objectFit`, `objectPosition`, `lazyBoundary`, `lazyRoot` props removed. `alt` is required. `onLoadingComplete` receives reference to `img` element. Built\-in loader config removed. |
| `v12.3.0` | `remotePatterns` and `unoptimized` configuration is stable. |
| `v12.2.0` | Experimental `remotePatterns` and experimental `unoptimized` configuration added. `layout="raw"` removed. |
| `v12.1.1` | `style` prop added. Experimental support for `layout="raw"` added. |
| `v12.1.0` | `dangerouslyAllowSVG` and `contentSecurityPolicy` configuration added. |
| `v12.0.9` | `lazyRoot` prop added. |
| `v12.0.0` | `formats` configuration added.AVIF support added.Wrapper `` changed to ``. |
| `v11.1.0` | `onLoadingComplete` and `lazyBoundary` props added. |
| `v11.0.0` | `src` prop support for static import.`placeholder` prop added.`blurDataURL` prop added. |
| `v10.0.5` | `loader` prop added. |
| `v10.0.1` | `layout` prop added. |
| `v10.0.0` | `next/image` introduced. |

Was this helpful?



## Functions: fetch | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/fetch)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)fetch# fetch

Next.js extends the [Web `fetch()` API](https://developer.mozilla.org/docs/Web/API/Fetch_API) to allow each request on the server to set its own persistent caching and revalidation semantics.

In the browser, the `cache` option indicates how a fetch request will interact with the *browser's* HTTP cache. With this extension, `cache` indicates how a *server\-side* fetch request will interact with the framework's persistent [Data Cache](/docs/app/building-your-application/caching#data-cache).

You can call `fetch` with `async` and `await` directly within Server Components.

app/page.tsxTypeScriptJavaScriptTypeScript\`\`\`
export default async function Page() {
 let data = await fetch('https://api.vercel.app/blog')
 let posts = await data.json()
 return (
 \
 {posts.map((post) =\> (
 \{post.title}\
 ))}
 \
 )
}
\`\`\`

## [`fetch(url, options)`](#fetchurl-options)

Since Next.js extends the [Web `fetch()` API](https://developer.mozilla.org/docs/Web/API/Fetch_API), you can use any of the [native options available](https://developer.mozilla.org/docs/Web/API/fetch#parameters).

### [`options.cache`](#optionscache)

Configure how the request should interact with Next.js [Data Cache](/docs/app/building-your-application/caching#data-cache).

\`\`\`
fetch(\`https://...\`, { cache: 'force\-cache' \| 'no\-store' })
\`\`\`
* **`auto no cache`** (default): Next.js fetches the resource from the remote server on every request in development, but will fetch once during `next build` because the route will be statically prerendered. If [Dynamic APIs](/docs/app/building-your-application/rendering/server-components#dynamic-rendering) are detected on the route, Next.js will fetch the resource on every request.
* **`no-store`**: Next.js fetches the resource from the remote server on every request, even if Dynamic APIs are not detected on the route.
* **`force-cache`**: Next.js looks for a matching request in its Data Cache.
	+ If there is a match and it is fresh, it will be returned from the cache.
	+ If there is no match or a stale match, Next.js will fetch the resource from the remote server and update the cache with the downloaded resource.

### [`options.next.revalidate`](#optionsnextrevalidate)

\`\`\`
fetch(\`https://...\`, { next: { revalidate: false \| 0 \| number } })
\`\`\`
Set the cache lifetime of a resource (in seconds).

* **`false`** \- Cache the resource indefinitely. Semantically equivalent to `revalidate: Infinity`. The HTTP cache may evict older resources over time.
* **`0`** \- Prevent the resource from being cached.
* **`number`** \- (in seconds) Specify the resource should have a cache lifetime of at most `n` seconds.

> **Good to know**:
> 
> 
> * If an individual `fetch()` request sets a `revalidate` number lower than the [default `revalidate`](/docs/app/api-reference/file-conventions/route-segment-config#revalidate) of a route, the whole route revalidation interval will be decreased.
> * If two fetch requests with the same URL in the same route have different `revalidate` values, the lower value will be used.
> * As a convenience, it is not necessary to set the `cache` option if `revalidate` is set to a number.
> * Conflicting options such as `{ revalidate: 3600, cache: 'no-store' }` will cause an error.

### [`options.next.tags`](#optionsnexttags)

\`\`\`
fetch(\`https://...\`, { next: { tags: \['collection'] } })
\`\`\`
Set the cache tags of a resource. Data can then be revalidated on\-demand using [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag). The max length for a custom tag is 256 characters and the max tag items is 128\.

## [Troubleshooting](#troubleshooting)

### [Fetch default `auto no store` and `cache: 'no-store'` not showing fresh data in development](#fetch-default-auto-no-store-and-cache-no-store-not-showing-fresh-data-in-development)

Next.js caches `fetch` responses in Server Components across Hot Module Replacement (HMR) in local development for faster responses and to reduce costs for billed API calls.

By default, the [HMR cache](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) applies to all fetch requests, including those with the default `auto no cache` and `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full\-page reloads.

See the [`serverComponentsHmrCache`](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) docs for more information.

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `fetch` introduced. |

Was this helpful?



## Getting Started: Project Structure | Next.js

[Read the full article](https://nextjs.org/docs/app/getting-started/project-structure)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Project Structure# Project structure and organization

This page provides an overview of the folder and file conventions in Next.js, as well as tips for organizing your project.

## [Folder and file conventions](#folder-and-file-conventions)

### [Top\-level folders](#top-level-folders)

Top\-level folders are used to organize your application's code and static assets.



|  |  |
| --- | --- |
| [`app`](/docs/app/building-your-application/routing) | App Router |
| [`pages`](/docs/pages/building-your-application/routing) | Pages Router |
| [`public`](/docs/app/building-your-application/optimizing/static-assets) | Static assets to be served |
| [`src`](/docs/app/building-your-application/configuring/src-directory) | Optional application source folder |

### [Top\-level files](#top-level-files)

Top\-level files are used to configure your application, manage dependencies, run middleware, integrate monitoring tools, and define environment variables.

|  |  |
| --- | --- |
| **Next.js** |  |
| [`next.config.js`](/docs/app/api-reference/config/next-config-js) | Configuration file for Next.js |
| [`package.json`](/docs/app/getting-started/installation#manual-installation) | Project dependencies and scripts |
| [`instrumentation.ts`](/docs/app/building-your-application/optimizing/instrumentation) | OpenTelemetry and Instrumentation file |
| [`middleware.ts`](/docs/app/building-your-application/routing/middleware) | Next.js request middleware |
| [`.env`](/docs/app/building-your-application/configuring/environment-variables) | Environment variables |
| [`.env.local`](/docs/app/building-your-application/configuring/environment-variables) | Local environment variables |
| [`.env.production`](/docs/app/building-your-application/configuring/environment-variables) | Production environment variables |
| [`.env.development`](/docs/app/building-your-application/configuring/environment-variables) | Development environment variables |
| [`.eslintrc.json`](/docs/app/api-reference/config/eslint) | Configuration file for ESLint |
| `.gitignore` | Git files and folders to ignore |
| `next-env.d.ts` | TypeScript declaration file for Next.js |
| `tsconfig.json` | Configuration file for TypeScript |
| `jsconfig.json` | Configuration file for JavaScript |

### [Routing Files](#routing-files)

|  |  |  |
| --- | --- | --- |
| [`layout`](/docs/app/api-reference/file-conventions/layout) | `.js` `.jsx` `.tsx` | Layout |
| [`page`](/docs/app/api-reference/file-conventions/page) | `.js` `.jsx` `.tsx` | Page |
| [`loading`](/docs/app/api-reference/file-conventions/loading) | `.js` `.jsx` `.tsx` | Loading UI |
| [`not-found`](/docs/app/api-reference/file-conventions/not-found) | `.js` `.jsx` `.tsx` | Not found UI |
| [`error`](/docs/app/api-reference/file-conventions/error) | `.js` `.jsx` `.tsx` | Error UI |
| [`global-error`](/docs/app/api-reference/file-conventions/error#global-errorjs) | `.js` `.jsx` `.tsx` | Global error UI |
| [`route`](/docs/app/api-reference/file-conventions/route) | `.js` `.ts` | API endpoint |
| [`template`](/docs/app/api-reference/file-conventions/template) | `.js` `.jsx` `.tsx` | Re\-rendered layout |
| [`default`](/docs/app/api-reference/file-conventions/default) | `.js` `.jsx` `.tsx` | Parallel route fallback page |

### [Nested routes](#nested-routes)

|  |  |
| --- | --- |
| `folder` | Route segment |
| `folder/folder` | Nested route segment |

### [Dynamic routes](#dynamic-routes)

|  |  |
| --- | --- |
| [`[folder]`](/docs/app/building-your-application/routing/dynamic-routes#convention) | Dynamic route segment |
| [`[...folder]`](/docs/app/building-your-application/routing/dynamic-routes#catch-all-segments) | Catch\-all route segment |
| [`[[...folder]]`](/docs/app/building-your-application/routing/dynamic-routes#optional-catch-all-segments) | Optional catch\-all route segment |

### [Route Groups and private folders](#route-groups-and-private-folders)

|  |  |
| --- | --- |
| [`(folder)`](/docs/app/building-your-application/routing/route-groups#convention) | Group routes without affecting routing |
| [`_folder`](#private-folders) | Opt folder and all child segments out of routing |

### [Parallel and Intercepted Routes](#parallel-and-intercepted-routes)

|  |  |
| --- | --- |
| [`@folder`](/docs/app/building-your-application/routing/parallel-routes#slots) | Named slot |
| [`(.)folder`](/docs/app/building-your-application/routing/intercepting-routes#convention) | Intercept same level |
| [`(..)folder`](/docs/app/building-your-application/routing/intercepting-routes#convention) | Intercept one level above |
| [`(..)(..)folder`](/docs/app/building-your-application/routing/intercepting-routes#convention) | Intercept two levels above |
| [`(...)folder`](/docs/app/building-your-application/routing/intercepting-routes#convention) | Intercept from root |

### [Metadata file conventions](#metadata-file-conventions)

#### [App icons](#app-icons)

|  |  |  |
| --- | --- | --- |
| [`favicon`](/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) | `.ico` | Favicon file |
| [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#icon) | `.ico` `.jpg` `.jpeg` `.png` `.svg` | App Icon file |
| [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated App Icon |
| [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon) | `.jpg` `.jpeg`, `.png` | Apple App Icon file |
| [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated Apple App Icon |

#### [Open Graph and Twitter images](#open-graph-and-twitter-images)

|  |  |  |
| --- | --- | --- |
| [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image) | `.jpg` `.jpeg` `.png` `.gif` | Open Graph image file |
| [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated Open Graph image |
| [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image) | `.jpg` `.jpeg` `.png` `.gif` | Twitter image file |
| [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated Twitter image |

#### [SEO](#seo)

|  |  |  |
| --- | --- | --- |
| [`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml) | `.xml` | Sitemap file |
| [`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts) | `.js` `.ts` | Generated Sitemap |
| [`robots`](/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt) | `.txt` | Robots file |
| [`robots`](/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file) | `.js` `.ts` | Generated Robots file |

## [Component hierarchy](#component-hierarchy)

The React components defined in special files of a route segment are rendered in a specific hierarchy:

* `layout.js`
* `template.js`
* `error.js` (React error boundary)
* `loading.js` (React suspense boundary)
* `not-found.js` (React error boundary)
* `page.js` or nested `layout.js`

In a nested route, the components of a segment will be nested **inside** the components of its parent segment.

## [Organizing your project](#organizing-your-project)

Apart from [folder and file conventions](/docs/app/getting-started/project-structure), Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.

### [Colocation](#colocation)

In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.

And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.

This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.


> **Good to know**:
> 
> 
> * While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](#store-project-files-outside-of-app).

### [Private folders](#private-folders)

Private folders can be created by prefixing a folder with an underscore: `_folderName`

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.

Since files in the `app` directory can be [safely colocated by default](#colocation), private folders are not required for colocation. However, they can be useful for:

* Separating UI logic from routing logic.
* Consistently organizing internal files across a project and the Next.js ecosystem.
* Sorting and grouping files in code editors.
* Avoiding potential naming conflicts with future Next.js file conventions.

> **Good to know**:
> 
> 
> * While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
> * You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL\-encoded form of an underscore): `%5FfolderName`.
> * If you don't use private folders, it would be helpful to know Next.js [special file conventions](/docs/app/getting-started/project-structure#routing-files) to prevent unexpected naming conflicts.

### [Route groups](#route-groups)

Route groups can be created by wrapping a folder in parenthesis: `(folderName)`

This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

Route groups are useful for:

* [Organizing routes into groups](/docs/app/building-your-application/routing/route-groups#organize-routes-without-affecting-the-url-path) e.g. by site section, intent, or team.
* Enabling nested layouts in the same route segment level:
	+ [Creating multiple nested layouts in the same segment, including multiple root layouts](/docs/app/building-your-application/routing/route-groups#creating-multiple-root-layouts)
	+ [Adding a layout to a subset of routes in a common segment](/docs/app/building-your-application/routing/route-groups#opting-specific-segments-into-a-layout)

### [`src` directory](#src-directory)

Next.js supports storing application code (including `app`) inside an optional [`src` directory](/docs/app/building-your-application/configuring/src-directory). This separates application code from project configuration files which mostly live in the root of a project.

### [Common strategies](#common-strategies)

The following section lists a very high\-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

> **Good to know**: In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.

#### [Store project files outside of `app`](#store-project-files-outside-of-app)

This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.

#### [Store project files in top\-level folders inside of `app`](#store-project-files-in-top-level-folders-inside-of-app)

This strategy stores all application code in shared folders in the **root of the `app` directory**.

#### [Split project files by feature or route](#split-project-files-by-feature-or-route)

This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.

Was this helpful?



## Functions: useSelectedLayoutSegment | Next.js

[Read the full article](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)

 MenuUsing App Router

Features available in /app

Using Latest Version

15\.1\.3

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)useSelectedLayoutSegment# useSelectedLayoutSegment

`useSelectedLayoutSegment` is a **Client Component** hook that lets you read the active route segment **one level below** the Layout it is called from.

It is useful for navigation UI, such as tabs inside a parent layout that change style depending on the active child segment.

app/example\-client\-component.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function ExampleClientComponent() {
 const segment = useSelectedLayoutSegment()

 return \Active segment: {segment}\
}
\`\`\`

> **Good to know**:
> 
> 
> * Since `useSelectedLayoutSegment` is a [Client Component](/docs/app/building-your-application/rendering/client-components) hook, and Layouts are [Server Components](/docs/app/building-your-application/rendering/server-components) by default, `useSelectedLayoutSegment` is usually called via a Client Component that is imported into a Layout.
> * `useSelectedLayoutSegment` only returns the segment one level down. To return all active segments, see [`useSelectedLayoutSegments`](/docs/app/api-reference/functions/use-selected-layout-segments)

## [Parameters](#parameters)

\`\`\`
const segment = useSelectedLayoutSegment(parallelRoutesKey?: string)
\`\`\`
`useSelectedLayoutSegment` *optionally* accepts a [`parallelRoutesKey`](/docs/app/building-your-application/routing/parallel-routes#useselectedlayoutsegments), which allows you to read the active route segment within that slot.

## [Returns](#returns)

`useSelectedLayoutSegment` returns a string of the active segment or `null` if one doesn't exist.

For example, given the Layouts and URLs below, the returned segment would be:

| Layout | Visited URL | Returned Segment |
| --- | --- | --- |
| `app/layout.js` | `/` | `null` |
| `app/layout.js` | `/dashboard` | `'dashboard'` |
| `app/dashboard/layout.js` | `/dashboard` | `null` |
| `app/dashboard/layout.js` | `/dashboard/settings` | `'settings'` |
| `app/dashboard/layout.js` | `/dashboard/analytics` | `'analytics'` |
| `app/dashboard/layout.js` | `/dashboard/analytics/monthly` | `'analytics'` |

## [Examples](#examples)

### [Creating an active link component](#creating-an-active-link-component)

You can use `useSelectedLayoutSegment` to create an active link component that changes style depending on the active segment. For example, a featured posts list in the sidebar of a blog:

app/blog/blog\-nav\-link.tsxTypeScriptJavaScriptTypeScript\`\`\`
'use client'

import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'

// This \*client\* component will be imported into a blog layout
export default function BlogNavLink({
 slug,
 children,
}: {
 slug: string
 children: React.ReactNode
}) {
 // Navigating to \`/blog/hello\-world\` will return 'hello\-world'
 // for the selected layout segment
 const segment = useSelectedLayoutSegment()
 const isActive = slug === segment

 return (
 \
 {children}
 \
 )
}
\`\`\`

app/blog/layout.tsxTypeScriptJavaScriptTypeScript\`\`\`
// Import the Client Component into a parent Layout (Server Component)
import { BlogNavLink } from './blog\-nav\-link'
import getFeaturedPosts from './get\-featured\-posts'

export default async function Layout({
 children,
}: {
 children: React.ReactNode
}) {
 const featuredPosts = await getFeaturedPosts()
 return (
 \
 {featuredPosts.map((post) =\> (
 \
 \{post.title}\
 \
 ))}
 \{children}\
 \
 )
}
\`\`\`

## [Version History](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `useSelectedLayoutSegment` introduced. |

Was this helpful?



