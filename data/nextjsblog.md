# https://nextjs.org/blog/

## Next.js 15 | Next.js

[Read the full article](https://nextjs.org/blog/next-15)

[Back to Blog](/blog)Monday, October 21st 2024

# Next.js 15

Posted by[Delba de Oliveira@delba\_oliveira](https://twitter.com/delba_oliveira)[Jimmy Lai@feedthejim](https://twitter.com/feedthejim)[Rich Haines@studio\_hungry](https://twitter.com/studio_hungry)Next.js 15 is officially stable and ready for production. This release builds on the updates from both [RC1](/blog/next-15-rc) and [RC2](/blog/next-15-rc2). We've focused heavily on stability while adding some exciting updates we think you'll love. Try Next.js 15 today:

terminal\`\`\`
\# Use the new automated upgrade CLI
npx @next/codemod@canary upgrade latest

\# ...or upgrade manually
npm install next@latest react@rc react\-dom@rc
\`\`\`
We're also excited to share more about what's coming next at [Next.js Conf](/conf) this Thursday, October 24th.

Here's what is new in Next.js 15:

* [**`@next/codemod` CLI:**](#smooth-upgrades-with-nextcodemod-cli) Easily upgrade to the latest Next.js and React versions.
* [**Async Request APIs (Breaking):**](#async-request-apis-breaking-change) Incremental step towards a simplified rendering and caching model.
* [**Caching Semantics (Breaking):**](#caching-semantics) `fetch` requests, `GET` Route Handlers, and client navigations are no longer cached by default.
* [**React 19 Support:**](#react-19) Support for React 19, React Compiler (Experimental), and hydration error improvements.
* [**Turbopack Dev (Stable):**](#turbopack-dev) Performance and stability improvements.
* [**Static Indicator:**](#static-route-indicator) New visual indicator shows static routes during development.
* [**`unstable_after` API (Experimental):**](#executing-code-after-a-response-with-unstable_after-experimental) Execute code after a response finishes streaming.
* [**`instrumentation.js` API (Stable):**](#instrumentationjs-stable) New API for server lifecycle observability.
* [**Enhanced Forms (`next/form`):**](#form-component) Enhance HTML forms with client\-side navigation.
* [**`next.config`:**](#support-for-nextconfigts) TypeScript support for `next.config.ts`.
* [**Self\-hosting Improvements:**](#improvements-for-self-hosting) More control over `Cache-Control` headers.
* [**Server Actions Security:**](#enhanced-security-for-server-actions) Unguessable endpoints and removal of unused actions.
* [**Bundling External Packages (Stable):**](#optimizing-bundling-of-external-packages-stable) New config options for App and Pages Router.
* [**ESLint 9 Support:**](#eslint-9-support) Added support for ESLint 9\.
* [**Development and Build Performance:**](#development-and-build-improvements) Improved build times and Faster Fast Refresh.

## [Smooth upgrades with `@next/codemod` CLI](#smooth-upgrades-with-nextcodemod-cli)

We include codemods (automated code transformations) with every major Next.js release to help automate upgrading breaking changes.

To make upgrades even smoother, we've released an enhanced codemod CLI:

Terminal\`\`\`
npx @next/codemod@canary upgrade latest
\`\`\`
This tool helps you upgrade your codebase to the latest stable or prerelease versions. The CLI will update your dependencies, show available codemods, and guide you through applying them.

The `canary` tag uses the latest version of the codemod while the latest specifies the Next.js version. We recommend using the canary version of the codemod even if you are upgrading to the latest Next.js version, as we plan to continue adding improvements to the tool based on your feedback.

Learn more about [Next.js codemod CLI](/docs/app/building-your-application/upgrading/codemods).

## [Async Request APIs (Breaking Change)](#async-request-apis-breaking-change)

In traditional Server\-Side Rendering, the server waits for a request before rendering any content. However, not all components depend on request\-specific data, so it's unnecessary to wait for the request to render them. Ideally, the server would prepare as much as possible before a request arrives. To enable this, and set the stage for future optimizations, we need to know when to wait for the request.

Therefore, we are transitioning APIs that rely on request\-specific data—such as `headers`, `cookies`, `params`, and `searchParams`—to be **asynchronous**.

\`\`\`
import { cookies } from 'next/headers';

export async function AdminPanel() {
 const cookieStore = await cookies();
 const token = cookieStore.get('token');

 // ...
}
\`\`\`
This is a **breaking change** and affects the following APIs:

* `cookies`
* `headers`
* `draftMode`
* `params` in `layout.js`, `page.js`, `route.js`, `default.js`, `generateMetadata`, and `generateViewport`
* `searchParams` in `page.js`

For an easier migration, these APIs can temporarily be accessed synchronously, but will show warnings in development and production until the next major version. A [codemod](/docs/app/building-your-application/upgrading/codemods) is available to automate the migration:

Terminal\`\`\`
npx @next/codemod@canary next\-async\-request\-api .
\`\`\`
For cases where the codemod can't fully migrate your code, please read the [upgrade guide](/docs/app/building-your-application/upgrading/version-15). We have also provided an [example](https://github.com/leerob/next-saas-starter/pull/62) of how to migrate a Next.js application to the new APIs.

## [Caching Semantics](#caching-semantics)

Next.js App Router launched with opinionated caching defaults. These were designed to provide the most performant option by default with the ability to opt out when required.

Based on your feedback, we re\-evaluated our [caching heuristics](https://x.com/feedthejim/status/1785242054773145636) and how they would interact with projects like Partial Prerendering (PPR) and with third party libraries using `fetch`.

With Next.js 15, we're changing the caching default for `GET` Route Handlers and the Client Router Cache from cached by default to uncached by default. If you want to retain the previous behavior, you can continue to opt\-into caching.

We're continuing to improve caching in Next.js in the coming months and we'll share more details soon.

### [`GET` Route Handlers are no longer cached by default](#get-route-handlers-are-no-longer-cached-by-default)

In Next 14, Route Handlers that used the `GET` HTTP method were cached by default unless they used a dynamic function or dynamic config option. In Next.js 15, `GET` functions are **not cached by default**.

You can still opt into caching using a static route config option such as `export dynamic = 'force-static'`.

Special Route Handlers like [`sitemap.ts`](/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image), and [`icon.tsx`](/docs/app/api-reference/file-conventions/metadata/app-icons), and other [metadata files](/docs/app/api-reference/file-conventions/metadata) remain static by default unless they use dynamic functions or dynamic config options.

### [Client Router Cache no longer caches Page components by default](#client-router-cache-no-longer-caches-page-components-by-default)

In Next.js 14\.2\.0, we introduced an experimental [`staleTimes`](/docs/app/api-reference/next-config-js/staleTimes) flag to allow custom configuration of the [Router Cache](/docs/app/building-your-application/caching#client-side-router-cache).

In Next.js 15, this flag still remains accessible, but we are changing the default behavior to have a `staleTime` of `0` for Page segments. This means that as you navigate around your app, the client will always reflect the latest data from the Page component(s) that become active as part of the navigation. However, there are still important behaviors that remain unchanged:

* Shared layout data won't be refetched from the server to continue to support [partial rendering](/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering).
* Back/forward navigation will still restore from cache to ensure the browser can restore scroll position.
* [`loading.js`](/docs/app/api-reference/file-conventions/loading) will remain cached for 5 minutes (or the value of the `staleTimes.static` configuration).

You can opt into the previous Client Router Cache behavior by setting the following configuration:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 staleTimes: {
 dynamic: 30,
 },
 },
};

export default nextConfig;
\`\`\`
## [React 19](#react-19)

As part of the Next.js 15 release, we've made the decision to align with the upcoming release of React 19\.

In version 15, the App Router uses React 19 RC, and we've also introduced backwards compatibility for React 18 with the Pages Router based on community feedback. If you're using the Pages Router, this allows you to upgrade to React 19 when ready.

Although React 19 is still in the RC phase, our extensive testing across real\-world applications and our close work with the React team have given us confidence in its stability. The core breaking changes have been well\-tested and won't affect existing App Router users. Therefore, we've decided to release Next.js 15 as stable now, so your projects are fully prepared for React 19 GA.

To ensure the transition is as smooth as possible, we've provided [codemods and automated tools](#smooth-upgrades-with-codemod-cli) to help ease the migration process.

Read the [Next.js 15 upgrade guide](/docs/app/building-your-application/upgrading/version-15), the [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide), and watch the [React Conf Keynote](https://www.youtube.com/live/T8TZQ6k4SLE?t=1788) to learn more.

### [Pages Router on React 18](#pages-router-on-react-18)

Next.js 15 maintains backward compatibility for the Pages Router with React 18, allowing users to continue using React 18 while benefiting from improvements in Next.js 15\.

Since the first Release Candidate (RC1\), we've shifted our focus to include support for React 18 based on community feedback. This flexibility enables you to adopt Next.js 15 while using the Pages Router with React 18, giving you greater control over your upgrade path.

> **Note:** While it is possible to run the Pages Router on React 18 and the App Router on React 19 in the same application, we don't recommend this setup. Doing so could result in unpredictable behavior and typings inconsistencies, as the underlying APIs and rendering logic between the two versions may not fully align.

### [React Compiler (Experimental)](#react-compiler-experimental)

The [React Compiler](https://react.dev/learn/react-compiler) is a new experimental compiler created by the React team at Meta. The compiler understands your code at a deep level through its understanding of plain JavaScript semantics and the [Rules of React](https://react.dev/reference/rules), which allows it to add automatic optimizations to your code. The compiler reduces the amount of manual memoization developers have to do through APIs such as `useMemo` and `useCallback` \- making code simpler, easier to maintain, and less error prone.

With Next.js 15, we've added support for the [React Compiler](https://react.dev/learn/react-compiler). Learn more about the React Compiler, and the [available Next.js config options](https://react.dev/learn/react-compiler#usage-with-nextjs).

> **Note:** The React Compiler is currently only available as a Babel plugin, which will result in slower development and build times.

### [Hydration error improvements](#hydration-error-improvements)

Next.js 14\.1 [made improvements](/blog/next-14-1#improved-error-messages-and-fast-refresh) to error messages and hydration errors. Next.js 15 continues to build on those by adding an improved hydration error view. Hydration errors now display the source code of the error with suggestions on how to address the issue.

For example, this was a previous hydration error message in Next.js 14\.1:


Next.js 15 has improved this to:


## [Turbopack Dev](#turbopack-dev)

We are happy to announce that `next dev --turbo` is now **stable and ready** to speed up your development experience. We've been using it to iterate on [vercel.com](https://vercel.com), [nextjs.org](https://nextjs.org), [v0](https://v0.dev), and all of our other applications with great results.

For example, with `vercel.com`, a large Next.js app, we've seen:

* Up to **76\.7% faster** local server startup.
* Up to **96\.3% faster** code updates with Fast Refresh.
* Up to **45\.8% faster** initial route compile without caching (Turbopack does not have disk caching yet).

You can learn more about Turbopack Dev in our new [blog post](/blog/turbopack-for-development-stable).

## [Static Route Indicator](#static-route-indicator)

Next.js now displays a Static Route Indicator during development to help you identify which routes are static or dynamic. This visual cue makes it easier to optimize performance by understanding how your pages are rendered.


You can also use the [next build](/docs/app/api-reference/cli/next#next-build-options) output to view the rendering strategy for all routes.

This update is part of our ongoing efforts to enhance observability in Next.js, making it easier for developers to monitor, debug, and optimize their applications. We're also working on dedicated developer tools, with more details to come soon.

Learn more about the [Static Route Indicator](/docs/app/api-reference/next-config-js/devIndicators#appisrstatus-static-indicator), which can be disabled.

## [Executing code after a response with `unstable_after` (Experimental)](#executing-code-after-a-response-with-unstable_after-experimental)

When processing a user request, the server typically performs tasks directly related to computing the response. However, you may need to perform tasks such as logging, analytics, and other external system synchronization.

Since these tasks are not directly related to the response, the user should not have to wait for them to complete. Deferring the work after responding to the user poses a challenge because serverless functions stop computation immediately after the response is closed.

`after()` is a new experimental API that solves this problem by allowing you to schedule work to be processed after the response has finished streaming, enabling secondary tasks to run without blocking the primary response.

To use it, add `experimental.after` to `next.config.js`:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 after: true,
 },
};

export default nextConfig;
\`\`\`
Then, import the function in Server Components, Server Actions, Route Handlers, or Middleware.

\`\`\`
import { unstable\_after as after } from 'next/server';
import { log } from '@/app/utils';

export default function Layout({ children }) {
 // Secondary task
 after(() =\> {
 log();
 });

 // Primary task
 return \{children}\;
}
\`\`\`
Learn more about [`unstable_after`](/docs/app/api-reference/functions/unstable_after).

## [`instrumentation.js` (Stable)](#instrumentationjs-stable)

The `instrumentation` file, with the `register()` API, allows users to tap into the Next.js server lifecycle to monitor performance, track the source of errors, and deeply integrate with observability libraries like [OpenTelemetry](https://opentelemetry.io/).

This feature is now **stable** and the `experimental.instrumentationHook` config option can be removed.

In addition, we've collaborated with [Sentry](https://sentry.io/) on designing a new `onRequestError` hook that can be used to:

* Capture important context about all errors thrown on the server, including:
	+ Router: Pages Router or App Router
	+ Server context: Server Component, Server Action, Route Handler, or Middleware
* Report the errors to your favorite observability provider.

\`\`\`
export async function onRequestError(err, request, context) {
 await fetch('https://...', {
 method: 'POST',
 body: JSON.stringify({ message: err.message, request, context }),
 headers: { 'Content\-Type': 'application/json' },
 });
}

export async function register() {
 // init your favorite observability provider SDK
}
\`\`\`
Learn more about the `onRequestError` [function](/docs/app/api-reference/file-conventions/instrumentation#onrequesterror-optional).

## [`` Component](#form-component)

The new `` component extends the HTML `` element with [prefetching](/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching), [client\-side navigation](/docs/app/building-your-application/routing/linking-and-navigating#5-soft-navigation), and progressive enhancement.

It is useful for forms that navigate to a new page, such as a search form that leads to a results page.

app/page.jsx\`\`\`
import Form from 'next/form';

export default function Page() {
 return (
 \
 \
 \Submit\
 \
 );
}
\`\`\`
The `` component comes with:

* **Prefetching**: When the form is in view, the [layout](/docs/app/api-reference/file-conventions/layout) and [loading](/docs/app/api-reference/file-conventions/loading) UI are prefetched, making navigation fast.
* **Client\-side Navigation:** On submission, shared layouts and client\-side state are preserved.
* **Progressive Enhancement**: If JavaScript hasn't loaded yet, the form still works via full\-page navigation.

Previously, achieving these features required a lot of manual boilerplate. For example:

Example\`\`\`
// Note: This is abbreviated for demonstration purposes.
// Not recommended for use in production code.

'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

export default function Form(props) {
 const action = props.action
 const router = useRouter()

 useEffect(() =\> {
 // if form target is a URL, prefetch it
 if (typeof action === 'string') {
 router.prefetch(action)
 }
 }, \[action, router])

 function onSubmit(event) {
 event.preventDefault()

 // grab all of the form fields and trigger a \`router.push\` with the data URL encoded
 const formData = new FormData(event.currentTarget)
 const data = new URLSearchParams()

 for (const \[name, value] of formData) {
 data.append(name, value as string)
 }

 router.push(\`${action}?${data.toString()}\`)
 }

 if (typeof action === 'string') {
 return \
 }

 return \
}
\`\`\`
Learn more about the [`` Component](/docs/app/api-reference/components/form).

## [Support for `next.config.ts`](#support-for-nextconfigts)

Next.js now supports the TypeScript `next.config.ts` file type and provides a `NextConfig` type for autocomplete and type\-safe options:

next.config.ts\`\`\`
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
 /\* config options here \*/
};

export default nextConfig;
\`\`\`
Learn more about [TypeScript support](/docs/app/building-your-application/configuring/typescript#type-checking-nextconfigts) in Next.js.

## [Improvements for self\-hosting](#improvements-for-self-hosting)

When self\-hosting applications, you may need more control over `Cache-Control` directives.

One common case is controlling the `stale-while-revalidate` period sent for ISR pages. We've implemented two improvements:

1. You can now configure the [`expireTime`](/docs/app/api-reference/next-config-js/expireTime) value in `next.config`. This was previously the `experimental.swrDelta` option.
2. Updated the default value to one year, ensuring most CDNs can fully apply the `stale-while-revalidate` semantics as intended.

We also no longer override custom `Cache-Control` values with our default values, allowing full control and ensuring compatibility with any CDN setup.

Finally, we've improved image optimization when self\-hosting. Previously, we recommended you install `sharp` for optimizing images on your Next.js server. This recommendation was sometimes missed. With Next.js 15, you no longer need to manually install `sharp` — Next.js will use `sharp` automatically when using `next start` or running with [standalone output mode](/docs/app/api-reference/next-config-js/output).

To learn more, see our new [demo and tutorial video](https://x.com/leeerob/status/1843796169173995544) on self\-hosting Next.js.

## [Enhanced Security for Server Actions](#enhanced-security-for-server-actions)

[Server Actions](https://react.dev/reference/rsc/server-actions) are server\-side functions that can be called from the client. They are defined by adding the `'use server'` directive at the top of a file and exporting an async function.

Even if a Server Action or utility function is not imported elsewhere in your code, it's still a publicly accessible HTTP endpoint. While this behavior is technically correct, it can lead to unintentional exposure of such functions.

To improve security, we've introduced the following enhancements:

* **Dead code elimination:** Unused Server Actions won't have their IDs exposed to the client\-side JavaScript bundle, reducing bundle size and improving performance.
* **Secure action IDs:** Next.js now creates unguessable, non\-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.

\`\`\`
// app/actions.js
'use server';

// This action \*\*is\*\* used in our application, so Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
export async function updateUserAction(formData) {}

// This action \*\*is not\*\* used in our application, so Next.js
// will automatically remove this code during \`next build\`
// and will not create a public endpoint.
export async function deleteUserAction(formData) {}
\`\`\`
You should still treat Server Actions as public HTTP endpoints. Learn more about [securing Server Actions](/blog/security-nextjs-server-components-actions#write).

## [Optimizing bundling of external packages (Stable)](#optimizing-bundling-of-external-packages-stable)

Bundling external packages can improve the cold start performance of your application. In the **App Router**, external packages are bundled by default, and you can opt\-out specific packages using the new [`serverExternalPackages`](/docs/app/api-reference/next-config-js/serverExternalPackages) config option.

In the **Pages Router**, external packages are not bundled by default, but you can provide a list of packages to bundle using the existing [`transpilePackages`](/docs/pages/api-reference/next-config-js/transpilePackages) option. With this configuration option, you need to specify each package.

To unify configuration between App and Pages Router, we're introducing a new option, [`bundlePagesRouterDependencies`](/docs/pages/api-reference/next-config-js/bundlePagesRouterDependencies) to match the default automatic bundling of the App Router. You can then use [`serverExternalPackages`](/docs/app/api-reference/next-config-js/serverExternalPackages) to opt\-out specific packages, if needed.

next.config.ts\`\`\`
const nextConfig = {
 // Automatically bundle external packages in the Pages Router:
 bundlePagesRouterDependencies: true,
 // Opt specific packages out of bundling for both App and Pages Router:
 serverExternalPackages: \['package\-name'],
};

export default nextConfig;
\`\`\`
Learn more about [optimizing external packages](/docs/app/building-your-application/optimizing/package-bundling).

## [ESLint 9 Support](#eslint-9-support)

Next.js 15 also introduces support for [ESLint 9](https://eslint.org/blog/2024/04/eslint-v9.0.0-released), following the end\-of\-life for ESLint 8 on October 5, 2024\.

To ensure a smooth transition, Next.js remain backwards compatible, meaning you can continue using either ESLint 8 or 9\.

If you upgrade to ESLint 9, and we detect that you haven't yet adopted [the new config format](https://eslint.org/blog/2024/04/eslint-v9.0.0-released/#flat-config-is-now-the-default-and-has-some-changes), Next.js will automatically apply the `ESLINT_USE_FLAT_CONFIG=false` escape hatch to ease migration.

Additionally, deprecated options like `—ext` and `—ignore-path` will be removed when running `next lint`. Please note that ESLint will eventually disallow these older configurations in ESLint 10, so we recommend starting your migration soon.

For more details on these changes, check out the [migration guide](https://eslint.org/docs/latest/use/migrate-to-9.0.0).

As part of this update, we've also upgraded `eslint-plugin-react-hooks` to `v5.0.0`, which introduces new rules for React Hooks usage. You can review all changes in the [changelog for eslint\-plugin\-react\-hooks@5\.0\.0](https://github.com/facebook/react/releases/tag/eslint-plugin-react-hooks%405.0.0).

## [Development and Build Improvements](#development-and-build-improvements)

### [Server Components HMR](#server-components-hmr)

During development, Server components are re\-executed when saved. This means, any `fetch` requests to your API endpoints or third\-party services are also called.

To improve local development performance and reduce potential costs for billed API calls, we now ensure Hot Module Replacement (HMR) can re\-use `fetch` responses from previous renders.

Learn more about the [Server Components HMR Cache](/docs/app/api-reference/next-config-js/serverComponentsHmrCache).

### [Faster Static Generation for the App Router](#faster-static-generation-for-the-app-router)

We've optimized static generation to improve build times, especially for pages with slow network requests.

Previously, our static optimization process rendered pages twice—once to generate data for client\-side navigation and a second time to render the HTML for the initial page visit. Now, we reuse the first render, cutting out the second pass, reducing workload and build times.

Additionally, static generation workers now share the `fetch` cache across pages. If a `fetch` call doesn't opt out of caching, its results are reused by other pages handled by the same worker. This reduces the number of requests for the same data.

### [Advanced Static Generation Control (Experimental)](#advanced-static-generation-control-experimental)

We've added experimental support for more control over the static generation process for advanced use cases that would benefit from greater control.

We recommend sticking to the current defaults unless you have specific requirements as these options can lead to increased resource usage and potential out\-of\-memory errors due to increased concurrency.

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 // how many times Next.js will retry failed page generation attempts
 // before failing the build
 staticGenerationRetryCount: 1
 // how many pages will be processed per worker
 staticGenerationMaxConcurrency: 8
 // the minimum number of pages before spinning up a new export worker
 staticGenerationMinPagesPerWorker: 25
 },
}

export default nextConfig;
\`\`\`
Learn more about the [Static Generation options](/docs/app/api-reference/next-config-js/staticGeneration).

## [Other Changes](#other-changes)

* **\[Breaking]** next/image: Removed `squoosh` in favor of `sharp` as an optional dependency ([PR](https://github.com/vercel/next.js/pull/63321))
* **\[Breaking]** next/image: Changed default `Content-Disposition` to `attachment` ([PR](https://github.com/vercel/next.js/pull/65631))
* **\[Breaking]** next/image: Error when `src` has leading or trailing spaces ([PR](https://github.com/vercel/next.js/pull/65637))
* **\[Breaking]** Middleware: Apply `react-server` condition to limit unrecommended React API imports ([PR](https://github.com/vercel/next.js/pull/65424))
* **\[Breaking]** next/font: Removed support for external `@next/font` package ([PR](https://github.com/vercel/next.js/pull/65601))
* **\[Breaking]** next/font: Removed `font-family` hashing ([PR](https://github.com/vercel/next.js/pull/53608))
* **\[Breaking]** Caching: `force-dynamic` will now set a `no-store` default to the fetch cache ([PR](https://github.com/vercel/next.js/pull/64145))
* **\[Breaking]** Config: Enable `swcMinify` ([PR](https://github.com/vercel/next.js/pull/65579)), `missingSuspenseWithCSRBailout` ([PR](https://github.com/vercel/next.js/pull/65688)), and `outputFileTracing` ([PR](https://github.com/vercel/next.js/pull/65579)) behavior by default and remove deprecated options
* **\[Breaking]** Remove auto\-instrumentation for Speed Insights (must now use the dedicated [@vercel/speed\-insights](https://www.npmjs.com/package/@vercel/speed-insights) package) ([PR](https://github.com/vercel/next.js/pull/64199))
* **\[Breaking]** Remove `.xml` extension for dynamic sitemap routes and align sitemap URLs between development and production ([PR](https://github.com/vercel/next.js/pull/65507))
* **\[Breaking]** We've deprecated exporting `export const runtime = "experimental-edge"` in the App Router. Users should now switch to `export const runtime = "edge"`. We've added a [codemod](/docs/app/building-your-application/upgrading/codemods#app-dir-runtime-config-experimental-edge) to perform this ([PR](https://github.com/vercel/next.js/pull/70480))
* **\[Breaking]** Calling `revalidateTag` and `revalidatePath` during render will now throw an error ([PR](https://github.com/vercel/next.js/pull/71093))
* **\[Breaking]** The `instrumentation.js` and `middleware.js` files will now use the vendored React packages ([PR](https://github.com/vercel/next.js/pull/69619))
* **\[Breaking]** The minimum required Node.js version has been updated to 18\.18\.0 ([PR](https://github.com/vercel/next.js/pull/67274))
* **\[Breaking]** `next/dynamic`: the deprecated `suspense` prop has been removed and when the component is used in the App Router, it won't insert an empty Suspense boundary anymore ([PR](https://github.com/vercel/next.js/pull/67014))
* **\[Breaking]** When resolving modules on the Edge Runtime, the `worker` module condition will not be applied ([PR](https://github.com/vercel/next.js/pull/66808))
* **\[Breaking]** Disallow using `ssr: false` option with `next/dynamic` in Server Components ([PR](https://github.com/vercel/next.js/pull/70378))
* **\[Improvement]** Metadata: Updated environment variable fallbacks for `metadataBase` when hosted on Vercel ([PR](https://github.com/vercel/next.js/pull/65089))
* **\[Improvement]** Fix tree\-shaking with mixed namespace and named imports from `optimizePackageImports` ([PR](https://github.com/vercel/next.js/pull/64894))
* **\[Improvement]** Parallel Routes: Provide unmatched catch\-all routes with all known params ([PR](https://github.com/vercel/next.js/pull/65063))
* **\[Improvement]** Config `bundlePagesExternals` is now stable and renamed to `bundlePagesRouterDependencies`
* **\[Improvement]** Config `serverComponentsExternalPackages` is now stable and renamed to `serverExternalPackages`
* **\[Improvement]** create\-next\-app: New projects ignore all `.env` files by default ([PR](https://github.com/vercel/next.js/pull/61920))
* **\[Improvement]** The `outputFileTracingRoot`, `outputFileTracingIncludes` and `outputFileTracingExcludes` have been upgraded from experimental and are now stable ([PR](https://github.com/vercel/next.js/pull/68464))
* **\[Improvement]** Avoid merging global CSS files with CSS module files deeper in the tree ([PR](https://github.com/vercel/next.js/pull/67373))
* **\[Improvement]** The cache handler can be specified via the `NEXT_CACHE_HANDLER_PATH` environment variable ([PR](https://github.com/vercel/next.js/pull/70537/))
* **\[Improvement]** The Pages Router now supports both React 18 and React 19 ([PR](https://github.com/vercel/next.js/pull/69484))
* **\[Improvement]** The Error Overlay now displays a button to copy the Node.js Inspector URL if the inspector is enabled ([PR](https://github.com/vercel/next.js/pull/69357))
* **\[Improvement]** Client prefetches on the App Router now use the `priority` attribute ([PR](https://github.com/vercel/next.js/pull/67356))
* **\[Improvement]** Next.js now provides an `unstable_rethrow` function to rethrow Next.js internal errors in the App Router ([PR](https://github.com/vercel/next.js/pull/65831))
* **\[Improvement]** `unstable_after` can now be used in static pages ([PR](https://github.com/vercel/next.js/pull/71231))
* **\[Improvement]** If a `next/dynamic` component is used during SSR, the chunk will be prefetched ([PR](https://github.com/vercel/next.js/pull/65486))
* **\[Improvement]** The `esmExternals` option is now supported on the App Router ([PR](https://github.com/vercel/next.js/pull/65041))
* **\[Improvement]** The `experimental.allowDevelopmentBuild` option can be used to allow `NODE_ENV=development` with `next build` for debugging purposes ([PR](https://github.com/vercel/next.js/pull/65463))
* **\[Improvement]** The Server Action transforms are now disabled in the Pages Router ([PR](https://github.com/vercel/next.js/pull/71028))
* **\[Improvement]** Build workers will now stop the build from hanging when they exit ([PR](https://github.com/vercel/next.js/pull/70997))
* **\[Improvement]** When redirecting from a Server Action, revalidations will now apply correctly ([PR](https://github.com/vercel/next.js/pull/70715))
* **\[Improvement]** Dynamic params are now handled correctly for parallel routes on the Edge Runtime ([PR](https://github.com/vercel/next.js/pull/70667))
* **\[Improvement]** Static pages will now respect staleTime after initial load ([PR](https://github.com/vercel/next.js/pull/70640))
* **\[Improvement]** `vercel/og` updated with a memory leak fix ([PR](https://github.com/vercel/next.js/pull/70214))
* **\[Improvement]** Patch timings updated to allow usage of packages like `msw` for APIs mocking ([PR](https://github.com/vercel/next.js/pull/68193))
* **\[Improvement]** Prerendered pages should use static staleTime ([PR](https://github.com/vercel/next.js/pull/67868))

To learn more, check out the [upgrade guide](/docs/app/building-your-application/upgrading/version-15).

## [Contributors](#contributors)

Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel.
This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Hendrik](https://github.com/unstubbable), [Janka](https://github.com/lubieowoce), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [Jiwon](https://github.com/devjiwonchoi), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Sam](https://github.com/samcx), [Sebastian](https://github.com/sebmarkbage), [Sebbie](https://github.com/eps1lon), [Shu](https://github.com/shuding), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Alex](https://github.com/arlyon), [Benjamin](https://github.com/bgw), [Donny](https://github.com/kdy1), [Maia](https://github.com/padmaia), [Niklas](https://github.com/mischnic), [Tim](https://github.com/timneutkens), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* The **Next.js Docs** team: [Delba](https://github.com/delbaoliveira), [Rich](https://github.com/molebox), [Ismael](https://github.com/ismaelrumzan), and [Lee](https://github.com/leerob).

Huge thanks to @AbhiShake1, @Aerilym, @AhmedBaset, @AnaTofuZ, @Arindam200, @Arinji2, @ArnaudFavier, @ArnoldVanN, @Auxdible, @B33fb0n3, @Bhavya031, @Bjornnyborg, @BunsDev, @CannonLock, @CrutchTheClutch, @DeepakBalaraman, @DerTimonius, @Develliot, @EffectDoplera, @Ehren12, @Ethan\-Arrowood, @FluxCapacitor2, @ForsakenHarmony, @Francoscopic, @Gomah, @GyoHeon, @Hemanshu\-Upadhyay, @HristovCodes, @HughHzyb, @IAmKushagraSharma, @IDNK2203, @IGassmann, @ImDR, @IncognitoTGT, @Jaaneek, @JamBalaya56562, @Jeffrey\-Zutt, @JohnGemstone, @JoshuaKGoldberg, @Julian\-Louis, @Juneezee, @KagamiChan, @Kahitar, @KeisukeNagakawa, @KentoMoriwaki, @Kikobeats, @KonkenBonken, @Kuboczoch, @Lada496, @LichuAcu, @LorisSigrist, @Lsnsh, @Luk\-z, @Luluno01, @M\-YasirGhaffar, @Maaz\-Ahmed007, @Manoj\-M\-S, @ManuLpz4, @Marukome0743, @MaxLeiter, @MehfoozurRehman, @MildTomato, @MonstraG, @N2D4, @NavidNourani, @Nayeem\-XTREME, @Netail, @NilsJacobsen, @Ocheretovich, @OlyaPolya, @PapatMayuri, @PaulAsjes, @PlagueFPS, @ProchaLu, @Pyr33x, @QiuranHu, @RiskyMH, @Sam\-Phillemon9493, @Sayakie, @Shruthireddy04, @SouthLink, @Strift, @SukkaW, @Teddir, @Tim\-Zj, @TrevorSayre, @Unsleeping, @Willem\-Jaap, @a89529294, @abdull\-haseeb, @abhi12299, @acdlite, @actopas, @adcichowski, @adiguno, @agadzik, @ah100101, @akazwz, @aktoriukas, @aldosch, @alessiomaffeis, @allanchau, @alpedia0, @amannn, @amikofalvy, @anatoliik\-lyft, @anay\-208, @andrii\-bodnar, @anku255, @ankur\-dwivedi, @aralroca, @archanaagivale30, @arlyon, @atik\-persei, @avdeev, @baeharam, @balazsorban44, @bangseongbeom, @begalinsaf, @bennettdams, @bewinsnw, @bgw, @blvdmitry, @bobaaaaa, @boris\-szl, @bosconian\-dynamics, @brekk, @brianshano, @cfrank, @chandanpasunoori, @chentsulin, @chogyejin, @chrisjstott, @christian\-bromann, @codeSTACKr, @coderfin, @coltonehrman, @controversial, @coopbri, @creativoma, @crebelskydico, @crutchcorn, @darthmaim, @datner, @davidsa03, @delbaoliveira, @devjiwonchoi, @devnyxie, @dhruv\-kaushik, @dineshh\-m, @diogocapela, @dnhn, @domdomegg, @domin\-mnd, @dvoytenko, @ebCrypto, @ekremkenter, @emmerich, @flybayer, @floriangosse, @forsakenharmony, @francoscopic, @frys, @gabrielrolfsen, @gaojude, @gdborton, @greatvivek11, @gnoff, @guisehn, @GyoHeon, @hamirmahal, @hiro0218, @hirotomoyamada, @housseindjirdeh, @hungdoansy, @huozhi, @hwangstar156, @iampoul, @ianmacartney, @icyJoseph, @ijjk, @imddc, @imranolas, @iscekic, @jantimon, @jaredhan418, @jeanmax1me, @jericopulvera, @jjm2317, @jlbovenzo, @joelhooks, @joeshub, @jonathan\-ingram, @jonluca, @jontewks, @joostmeijles, @jophy\-ye, @jordienr, @jordyfontoura, @kahlstrm, @karlhorky, @karlkeefer, @kartheesan05, @kdy1, @kenji\-webdev, @kevva, @khawajaJunaid, @kidonng, @kiner\-tang, @kippmr, @kjac, @kjugi, @kshehadeh, @kutsan, @kwonoj, @kxlow, @leerob, @lforst, @li\-jia\-nan, @liby, @lonr, @lorensr, @lovell, @lubieowoce, @luciancah, @luismiramirez, @lukahartwig, @lumirlumir, @luojiyin1987, @mamuso, @manovotny, @marlier, @mauroaccornero, @maxhaomh, @mayank1513, @mcnaveen, @md\-rejoyan\-islam, @mehmetozguldev, @mert\-duzgun, @mirasayon, @mischnic, @mknichel, @mobeigi, @molebox, @mratlamwala, @mud\-ali, @n\-ii\-ma, @n1ckoates, @nattui, @nauvalazhar, @neila\-a, @neoFinch, @niketchandivade, @nisabmohd, @none23, @notomo, @notrab, @nsams, @nurullah, @okoyecharles, @omahs, @paarthmadan, @pathliving, @pavelglac, @penicillin0, @phryneas, @pkiv, @pnutmath, @qqww08, @r34son, @raeyoung\-kim, @remcohaszing, @remorses, @rezamauliadi, @rishabhpoddar, @ronanru, @royalfig, @rubyisrust, @ryan\-nauman, @ryohidaka, @ryota\-murakami, @s\-ekai, @saltcod, @samcx, @samijaber, @sean\-rallycry, @sebmarkbage, @shubh73, @shuding, @sirTangale, @sleevezip, @slimbde, @soedirgo, @sokra, @sommeeeer, @sopranopillow, @souporserious, @srkirkland, @steadily\-worked, @steveluscher, @stipsan, @styfle, @stylessh, @syi0808, @symant233, @tariknh, @theoludwig, @timfish, @timfuhrmann, @timneutkens, @tknickman, @todor0v, @tokkiyaa, @torresgol10, @tranvanhieu01012002, @txxxxc, @typeofweb, @unflxw, @unstubbable, @versecafe, @vicb, @vkryachko, @wbinnssmith, @webtinax, @weicheng95, @wesbos, @whatisagi, @wiesson, @woutvanderploeg, @wyattjoh, @xiaohanyu, @xixixao, @xugetsu, @yosefbeder, @ypessoa, @ytori, @yunsii, @yurivangeffen, @z0n, @zce, @zhawtof, @zsh77, and @ztanner for helping!



## Next.js 15 RC 2 | Next.js

[Read the full article](https://nextjs.org/blog/next-15-rc2)

[Back to Blog](/blog)Tuesday, October 15th 2024

# Next.js 15 RC 2

Posted by[Delba de Oliveira@delba\_oliveira](https://twitter.com/delba_oliveira)[Jiachi Liu@huozhi](https://twitter.com/huozhi)[Jiwon Choi@devjiwonchoi](https://twitter.com/devjiwonchoi)[Josh Story@joshcstory](https://twitter.com/joshcstory)[Sebastian Silbermann@sebsilbermann](https://twitter.com/sebsilbermann)[Zack Tanner@zt1072](https://twitter.com/zt1072)Following the announcement of the first Next.js 15 Release Candidate [back in May,](https://nextjs.org/blog/next-15-rc) we’ve been preparing a second Release Candidate based on your feedback. Here’s what we’ve been working on:

* [**`@next/codemod upgrade`**](#smooth-upgrades-with-codemod-cli): Easily upgrade to the latest Next.js and React versions.
* [**Turbopack for development**](#turbopack-for-development): Performance improvements and Next.js 15 stability target.
* [**Async Request APIs (Breaking)**](#async-request-apis-breaking-change): Incremental step towards a simplified rendering and caching model.
* [**Server Actions**](#enhanced-security-for-server-actions): Enhanced security with unguessable endpoints and removal of unused actions.
* [**Static Indicator**](#static-route-indicator): New visual indicator shows static routes during development.
* [**`next/form`**](#form-component): Enhance HTML forms with client\-side navigation.
* [**`next.config.ts`**](#support-for-nextconfigts): TypeScript support for the Next.js configuration file.
* [**`instrumentation.js` (Stable)**](#instrumentationjs-stable): New API for server lifecycle observability.
* [**Development and Build improvements**](#development-and-build-improvements): Improved build times and Faster Fast Refresh.
* [**Self\-hosting**](#improvements-for-self-hosting): More control over `Cache-Control` headers.
* [**Linting**](#eslint-9-support): Added support for ESLint 9\.

Try the Next.js 15 Release Candidate (RC2\) today:

\`\`\`
\# Use the new automated upgrade CLI
npx @next/codemod@canary upgrade rc

\# ...or upgrade manually
npm install next@rc react@rc react\-dom@rc
\`\`\`

> **Note:** This Release Candidate includes all changes from the [previous RC](/blog/next-15-rc).

## [Smooth upgrades with codemod CLI](#smooth-upgrades-with-codemod-cli)

We include codemods (automated code transformations) with every major Next.js release to help automate upgrading breaking changes.

To make upgrades even smoother, we've released an enhanced codemod CLI:

\`\`\`
npx @next/codemod@canary upgrade rc
\`\`\`
This tool helps you upgrade your codebase to the latest stable or prerelease versions. The CLI will update your dependencies, show available codemods, and guide you through applying them. The specified dist tag on the command line (`@rc`, `@canary`, etc.) determines the version to upgrade to.

Learn more about [Next.js codemods](/docs/canary/app/building-your-application/upgrading/codemods).

## [Turbopack for Development](#turbopack-for-development)

Turbopack for local development will become stable in the general release of Next.js 15, while remaining opt\-in. You can try it today by running:

\`\`\`
next dev \-\-turbo
\`\`\`
Thanks to the thousands of developers who participated in testing, reporting issues, and verifying fixes throughout the Turbopack beta and release candidate phases, we've resolved [54 GitHub issues](https://github.com/vercel/next.js/issues?q=is:issue+is:closed+label:Turbopack+created:%3E%3D2024-05-23+) since the first Next.js 15 Release Candidate. Alongside this community effort, our internal testing on [vercel.com](http://vercel.com/), [v0\.dev](http://v0.dev), and [nextjs.org](http://nextjs.org/) helped identify numerous additional improvements.

In the last three months, we've focused on optimizing cold compilation performance. Compared to the previous release, we've seen:

* **25–35% reduction** in memory usage.
* **30–50% faster** compilation for large pages with thousands of modules.

We will continue to optimize these areas in future releases.

Looking ahead, the Turbopack team is making significant progress on persistent caching, memory usage reduction, and Turbopack for `next build`—with [96% of tests passing](https://areweturboyet.com/build).

> **Note:** See all of the [supported and unsupported features](/docs/architecture/turbopack#unsupported-features) of Turbopack.

## [Async Request APIs (Breaking Change)](#async-request-apis-breaking-change)

In traditional Server\-Side Rendering, the server waits for a request before rendering any content. However, not all components depend on request\-specific data, so it's unnecessary to wait for the request to render them. Ideally, the server would prepare as much as possible before a request arrives. To enable this, and set the stage for future optimizations, we need to know when to wait for the request.

Therefore, we are transitioning APIs that rely on request\-specific data—such as `headers`, `cookies`, `params`, and `searchParams`—to be **asynchronous**.

\`\`\`
import { cookies } from 'next/headers';

export async function AdminPanel() {
 const cookieStore = await cookies();
 const token = cookieStore.get('token');

 // ...
}
\`\`\`
This is a **breaking change** and affects the following APIs:

* `cookies`
* `headers`
* `draftMode`
* `params` in `layout.js`, `page.js`, `route.js`, `default.js`, `generateMetadata`, and `generateViewport`
* `searchParams` in `page.js`

For an easier migration, these APIs can temporarily be accessed synchronously, but will show warnings in development and production until the next major version. A [codemod](/docs/canary/app/building-your-application/upgrading/codemods) is available to automate the migration:

\`\`\`
npx @next/codemod@canary next\-async\-request\-api .
\`\`\`
For cases where the codemod can't fully migrate your code, please read the [upgrade guide](/docs/canary/app/building-your-application/upgrading/version-15). We have also provided an [example](https://github.com/leerob/next-saas-starter/pull/62) of how to migrate a Next.js application to the new APIs.

## [Enhanced Security for Server Actions](#enhanced-security-for-server-actions)

[Server Actions](https://react.dev/reference/rsc/server-actions) are server\-side functions that can be called from the client. They are defined by adding the `'use server'` directive at the top of a file and exporting an async function.

Even if a Server Action or utility function is not imported elsewhere in your code, it’s still a publicly accessible HTTP endpoint. While this behavior is technically correct, it can lead to unintentional exposure of such functions.

To improve security, we’ve introduced the following enhancements:

* **Dead code elimination:** Unused Server Actions won’t have their IDs exposed to the client\-side JavaScript bundle, reducing bundle size and improving performance.
* **Secure action IDs:** Next.js now creates unguessable, non\-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.

\`\`\`
// app/actions.js
'use server';

// This action \*\*is\*\* used in our application, so Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
export async function updateUserAction(formData) {}

// This action \*\*is not\*\* used in our application, so Next.js
// will automatically remove this code during \`next build\`
// and will not create a public endpoint.
export async function deleteUserAction(formData) {}
\`\`\`
You should still treat Server Actions as public HTTP endpoints. Learn more about [securing Server Actions](https://nextjs.org/blog/security-nextjs-server-components-actions#write).

## [Static Route Indicator](#static-route-indicator)

Next.js now displays a Static Route Indicator during development to help you identify which routes are static or dynamic. This visual cue makes it easier to optimize performance by understanding how your pages are rendered.


You can also use the [next build](/docs/app/api-reference/cli/next#next-build-options) output to view the rendering strategy for all routes.

This update is part of our ongoing efforts to enhance observability in Next.js, making it easier for developers to monitor, debug, and optimize their applications. We're also working on dedicated developer tools, with more details to come soon.

Learn more about the [Static Route Indicator](/docs/canary/app/api-reference/next-config-js/devIndicators#appisrstatus-static-indicator), which can be disabled.

## [`` Component](#form-component)

The new `` component extends the HTML `` element with [prefetching](/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching), [client\-side navigation](/docs/app/building-your-application/routing/linking-and-navigating#5-soft-navigation), and progressive enhancement.

It is useful for forms that navigate to a new page, such as a search form that leads to a results page.

\`\`\`
import Form from 'next/form';

export default function Page() {
 return (
 \
 \
 \Submit\
 \
 );
}
\`\`\`
The `` component comes with:

* **Prefetching**: When the form is in view, the [layout](/docs/app/api-reference/file-conventions/layout) and [loading](/docs/app/api-reference/file-conventions/loading) UI are prefetched, making navigation fast.
* **Client\-side Navigation:** On submission, shared layouts and client\-side state are preserved.
* **Progressive Enhancement**: If JavaScript hasn’t loaded yet, the form still works via full\-page navigation.

Previously, achieving these features required a lot of manual boilerplate. For example:

Example\`\`\`
// Note: This is abbreviated for demonstration purposes.
// Not recommended for use in production code.

'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

export default function Form(props) {
 const action = props.action
 const router = useRouter()

 useEffect(() =\> {
 // if form target is a URL, prefetch it
 if (typeof action === 'string') {
 router.prefetch(action)
 }
 }, \[action, router])

 function onSubmit(event) {
 event.preventDefault()

 // grab all of the form fields and trigger a \`router.push\` with the data URL encoded
 const formData = new FormData(event.currentTarget)
 const data = new URLSearchParams()

 for (const \[name, value] of formData) {
 data.append(name, value as string)
 }

 router.push(\`${action}?${data.toString()}\`)
 }

 if (typeof action === 'string') {
 return \
 }

 return \
}
\`\`\`
Learn more about the [`` Component](/docs/canary/app/api-reference/components/form).

## [Support for `next.config.ts`](#support-for-nextconfigts)

Next.js now supports the TypeScript `next.config.ts` file type and provides a `NextConfig` type for autocomplete and type\-safe options:

\`\`\`
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
 /\* config options here \*/
};

export default nextConfig;
\`\`\`
Learn more about [TypeScript support](/docs/canary/app/building-your-application/configuring/typescript#type-checking-nextconfigts) in Next.js.

## [`instrumentation.js` (Stable)](#instrumentationjs-stable)

The `instrumentation` file, with the `register()` API, allows users to tap into the Next.js server lifecycle to monitor performance, track the source of errors, and deeply integrate with observability libraries like [OpenTelemetry](https://opentelemetry.io/).

This feature is now **stable** and the `experimental.instrumentationHook` config option can be removed.

In addition, we’ve collaborated with [Sentry](https://sentry.io/) on designing a new `onRequestError` hook that can be used to:

* Capture important context about all errors thrown on the server, including:
	+ Router: Pages Router or App Router
	+ Server context: Server Component, Server Action, Route Handler, or Middleware
* Report the errors to your favorite observability provider.

\`\`\`
export async function onRequestError(err, request, context) {
 await fetch('https://...', {
 method: 'POST',
 body: JSON.stringify({ message: err.message, request, context }),
 headers: { 'Content\-Type': 'application/json' },
 });
}

export async function register() {
 // init your favorite observability provider SDK
}
\`\`\`
Learn more about the `onRequestError` [function](/docs/canary/app/api-reference/file-conventions/instrumentation#onrequesterror-optional).

## [Development and Build Improvements](#development-and-build-improvements)

### [Server Components HMR](#server-components-hmr)

During development, Server components are re\-executed when saved. This means, any `fetch` requests to your API endpoints or third\-party services are also called.

To improve local development performance and reduce potential costs for billed API calls, we now ensure Hot Module Replacement (HMR) can re\-use `fetch` responses from previous renders.

Learn more about the [Server Components HMR Cache](/docs/canary/app/api-reference/next-config-js/serverComponentsHmrCache).

### [Faster Static Generation for the App Router](#faster-static-generation-for-the-app-router)

We've optimized static generation to improve build times, especially for pages with slow network requests.

Previously, our static optimization process rendered pages twice—once to generate data for client\-side navigation and a second time to render the HTML for the initial page visit. Now, we reuse the first render, cutting out the second pass, reducing workload and build times.

Additionally, static generation workers now share the `fetch` cache across pages. If a `fetch` call doesn’t opt out of caching, its results are reused by other pages handled by the same worker. This reduces the number of requests for the same data.

### [Advanced Static Generation Control (Experimental)](#advanced-static-generation-control-experimental)

We’ve added experimental support for more control over static generation process for advanced use cases that would benefit from greater control.

We recommend sticking to the current defaults unless you have specific requirements as these options can lead to increased resource usage and potential out\-of\-memory errors due to increased concurrency.

\`\`\`
const nextConfig = {
 experimental: {
 // how many times Next.js will retry failed page generation attempts
 // before failing the build
 staticGenerationRetryCount: 1
 // how many pages will be processed per worker
 staticGenerationMaxConcurrency: 8
 // the minimum number of pages before spinning up a new export worker
 staticGenerationMinPagesPerWorker: 25
 },
}

export default nextConfig;
\`\`\`
Learn more about the [Static Generation options](/docs/canary/app/api-reference/next-config-js/staticGeneration).

## [Improvements for self\-hosting](#improvements-for-self-hosting)

When self\-hosting applications, you may need more control over `Cache-Control` directives.

One common case is controlling the `stale-while-revalidate` period sent for ISR pages. We've implemented two improvements:

1. You can now configure the [`expireTime`](/docs/canary/app/api-reference/next-config-js/expireTime) value in `next.config`. This was previously the `experimental.swrDelta` option.
2. Updated the default value to one year, ensuring most CDNs can fully apply the `stale-while-revalidate` semantics as intended.

We also no longer override custom `Cache-Control` values with our default values, allowing full control and ensuring compatibility with any CDN setup.

Finally, we've improved image optimization when self\-hosting. Previously, we recommended you install `sharp` for optimizing images on your Next.js server. This recommendation was sometimes missed. With Next.js 15, you no longer need to manually install `sharp` — Next.js will use `sharp` automatically when using `next start` or running with [standalone output mode](/docs/app/api-reference/next-config-js/output).

To learn more, see our new [demo and tutorial video](https://x.com/leeerob/status/1843796169173995544) on self\-hosting Next.js.

## [ESLint 9 Support](#eslint-9-support)

Next.js 15 also introduces support for [ESLint 9](https://eslint.org/blog/2024/04/eslint-v9.0.0-released), following the end\-of\-life for ESLint 8 on October 5, 2024\.

To ensure a smooth transition, Next.js remain backwards compatible, meaning you can continue using either ESLint 8 or 9\.

If you upgrade to ESLint 9, and we detect that you haven’t yet adopted [the new config format](https://eslint.org/blog/2024/04/eslint-v9.0.0-released/#flat-config-is-now-the-default-and-has-some-changes), Next.js will automatically apply the `ESLINT_USE_FLAT_CONFIG=false` escape hatch to ease migration.

Additionally, deprecated options like `—ext` and `—ignore-path` will be removed when running `next lint`. Please note that ESLint will eventually disallow these older configurations in ESLint 10, so we recommend starting your migration soon.

For more details on these changes, check out the [migration guide](https://eslint.org/docs/latest/use/migrate-to-9.0.0).

As part of this update, we’ve also upgraded `eslint-plugin-react-hooks` to `v5.0.0`, which introduces new rules for React Hooks usage. You can review all changes in the [changelog for eslint\-plugin\-react\-hooks@5\.0\.0](https://github.com/facebook/react/releases/tag/eslint-plugin-react-hooks%405.0.0).

## [Other Changes](#other-changes)

* All of the changes previously described in the RC 1 [blog post](/blog/next-15-rc)
* **\[Breaking]** We’ve deprecated exporting `export const runtime = "experimental-edge"` in the App Router. Users should now switch to `export const runtime = "edge"`. We’ve added a [codemod](/docs/canary/app/building-your-application/upgrading/codemods#app-dir-runtime-config-experimental-edge) to perform this ([PR](https://github.com/vercel/next.js/pull/70480))
* **\[Breaking]** Calling `revalidateTag` and `revalidatePath` during render will now throw an error ([PR](https://github.com/vercel/next.js/pull/71093))
* **\[Breaking]** The `instrumentation.js` and `middleware.js` files will now use the vendored React packages ([PR](https://github.com/vercel/next.js/pull/69619))
* **\[Breaking]** The minimum required Node.js version has been updated to 18\.18\.0 ([PR](https://github.com/vercel/next.js/pull/67274))
* **\[Breaking]** `next/dynamic`: the deprecated `suspense` prop has been removed and when the component is used in the App Router, it won't insert an empty Suspense boundary anymore ([PR](https://github.com/vercel/next.js/pull/67014))
* **\[Breaking]** When resolving modules on the Edge Runtime, the `worker` module condition will not be applied ([PR](https://github.com/vercel/next.js/pull/66808))
* **\[Breaking]** Disallow using `ssr: false` option with `next/dynamic` in Server Components ([PR](https://github.com/vercel/next.js/pull/70378))
* **\[Improvement]** The `outputFileTracingRoot`, `outputFileTracingIncludes` and `outputFileTracingExcludes` have been upgraded from experimental and are now stable ([PR](https://github.com/vercel/next.js/pull/68464))
* **\[Improvement]** Avoid merging global CSS files with CSS module files deeper in the tree ([PR](https://github.com/vercel/next.js/pull/67373))
* **\[Improvement]** The cache handler can be specified via the `NEXT_CACHE_HANDLER_PATH` environment variable ([PR](https://github.com/vercel/next.js/pull/70537/))
* **\[Improvement]** The Pages Router now supports both React 18 and React 19 ([PR](https://github.com/vercel/next.js/pull/69484))
* **\[Improvement]** The Error Overlay now displays a button to copy the Node.js Inspector URL if the inspector is enabled ([PR](https://github.com/vercel/next.js/pull/69357))
* **\[Improvement]** Client prefetches on the App Router now use the `priority` attribute ([PR](https://github.com/vercel/next.js/pull/67356))
* **\[Improvement]** Next.js now provides an `unstable_rethrow` function to rethrow Next.js internal errors in the App Router ([PR](https://github.com/vercel/next.js/pull/65831))
* **\[Improvement]** `unstable_after` can now be used in static pages ([PR](https://github.com/vercel/next.js/pull/71231))
* **\[Improvement]** If a `next/dynamic` component is used during SSR, the chunk will be prefetched ([PR](https://github.com/vercel/next.js/pull/65486))
* **\[Improvement]** The `esmExternals` option is now supported on the App Router ([PR](https://github.com/vercel/next.js/pull/65041))
* **\[Improvement]** The `experimental.allowDevelopmentBuild` option can be used to allow `NODE_ENV=development` with `next build` for debugging purposes ([PR](https://github.com/vercel/next.js/pull/65463))
* **\[Improvement]** The Server Action transforms are now disabled in the Pages Router ([PR](https://github.com/vercel/next.js/pull/71028))
* **\[Improvement]** Build workers will now stop the build from hanging when they exit ([PR](https://github.com/vercel/next.js/pull/70997))
* **\[Improvement]** When redirecting from a Server Action, revalidations will now apply correctly ([PR](https://github.com/vercel/next.js/pull/70715))
* **\[Improvement]** Dynamic params are now handled correctly for parallel routes on the Edge Runtime ([PR](https://github.com/vercel/next.js/pull/70667))
* **\[Improvement]** Static pages will now respect staleTime after initial load ([PR](https://github.com/vercel/next.js/pull/70640))
* **\[Improvement]** `vercel/og` updated with a memory leak fix ([PR](https://github.com/vercel/next.js/pull/70214))
* **\[Improvement]** Patch timings updated to allow usage of packages like `msw` for APIs mocking ([PR](https://github.com/vercel/next.js/pull/68193))

## [Contributors](#contributors)

Next.js is the result of the combined work of over 3,000 individual developers, and our core team at Vercel.
This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Hendrik](https://github.com/unstubbable), [Janka](https://github.com/lubieowoce), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [Jiwon](https://github.com/devjiwonchoi), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Sam](https://github.com/samcx), [Sebastian](https://github.com/sebmarkbage), [Sebbie](https://github.com/eps1lon), [Shu](https://github.com/shuding), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Alex](https://github.com/arlyon), [Benjamin](https://github.com/bgw), [Donny](https://github.com/kdy1), [Maia](https://github.com/padmaia), [Niklas](https://github.com/mischnic), [Tim](https://github.com/timneutkens), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* The **Next.js Docs**  team: [Delba](https://github.com/delbaoliveira), [Rich](https://github.com/molebox), [Ismael](https://github.com/ismaelrumzan), and [Lee](https://github.com/leerob).

Huge thanks to @huozhi, @shuding, @wyattjoh, @PaulAsjes, @mcnaveen, @timneutkens, @stipsan, @aktoriukas, @sirTangale, @greatvivek11, @sokra, @anatoliik\-lyft, @wbinnssmith, @coltonehrman, @hungdoansy, @kxlow, @ztanner, @manovotny, @leerob, @ryota\-murakami, @ijjk, @pnutmath, @feugy, @Jeffrey\-Zutt, @wiesson, @eps1lon, @devjiwonchoi, @Ethan\-Arrowood, @kenji\-webdev, @domdomegg, @samcx, @Jaaneek, @evanwinter, @kdy1, @balazsorban44, @feedthejim, @ForsakenHarmony, @kwonoj, @delbaoliveira, @xiaohanyu, @dvoytenko, @bobaaaaa, @bgw, @gaspar09, @souporserious, @unflxw, @kiner\-tang, @Ehren12, @EffectDoplera, @IAmKushagraSharma, @Auxdible, @sean\-rallycry, @jeanmax1me, @unstubbable, @NilsJacobsen, @adiguno, @ryan\-nauman, @zsh77, @KagamiChan, @steveluscher, @MehfoozurRehman, @vkryachko, @chentsulin, @samijaber, @begalinsaf, @FluxCapacitor2, @lukahartwig, @brianshano, @pavelglac, @styfle, @symant233, @HristovCodes, @karlhorky, @jonluca, @jonathan\-ingram, @mknichel, @sopranopillow, @Gomah, @imddc, @notrab, @gabrielrolfsen, @remorses, @AbhiShake1, @agadzik, @rishabhpoddar, @rezamauliadi, @IncognitoTGT, @webtinax, @BunsDev, @nisabmohd, @z0n, @bennettdams, @joeshub, @n1ckoates, @srkirkland, @RiskyMH, @coopbri, @okoyecharles, @diogocapela, @dnhn, @typeofweb, @davidsa03, @imranolas, @lubieowoce, @maxhaomh, @mirasayon, @blvdmitry, @hwangstar156, @lforst, @emmerich, @christian\-bromann, @Lsnsh, @datner, @hiro0218, @flybayer, @ianmacartney, @ypessoa, @ryohidaka, @icyJoseph, @Arinji2, @lovell, @nsams, @Nayeem\-XTREME, @JamBalaya56562, @Arindam200, @gaojude, @qqww08, @todor0v, @tokkiyaa, @arlyon, @lorensr, @Juneezee, @Sayakie, @IGassmann, @bosconian\-dynamics, @phryneas, @akazwz, @atik\-persei, @shubh73, @alpedia0, @chogyejin, @notomo, @ArnoldVanN, @dhruv\-kaushik, @kevva, @Kahitar, @anay\-208, @boris\-szl, @devnyxie, @LorisSigrist, @M\-YasirGhaffar, @Lada496, @kippmr, @torresgol10, @pkiv, @Netail, @jontewks, @ArnaudFavier, @chrisjstott, @mratlamwala, @mayank1513, @karlkeefer, @kshehadeh, @Marukome0743, @a89529294, @anku255, @KeisukeNagakawa, @andrii\-bodnar, @aldosch, @versecafe, @steadily\-worked, @cfrank, @QiuranHu, @farsabbutt, @joostmeijles, @saltcod, @archanaagivale30, @crutchcorn, @crebelskydico, @Maaz\-Ahmed007, @jophy\-ye, @remcohaszing, @JoshuaKGoldberg, @creativoma, @GyoHeon, @SukkaW, @MaxLeiter, @neila\-a, @stylessh, @Teddir, @ManuLpz4, @Julian\-Louis, @syi0808, @mert\-duzgun, @amannn, @MonstraG, @hamirmahal, @tariknh, @Kikobeats, @LichuAcu, @Kuboczoch, @himself65, @Sam\-Phillemon9493, @Shruthireddy04, @Hemanshu\-Upadhyay, @timfuhrmann, @controversial, @pathliving, @mischnic, @mauroaccornero, @NavidNourani, @allanchau, @ekremkenter, @yurivangeffen, @gnoff, @darthmaim, @gdborton, @Willem\-Jaap, @KentoMoriwaki, @TrevorSayre, @marlier, @Luluno01, @xixixao, @domin\-mnd, @niketchandivade, @N2D4, @kjugi, @luciancah, @mud\-ali, @codeSTACKr, @luojiyin1987, @mehmetozguldev, @ronanru, @tknickman, @joelhooks, @khawajaJunaid, @rubyisrust, @abdull\-haseeb, @bewinsnw, @housseindjirdeh, @li\-jia\-nan, @aralroca, @s\-ekai, @ah100101, @jantimon, @jordienr, @iscekic, @Strift, @slimbde, @nauvalazhar, @HughHzyb, @guisehn, @wesbos, @OlyaPolya, @paarthmadan, @AhmedBaset, @dineshh\-m, @avdeev, @Bhavya031, @MildTomato, @Bjornnyborg, @amikofalvy, @yosefbeder, @kjac, @woutvanderploeg, @Ocheretovich, @ProchaLu, @luismiramirez, @omahs, @theoludwig, @abhi12299, @sommeeeer, @lumirlumir, @royalfig, @iampoul, @molebox, @txxxxc, @zce, @mamuso, @kahlstrm, @vercel\-release\-bot, @zhawtof, @PapatMayuri, @PlagueFPS, @IDNK2203, @jericopulvera, @liby, @CannonLock, @timfish, @whatisagi, @none23, @haouvw, @Pyr33x, @SouthLink, @frydj, @CrutchTheClutch, @sleevezip, @r34son, @yunsii, @md\-rejoyan\-islam, @kartheesan05, @nattui, @KonkenBonken, @weicheng95, @brekk, @Francoscopic, @B33fb0n3, @ImDR, @nurullah, @hdodov, @ebCrypto, @soedirgo, @floriangosse, @Tim\-Zj, @raeyoung\-kim, @erwannbst, @DerTimonius, @hirotomoyamada, @Develliot, @chandanpasunoori, @vicb, @ankur\-dwivedi, @kidonng, @baeharam, @AnaTofuZ, @coderfin, @xugetsu, @alessiomaffeis, @kutsan, @jordyfontoura, @sebmarkbage, @tranvanhieu01012002, @jlbovenzo, @Luk\-z, @jaredhan418, @bangseongbeom, @penicillin0, @neoFinch, @DeepakBalaraman, @Manoj\-M\-S, @Unsleeping, @lonr, @Aerilym, @ytori, @acdlite, @actopas, @n\-ii\-ma, @adcichowski, @mobeigi, @JohnGemstone, and @jjm2317 for helping!



## Next.js 15 RC | Next.js

[Read the full article](https://nextjs.org/blog/next-15-rc)

[Back to Blog](/blog)Thursday, May 23rd 2024

# Next.js 15 RC

Posted by[Delba de Oliveira@delba\_oliveira](https://twitter.com/delba_oliveira)[Zack Tanner@zt1072](https://twitter.com/zt1072)The Next.js 15 Release Candidate (RC) is now available. This early version allows you to test the latest features before the upcoming stable release.

* [**React:**](#react-19-rc) Support for the React 19 RC, React Compiler (Experimental), and hydration error improvements
* [**Caching:**](#caching-updates) `fetch` requests, `GET` Route Handlers, and client navigations are no longer cached by default
* [**Partial Prerendering (Experimental):**](#incremental-adoption-of-partial-prerendering-experimental) New Layout and Page config option for incremental adoption
* [**`next/after` (Experimental):**](#executing-code-after-a-response-with-nextafter-experimental) New API to execute code after a response has finished streaming
* [**`create-next-app`:**](#create-next-app-updates) Updated design and a new flag to enable Turbopack in local development
* [**Bundling external packages (Stable):**](#optimizing-bundling-of-external-packages-stable) New config options for App and Pages Router

Try the Next.js 15 RC today:

Terminal\`\`\`
npm install next@rc react@rc react\-dom@rc
\`\`\`
## [React 19 RC](#react-19-rc)

The Next.js App Router is built on the React [canary channel](https://react.dev/blog/2023/05/03/react-canaries) for frameworks, which has allowed developers to use and provide feedback on these new React APIs before the v19 release.

Next.js 15 RC now supports React 19 RC, which includes new features for both the client and server like Actions.

Read the [Next.js 15 upgrade guide](https://nextjs.org/docs/app/building-your-application/upgrading/version-15), the [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide), and watch the [React Conf Keynote](https://www.youtube.com/live/T8TZQ6k4SLE?t=1788) to learn more.

> **Note:** Some third party libraries may not be compatible with React 19 yet.

## [React Compiler (Experimental)](#react-compiler-experimental)

The [React Compiler](https://react.dev/learn/react-compiler) is a new experimental compiler created by the React team at Meta. The compiler understands your code at a deep level through its understanding of plain JavaScript semantics and the [Rules of React](https://react.dev/reference/rules), which allows it to add automatic optimizations to your code. The compiler reduces the amount of manual memoization developers have to do through APIs such as `useMemo` and `useCallback` \- making code simpler, easier to maintain, and less error prone.

With Next.js 15, we've added support for the [React Compiler](https://react.dev/learn/react-compiler).

Install `babel-plugin-react-compiler`:

Terminal\`\`\`
npm install babel\-plugin\-react\-compiler
\`\`\`
Then, add `experimental.reactCompiler` option in `next.config.js`:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 reactCompiler: true,
 },
};

module.exports = nextConfig;
\`\`\`
Optionally, you can configure the compiler to run in "opt\-in" mode as follows:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 reactCompiler: {
 compilationMode: 'annotation',
 },
 },
};

module.exports = nextConfig;
\`\`\`

> **Note:** The React Compiler is currently only possible to use in Next.js through a Babel plugin, which could result in slower build times.

Learn more about the [React Compiler](https://react.dev/learn/react-compiler), and the [available Next.js config options](https://react.dev/learn/react-compiler#usage-with-nextjs).

### [Hydration error improvements](#hydration-error-improvements)

Next.js 14\.1 [made improvements](/blog/next-14-1#improved-error-messages-and-fast-refresh) to error messages and hydration errors. Next.js 15 continues to build on those by adding an improved hydration error view. Hydration errors now display the source code of the error with suggestions on how to address the issue.

For example, this was a previous hydration error message in Next.js 14\.1:


Next.js 15 RC has improved this to:


## [Caching updates](#caching-updates)

Next.js App Router launched with opinionated caching defaults. These were designed to provide the most performant option by default with the ability to opt out when required.

Based on your feedback, we re\-evaluated our [caching heuristics](https://x.com/feedthejim/status/1785242054773145636) and how they would interact with projects like Partial Prerendering (PPR) and with third party libraries using `fetch`.

With Next.js 15, we’re changing the caching default for `fetch` requests, `GET` Route Handlers, and Client Router Cache from cached by default to uncached by default. If you want to retain the previous behavior, you can continue to opt\-into caching.

We're continuing to improve caching in Next.js in the coming months and we'll share more details in the Next.js 15 GA announcement.

### [`fetch` Requests are no longer cached by default](#fetch-requests-are-no-longer-cached-by-default)

Next.js uses the [Web `fetch` API](https://developer.mozilla.org/docs/Web/API/Fetch_API) cache option to configure how a server\-side fetch request interacts with the framework's persistent HTTP cache:

\`\`\`
fetch('https://...', { cache: 'force\-cache' \| 'no\-store' });
\`\`\`
* `no-store` \- fetch a resource from a remote server on every request and do not update the cache
* `force-cache` \- fetch a resource from the cache (if it exists) or a remote server and update the cache

In Next.js 14, `force-cache` was used by default if a `cache` option was not provided, unless a dynamic function or dynamic config option was used.

In Next.js 15, `no-store` is used by default if a `cache` option is not provided. This means **fetch requests will not be cached by default**.

You can still opt into caching `fetch` requests by:

* Setting the [`cache` option](https://nextjs.org/docs/app/api-reference/functions/fetch#optionscache) to `force-cache` in a single `fetch` call
* Setting the [`dynamic` route config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) to `'force-static'` for a single route
* Setting the [`fetchCache` route config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#fetchcache) to `'default-cache'` to override all `fetch` requests in a Layout or Page to use `force-cache` unless they explicitly specify their own `cache` option

### [`GET` Route Handlers are no longer cached by default](#get-route-handlers-are-no-longer-cached-by-default)

In Next 14, Route Handlers that used the `GET` HTTP method were cached by default unless they used a dynamic function or dynamic config option. In Next.js 15, `GET` functions are **not cached by default**.

You can still opt into caching using a static route config option such as `export dynamic = 'force-static'`.

Special Route Handlers like [`sitemap.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), and [`icon.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons), and other [metadata files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata) remain static by default unless they use dynamic functions or dynamic config options.

### [Client Router Cache no longer caches Page components by default](#client-router-cache-no-longer-caches-page-components-by-default)

In Next.js 14\.2\.0, we introduced an experimental [`staleTimes`](https://nextjs.org/docs/app/api-reference/next-config-js/staleTimes) flag to allow custom configuration of the [Router Cache](https://nextjs.org/docs/app/building-your-application/caching#client-side-router-cache).

In Next.js 15, this flag still remains accessible, but we are changing the default behavior to have a `staleTime` of `0` for Page segments. This means that as you navigate around your app, the client will always reflect the latest data from the Page component(s) that become active as part of the navigation. However, there are still important behaviors that remain unchanged:

* Shared layout data won't be refetched from the server to continue to support [partial rendering](https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating#4-partial-rendering).
* Back/forward navigation will still restore from cache to ensure the browser can restore scroll position.
* [Loading.js](https://nextjs.org/docs/app/api-reference/file-conventions/loading) will remain cached for 5 minutes (or the value of the `staleTimes.static` configuration).

You can opt into the previous Client Router Cache behavior by setting the following configuration:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 staleTimes: {
 dynamic: 30,
 },
 },
};

module.exports = nextConfig;
\`\`\`
## [Incremental adoption of Partial Prerendering (Experimental)](#incremental-adoption-of-partial-prerendering-experimental)

In Next.js 14, we [introduced Partial Prerendering (PPR)](/blog/next-14#partial-prerendering-preview) \- an optimization that combines [static and dynamic rendering](https://nextjs.org/docs/app/building-your-application/rendering/server-components#server-rendering-strategies) on the same page.

Next.js currently defaults to static rendering unless you use [dynamic functions](https://nextjs.org/docs/app/building-your-application/routing/route-handlers#dynamic-functions) such as `cookies()`, `headers()`, and uncached data requests. These APIs opt an entire route into dynamic rendering. With PPR, you can wrap any dynamic UI in a Suspense boundary. When a new request comes in, Next.js will immediately serve a static HTML shell, then render and stream the dynamic parts in the same HTTP request.

To allow for incremental adoption, we’ve added an `experimental_ppr` route config option for opting specific Layouts and Pages into PPR:

app/page.jsx\`\`\`
import { Suspense } from "react"
import { StaticComponent, DynamicComponent } from "@/app/ui"

export const experimental\_ppr = true

export default function Page() {
 return {
 \
 \
 \
 \
 \
 \
 };
}
\`\`\`
To use the new option, you’ll need to set the `experimental.ppr` config in your `next.config.js` file to `'incremental'`:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 ppr: 'incremental',
 },
};

module.exports = nextConfig;
\`\`\`
Once all the segments have PPR enabled, it’ll be considered safe for you to set the `ppr` value to `true`, and enable it for the entire app and all future routes.

We will share more about our PPR roadmap in our Next.js 15 GA blog post.

Learn more about [Partial Prerendering](https://nextjs.org/docs/app/building-your-application/rendering/partial-prerendering).

## [Executing code after a response with `next/after` (Experimental)](#executing-code-after-a-response-with-nextafter-experimental)

When processing a user request, the server typically performs tasks directly related to computing the response. However, you may need to perform tasks such as logging, analytics, and other external system synchronization.

Since these tasks are not directly related to the response, the user should not have to wait for them to complete. Deferring the work after responding to the user poses a challenge because serverless functions stop computation immediately after the response is closed.

`after()` is a new experimental API that solves this problem by allowing you to schedule work to be processed after the response has finished streaming, enabling secondary tasks to run without blocking the primary response.

To use it, add `experimental.after` to `next.config.js`:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 after: true,
 },
};

module.exports = nextConfig;
\`\`\`
Then, import the function in Server Components, Server Actions, Route Handlers, or Middleware.

\`\`\`
import { unstable\_after as after } from 'next/server';
import { log } from '@/app/utils';

export default function Layout({ children }) {
 // Secondary task
 after(() =\> {
 log();
 });

 // Primary task
 return \{children}\;
}
\`\`\`
Learn more about [`next/after`](https://nextjs.org/docs/app/api-reference/functions/unstable_after).

## [`create-next-app` updates](#create-next-app-updates)

For Next.js 15, we've updated `create-next-app` with a new design.


When running `create-next-app`, there is a new prompt asking if you want to enable Turbopack for local development (defaults to `No`).

Terminal\`\`\`
✔ Would you like to use Turbopack for next dev? … No / Yes
\`\`\`
The `--turbo` flag can be used to enable Turbopack.

Terminal\`\`\`
npx create\-next\-app@rc \-\-turbo
\`\`\`
To make getting started on a new project even easier, a new `--empty` flag has been added to the CLI. This will remove any extraneous files and styles, resulting in a minimal "hello world" page.

Terminal\`\`\`
npx create\-next\-app@rc \-\-empty
\`\`\`
## [Optimizing bundling of external packages (Stable)](#optimizing-bundling-of-external-packages-stable)

Bundling external packages can improve the cold start performance of your application. In the **App Router**, external packages are bundled by default, and you can opt\-out specific packages using the new [`serverExternalPackages`](https://nextjs.org/docs/app/api-reference/next-config-js/serverExternalPackages) config option.

In the **Pages Router**, external packages are not bundled by default, but you can provide a list of packages to bundle using the existing [`transpilePackages`](https://nextjs.org/docs/pages/api-reference/next-config-js/transpilePackages) option. With this configuration option, you need to specify each package.

To unify configuration between App and Pages Router, we’re introducing a new option, [`bundlePagesRouterDependencies`](https://nextjs.org/docs/pages/api-reference/next-config-js/bundlePagesRouterDependencies) to match the default automatic bundling of the App Router. You can then use [`serverExternalPackages`](https://nextjs.org/docs/app/api-reference/next-config-js/serverExternalPackages) to opt\-out specific packages, if needed.

next.config.ts\`\`\`
const nextConfig = {
 // Automatically bundle external packages in the Pages Router:
 bundlePagesRouterDependencies: true,
 // Opt specific packages out of bundling for both App and Pages Router:
 serverExternalPackages: \['package\-name'],
};

module.exports = nextConfig;
\`\`\`
Learn more about [optimizing external packages](https://nextjs.org/docs/app/building-your-application/optimizing/package-bundling).

## [Other Changes](#other-changes)

* **\[Breaking]** Minimum React version is now 19 RC
* **\[Breaking]** next/image: Removed `squoosh` in favor of `sharp` as an optional dependency ([PR](https://github.com/vercel/next.js/pull/63321))
* **\[Breaking]** next/image: Changed default `Content-Disposition` to `attachment` ([PR](https://github.com/vercel/next.js/pull/65631))
* **\[Breaking]** next/image: Error when `src` has leading or trailing spaces ([PR](https://github.com/vercel/next.js/pull/65637))
* **\[Breaking]** Middleware: Apply `react-server` condition to limit unrecommended react API imports ([PR](https://github.com/vercel/next.js/pull/65424))
* **\[Breaking]** next/font: Removed support for external `@next/font` package ([PR](https://github.com/vercel/next.js/pull/65601))
* **\[Breaking]** next/font: Removed `font-family` hashing ([PR](https://github.com/vercel/next.js/pull/53608))
* **\[Breaking]** Caching: `force-dynamic` will now set a `no-store` default to the fetch cache ([PR](https://github.com/vercel/next.js/pull/64145))
* **\[Breaking]** Config: Enable `swcMinify` ([PR](https://github.com/vercel/next.js/pull/65579)), `missingSuspenseWithCSRBailout` ([PR](https://github.com/vercel/next.js/pull/65688)), and `outputFileTracing` ([PR](https://github.com/vercel/next.js/pull/65579)) behavior by default and remove deprecated options
* **\[Breaking]** Remove auto\-instrumentation for Speed Insights (must now use the dedicated [@vercel/speed\-insights](https://www.npmjs.com/package/@vercel/speed-insights) package) ([PR](https://github.com/vercel/next.js/pull/64199))
* **\[Breaking]** Remove `.xml` extension for dynamic sitemap routes and align sitemap URLs between development and production ([PR](https://github.com/vercel/next.js/pull/65507))
* **\[Improvement]** Metadata: Updated environmental variable fallbacks for `metadataBase` when hosted on Vercel ([PR](https://github.com/vercel/next.js/pull/65089))
* **\[Improvement]** Fix tree\-shaking with mixed namespace and named imports from `optimizePackageImports` ([PR](https://github.com/vercel/next.js/pull/64894))
* **\[Improvement]** Parallel Routes: Provide unmatched catch\-all routes with all known params ([PR](https://github.com/vercel/next.js/pull/65063))
* **\[Improvement]** Config `bundlePagesExternals` is now stable and renamed to `bundlePagesRouterDependencies`
* **\[Improvement]** Config `serverComponentsExternalPackages` is now stable and renamed to `serverExternalPackages`
* **\[Improvement]** create\-next\-app: New projects ignore all `.env` files by default ([PR](https://github.com/vercel/next.js/pull/61920))
* **\[Docs]** Improve auth documentation ([PR](https://github.com/vercel/next.js/pull/63140))
* **\[Docs]** `@next/env` package ([PR](https://github.com/vercel/next.js/pull/64908))

To learn more, check out the [upgrade guide](https://nextjs.org/docs/app/building-your-application/upgrading/version-15).

## [Contributors](#contributors)

Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel.
This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Balazs](https://github.com/balazsorban44), [Ethan](https://github.com/Ethan-Arrowood), [Janka](https://github.com/lubieowoce), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Sam](https://github.com/samcx), [Sebastian](https://github.com/sebmarkbage), [Sebbie](https://github.com/eps1lon), [Shu](https://github.com/shuding), [Steven](https://github.com/styfle), [Tim](https://github.com/timneutkens), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Alex](https://github.com/arlyon), [Benjamin](https://github.com/bgw), [Donny](https://github.com/kdy1), [Leah](https://github.com/forsakenharmony), [Maia](https://github.com/padmaia), [OJ](https://github.com/kwonoj), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* **Next.js Docs**: [Delba](https://github.com/delbaoliveira), [Steph](https://github.com/StephDietz), [Michael](https://github.com/manovotny), [Anthony](https://github.com/anthonyshew), and [Lee](https://github.com/leerob).

Huge thanks to @devjiwonchoi, @ijjk, @Ethan\-Arrowood, @sokra, @kenji\-webdev, @wbinnssmith, @huozhi, @domdomegg, @samcx, @Jaaneek, @evanwinter, @wyattjoh, @kdy1, @balazsorban44, @feedthejim, @ztanner, @ForsakenHarmony, @kwonoj, @delbaoliveira, @stipsan, @leerob, @shuding, @xiaohanyu, @timneutkens, @dvoytenko, @bobaaaaa, @bgw, @gaspar09, @souporserious, @unflxw, @kiner\-tang, @Ehren12, @EffectDoplera, @IAmKushagraSharma, @Auxdible, @sean\-rallycry, @Jeffrey\-Zutt, @eps1lon, @jeanmax1me, @unstubbable, @NilsJacobsen, @PaulAsjes, @adiguno, @ryan\-nauman, @zsh77, @KagamiChan, @steveluscher, @MehfoozurRehman, @vkryachko, @chentsulin, @samijaber, @begalinsaf, @FluxCapacitor2, @lukahartwig, @brianshano, @pavelglac, @styfle, @symant233, @HristovCodes, @karlhorky, @jonluca, @jonathan\-ingram, @mknichel, @sopranopillow, @Gomah, @imddc, @notrab, @gabrielrolfsen, @remorses, @AbhiShake1, @agadzik, @ryota\-murakami, @rishabhpoddar, @rezamauliadi, @IncognitoTGT, @webtinax, @BunsDev, @nisabmohd, @z0n, @bennettdams, @joeshub, @n1ckoates, @srkirkland, @RiskyMH, @coopbri, @okoyecharles, @diogocapela, @dnhn, @typeofweb, @davidsa03, @imranolas, @lubieowoce, @maxhaomh, @mirasayon, @blvdmitry, @hwangstar156, @lforst, @emmerich, @christian\-bromann, @Lsnsh, @datner, @hiro0218, @flybayer, @ianmacartney, @ypessoa, @ryohidaka, @icyJoseph, @Arinji2, @lovell, @nsams, @Nayeem\-XTREME, @JamBalaya56562, @Arindam200, @gaojude, @qqww08, @todor0v, @coltonehrman, and @wiesson for helping!



## Next.js 15.1 | Next.js

[Read the full article](https://nextjs.org/blog/next-15-1)

[Back to Blog](/blog)Tuesday, December 10th 2024

# Next.js 15\.1

Posted by[Janka Uryga@lubieowoce](https://twitter.com/lubieowoce)[Jiachi Liu@huozhi](https://twitter.com/huozhi)[Sebastian Silbermann@sebsilbermann](https://twitter.com/sebsilbermann)Next.js 15\.1 brings core upgrades, new APIs, and improvements to the developer experience. Key updates include:

* [**React 19 (stable)**](/blog/next-15-1#react-19-stable): Support for React 19 is officially available in both Pages Router \& App Router.
* [**Improved Error Debugging**](/blog/next-15-1#improved-error-debugging): Enhanced DX and better source maps for the browser and the terminal.
* [**`after` (stable)**](/blog/next-15-1#after-stable): New API to execute code after a response has finished streaming.
* [**`forbidden` / `unauthorized` (experimental)**](/blog/next-15-1#forbidden-and-unauthorized-experimental): New APIs to enable more granular authentication error handling.

Upgrade today, or get started with:

Terminal\`\`\`
\# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest

\# ...or upgrade manually
npm install next@latest react@latest react\-dom@latest

\# ...or start a new project
npx create\-next\-app@latest
\`\`\`
## [React 19 (stable)](#react-19-stable)

Next.js 15\.1 now fully supports React 19:

* **For the Pages Router**: you can now use React 19 stable without needing the Release Candidate or Canary releases, alongside continued support for React 18\.
* **For the App Router**: we will continue to provide React Canary releases built\-in. These include all the stable React 19 changes, as well as newer features being validated in frameworks, prior to a new React release.

Since the Next.js 15 release, a significant addition to React 19 was “[sibling pre\-warming](https://react.dev/blog/2024/04/25/react-19-upgrade-guide#improvements-to-suspense)”.

For a comprehensive overview of React 19’s updates, please refer to [the official React 19 blog post](https://react.dev/blog/2024/12/05/react-19).

## [Improved Error Debugging](#improved-error-debugging)

We’ve made improvements to error debugging in Next.js, ensuring you can quickly locate the source of issues, whether they appear in the terminal, browser, or attached debuggers. These enhancements apply to both Webpack and Turbopack ([now stable with Next.js 15](/blog/turbopack-for-development-stable)).

### [Source Maps Enhancements](#source-maps-enhancements)

Errors are now easier to trace back to their origin through the improved use of source maps. We’ve implemented the [`ignoreList` property of source maps](https://developer.chrome.com/docs/devtools/x-google-ignore-list), which allows Next.js to hide stack frames for external dependencies, making your application code the primary focus.

For slightly more accurate source mapping of method names, we suggest adopting Turbopack (now stable), which has improved handling and detection of source maps over Webpack.

> **For library authors**: We recommend populating the `ignoreList` property in sourcemaps when publishing your libraries, especially if they are configured as external (e.g. in the `serverExternalPackages` config).

### [Collapsed Stack Frames](#collapsed-stack-frames)

We’ve improved the logic for collapsing stack frames to highlight the most relevant parts of your code.

* **In the browser and error overlay**: Stack frames from third\-party dependencies are hidden by default, focusing on your application code. You can reveal the hidden frames by clicking “Show ignored frames” in the devtools or the overlay.
* **In the terminal**: Third\-party dependency frames are also collapsed by default, and error formatting now aligns with the browser output for a consistent debugging experience. Errors are replayed in the browser to ensure you don’t miss important information during development if you need the entire stack trace.

### [Enhanced Profiling](#enhanced-profiling)

Ignored stack frames are also recognized by built\-in browser profilers. This makes profiling your application easier, allowing you to pinpoint slow functions in your code without noise from external libraries.

### [Improved with the Edge Runtime](#improved-with-the-edge-runtime)

When using the Edge runtime, errors are now displayed consistently across development environments, ensuring seamless debugging. Previously, logged errors would only include the message and not the stack.

### [Before and after](#before-and-after)

Terminal **Before**:

Terminal\`\`\`
 ⨯ app/page.tsx (6:11\) @ eval
 ⨯ Error: boom
 at eval (./app/page.tsx:12:15\)
 at Page (./app/page.tsx:11:74\)
 at AsyncLocalStorage.run (node:async\_hooks:346:14\)
 at stringify (\)
 at AsyncLocalStorage.run (node:async\_hooks:346:14\)
 at AsyncResource.runInAsyncScope (node:async\_hooks:206:9\)
digest: "380744807"
 4 \| export default function Page() {
 5 \| const throwError = myCallback(() =\> {
\> 6 \| throw new Error('boom')
 \| ^
 7 \| }, \[])
 8 \|
 9 \| throwError()
 GET / 500 in 2354ms
\`\`\`
Terminal **After**:

Terminal\`\`\`
 ⨯ Error: boom
 at eval (app/page.tsx:6:10\)
 at Page (app/page.tsx:5:32\)
 4 \| export default function Page() {
 5 \| const throwError = myCallback(() =\> {
\> 6 \| throw new Error('boom')
 \| ^
 7 \| }, \[])
 8 \|
 9 \| throwError() {
 digest: '225828171'
}
\`\`\`
Error Overlay **Before**



An example of the Next.js error overlay before version 15\.1

Error Overlay **After**



An example of the Next.js error overlay after version 15\.1

These improvements make errors clearer and more intuitive, allowing you to focus your time building your application rather than debugging.

We’re also thrilled to announce the introduction of a redesigned UI for the error overlay, coming in upcoming releases.

## [`after` (stable)](#after-stable)

The `after()` API is now stable following its introduction in the first Next.js 15 RC.

`after()` provides a way to perform tasks such as logging, analytics, and other system synchronization after the response has finished streaming to the user, without blocking the primary response.

### [Key changes](#key-changes)

Since its introduction, we’ve stabilized `after()` and addressed feedback including:

* **Improved support** for self\-hosted Next.js servers.
* **Bug fixes** for scenarios where `after()` interacted with other Next.js features.
* **Enhanced extensibility**, enabling other platforms to inject their own `waitUntil()` primitives to power `after()`.
* **Support for runtime APIs** such as `cookies()` and `headers()` in Server Actions and Route Handlers.

app/layout.js\`\`\`
import { after } from 'next/server';
import { log } from '@/app/utils';

export default function Layout({ children }) {
 // Secondary task
 after(() =\> {
 log();
 });

 // Primary task
 return \{children}\;
}
\`\`\`
Read more about the [`after`](/docs/app/api-reference/functions/after) API and how to leverage it in the documentation.

## [`forbidden` and `unauthorized` (experimental)](#forbidden-and-unauthorized-experimental)

Next.js 15\.1 includes two experimental APIs, `forbidden()` and `unauthorized()`, based on community feedback.

> **We’d love your feedback** — please try it in your development environments and share your thoughts in this [discussion thread](https://github.com/vercel/next.js/discussions/73753).

### [Overview](#overview)

If you’re familiar with the App Router, you’ve likely used [`notFound()`](/docs/app/api-reference/file-conventions/not-found) to trigger 404 behavior alongside the customizable `not-found.tsx` file. With version 15\.1, we’re extending this approach to authorization errors:

• `forbidden()` triggers a **403 error** with customizable UI via `forbidden.tsx`.

• `unauthorized()` triggers a **401 error** with customizable UI via `unauthorized.tsx`.

> **Good to know:** As with `notFound()` errors, the status code will be `200` if the error is triggered after initial response headers have been sent. [Learn more](/docs/app/building-your-application/routing/loading-ui-and-streaming#status-codes).

### [Enabling the feature](#enabling-the-feature)

As this feature is still experimental, you’ll need to enable it in your `next.config.ts` file:

next.config.ts\`\`\`
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
 experimental: {
 authInterrupts: true,
 },
};

export default nextConfig;
\`\`\`

> **Note:** `next.config.ts` support was introduced in Next.js 15\. [Learn more](/docs/app/api-reference/config/next-config-js#typescript).

### [Using `forbidden()` and `unauthorized()`](#using-forbidden-and-unauthorized)

You can use `forbidden()` and `unauthorized()` in Server Actions, Server Components, Client Components, or Route Handlers. Here’s an example:

\`\`\`
import { verifySession } from '@/app/lib/dal';
import { forbidden } from 'next/navigation';

export default async function AdminPage() {
 const session = await verifySession();

 // Check if the user has the 'admin' role
 if (session.role !== 'admin') {
 forbidden();
 }

 // Render the admin page for authorized users
 return \Admin Page\;
}
\`\`\`
### [Creating custom error pages](#creating-custom-error-pages)

To customize the error pages, create the following files:

app/forbidden.tsx\`\`\`
import Link from 'next/link';

export default function Forbidden() {
 return (
 \
 \Forbidden\
 \You are not authorized to access this resource.\
 \Return Home\
 \
 );
}
\`\`\`
app/unauthorized.tsx\`\`\`
import Link from 'next/link';

export default function Unauthorized() {
 return (
 \
 \Unauthorized\
 \Please log in to access this page.\
 \Go to Login\
 \
 );
}
\`\`\`
We'd like to thank [Clerk](https://clerk.com) for proposing this feature through a PR and assisting us in prototyping the API. Before we stabilize this feature in 15\.2, we're planning on adding more capabilities and improvements to the APIs to support a wider range of use cases.

Read the documentation for the [`unauthorized`](/docs/app/api-reference/functions/unauthorized) and [`forbidden`](/docs/app/api-reference/functions/forbidden) APIs for more details.

## [Other Changes](#other-changes)

* **\[Feature]** Use ESLint 9 in `create-next-app` ([PR](https://github.com/vercel/next.js/pull/72762))
* **\[Feature]** Increase max cache tags to 128 ([PR](https://github.com/vercel/next.js/pull/73124))
* **\[Feature]** Add an option to disable experimental CssChunkingPlugin ([PR](https://github.com/vercel/next.js/pull/73286))
* **\[Feature]** Add experimental CSS inlining support ([PR](https://github.com/vercel/next.js/pull/72195))
* **\[Improvement]** Silence Sass `legacy-js-api` warning ([PR](https://github.com/vercel/next.js/pull/72632))
* **\[Improvement]** Fix unhandled rejection when using rewrites ([PR](https://github.com/vercel/next.js/pull/72530))
* **\[Improvement]** Ensure parent process exits when webpack worker fails ([PR](https://github.com/vercel/next.js/pull/72921))
* **\[Improvement]** Fixed route interception on a catch\-all route ([PR](https://github.com/vercel/next.js/pull/72902))
* **\[Improvement]** Fixed response cloning issue in request deduping ([PR](https://github.com/vercel/next.js/pull/73274))
* **\[Improvement]** Fixed Server Action redirects between multiple root layouts ([PR](https://github.com/vercel/next.js/pull/73063))
* **\[Improvement]** Support providing MDX plugins as strings for Turbopack compatibility ([PR](https://github.com/vercel/next.js/pull/72802))

## [Contributors](#contributors)

Next.js is the result of the combined work of over 3,000 individual developers. This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Hendrik](https://github.com/unstubbable), [Janka](https://github.com/lubieowoce), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [Jiwon](https://github.com/devjiwonchoi), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Jude](https://github.com/gaojude), [Sam](https://github.com/samcx), [Sebastian](https://github.com/sebmarkbage), [Sebbie](https://github.com/eps1lon), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Alex](https://github.com/arlyon), [Benjamin](https://github.com/bgw), [Donny](https://github.com/kdy1), [Maia](https://github.com/padmaia), [Niklas](https://github.com/mischnic), [Tim](https://github.com/timneutkens), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* The **Next.js Docs** team: [Delba](https://github.com/delbaoliveira), [Rich](https://github.com/molebox), [Ismael](https://github.com/ismaelrumzan), and [Lee](https://github.com/leerob).

Huge thanks to @sokra, @molebox, @delbaoliveira, @eps1lon, @wbinnssmith, @JamBalaya56562, @hyungjikim, @adrian\-faustino, @mottox2, @lubieowoce, @bgw, @mknichel, @wyattjoh, @huozhi, @kdy1, @mischnic, @ijjk, @icyJoseph, @acdlite, @unstubbable, @gaojude, @devjiwonchoi, @cena\-ko, @lforst, @devpla, @samcx, @styfle, @ztanner, @Marukome0743, @timneutkens, @JeremieDoctrine, @ductnn, @karlhorky, @reynaldichernando, @chogyejin, @y\-yagi, @philparzer, @alfawal, @Rhynden, @arlyon, @MJez29, @Goodosky, @themattmayfield, @tobySolutions, @kevinmitch14, @leerob, @emmanuelgautier, @mrhrifat, @lid0a, @boar\-is, @nisabmohd, @PapatMayuri, @ovogmap, @Reflex2468, @LioRael, @betterthanhajin, @HerringtonDarkholme, @bpb54321, @ahmoin, @Kikobeats, @abdelrahmanAbouelkheir, @lumirlumir, @yeeed711, @petter, and @suu3 for helping!



## Next.js 14 | Next.js

[Read the full article](https://nextjs.org/blog/next-14)

[Back to Blog](/blog)Thursday, October 26th 2023

# Next.js 14

Posted by[Lee Robinson@leeerob](https://twitter.com/leeerob)[Tim Neutkens@timneutkens](https://twitter.com/timneutkens)As we announced at [Next.js Conf](https://nextjs.org/conf), Next.js 14 is our most focused release with:

* [**Turbopack**](#nextjs-compiler-turbocharged): 5,000 tests passing for App \& Pages Router
	+ **53% faster** local server startup
	+ **94% faster** code updates with Fast Refresh
* [**Server Actions (Stable)**](#forms-and-mutations): Progressively enhanced mutations
	+ Integrated with caching \& revalidating
	+ Simple function calls, or works natively with forms
* [**Partial Prerendering (Preview)**](#partial-prerendering-preview): Fast initial static response \+ streaming dynamic content
* [**Next.js Learn (New)**](#nextjs-learn-course): Free course teaching the App Router, authentication, databases, and more.

Upgrade today or get started with:

Terminal\`\`\`
npx create\-next\-app@latest
\`\`\`
## [Next.js Compiler: Turbocharged](#nextjs-compiler-turbocharged)

Since Next.js 13, we've been working to improve local development performance in Next.js in both the Pages and App Router.

Previously, we were rewriting `next dev` and other parts of Next.js to support this effort. We have since changed our approach to be more incremental. This means our Rust\-based compiler will reach stability soon, as we've refocused on supporting all Next.js features first.

5,000 integration tests for `next dev` are now passing with [Turbopack](https://turbo.build/pack), our underlying Rust engine. These tests include 7 years of bug fixes and reproductions.

While testing on `vercel.com`, a large Next.js application, we've seen:

* Up to **53\.3% faster** local server startup
* Up to **94\.7% faster** code updates with Fast Refresh

This benchmark is a practical result of performance improvements you should expect with a large application (and large module graph). With 90% of tests for `next dev` now passing, you should see faster and more reliable performance consistently when using `next dev --turbo`.

Once we hit 100% of tests passing, we'll move Turbopack to stable in an upcoming minor release. We'll also continue to support using webpack for custom configurations and ecosystem plugins.

You can follow the percentage of tests passing at [areweturboyet.com](https://areweturboyet.com).

## [Forms and Mutations](#forms-and-mutations)

Next.js 9 introduced API Routes—a way to quickly build backend endpoints alongside your frontend code.

For example, you would create a new file in the `api/` directory:

pages/api/submit.ts\`\`\`
import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(
 req: NextApiRequest,
 res: NextApiResponse,
) {
 const data = req.body;
 const id = await createItem(data);
 res.status(200\).json({ id });
}
\`\`\`
Then, on the client\-side, you could use React and an event handler like `onSubmit` to make a `fetch` to your API Route.

pages/index.tsx\`\`\`
import { FormEvent } from 'react';

export default function Page() {
 async function onSubmit(event: FormEvent\) {
 event.preventDefault();

 const formData = new FormData(event.currentTarget);
 const response = await fetch('/api/submit', {
 method: 'POST',
 body: formData,
 });

 // Handle response if necessary
 const data = await response.json();
 // ...
 }

 return (
 \
 \
 \Submit\
 \
 );
}
\`\`\`
Now with Next.js 14, we want to simplify the developer experience of authoring data mutations. Further, we want to improve the user experience when the user has a slow network connection, or when submitting a form from a lower\-powered device.

### [Server Actions (Stable)](#server-actions-stable)

What if you didn't need to manually create an API Route? Instead, you could define a function that runs securely on the server, called directly from your React components.

The App Router is built on the React `canary` channel, which is [stable for frameworks](https://react.dev/blog/2023/05/03/react-canaries) to adopt new features. As of v14, Next.js has upgraded to the latest React `canary`, which includes stable Server Actions.

The previous example from the Pages Router can be simplified to one file:

app/page.tsx\`\`\`
export default function Page() {
 async function create(formData: FormData) {
 'use server';
 const id = await createItem(formData);
 }

 return (
 \
 \
 \Submit\
 \
 );
}
\`\`\`
Server Actions should feel familiar for any developers who have previously used server\-centric frameworks in the past. It's built on web fundamentals like forms and the [FormData Web API](https://developer.mozilla.org/en-US/docs/Web/API/FormData).

While using Server Actions through a form is helpful for progressive enhancement, it is not a requirement. You can also call them directly as a function, without a form. When using TypeScript, this gives you full end\-to\-end type\-safety between the client and server.

Mutating data, re\-rendering the page, or redirecting can happen in **one network roundtrip**, ensuring the correct data is displayed on the client, even if the upstream provider is slow. Further, you can compose and reuse different actions, including many different actions in the same route.

### [Caching, Revalidating, Redirecting, and more](#caching-revalidating-redirecting-and-more)

Server Actions are deeply integrated into the entire App Router model. You can:

* Revalidate cached data with `revalidatePath()` or `revalidateTag()`
* Redirect to different routes through `redirect()`
* Set and read cookies through `cookies()`
* Handle optimistic UI updates with `useOptimistic()`
* Catch and display errors from the server with `useFormState()`
* Display loading states on the client with `useFormStatus()`

Learn more about [Forms and Mutations with Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/forms-and-mutations) or about the [security model](https://nextjs.org/blog/security-nextjs-server-components-actions) and best practices for Server Components and Server Actions.

## [Partial Prerendering (Preview)](#partial-prerendering-preview)

We'd like to share a preview of Partial Prerendering — a compiler optimization for dynamic content with a fast initial static response — that we're working on for Next.js.

Partial Prerendering builds on a decade of research and development into server\-side rendering (SSR), static\-site generation (SSG), and incremental static revalidation (ISR).

### [Motivation](#motivation)

We've heard your feedback. There's currently too many runtimes, configuration options, and rendering methods to have to consider. You want the speed and reliability of static, while also supporting fully dynamic, personalized responses.

Having great performance globally *and* personalization shouldn't come at the cost of complexity.

Our challenge was to create a better developer experience, simplifying the existing model without introducing new APIs for developers to learn. While partial caching of server\-side content has existed, these approaches still need to meet the developer experience and composability goals we aim for.

**Partial Prerendering requires no new APIs to learn.**

### [Built on React Suspense](#built-on-react-suspense)

Partial Prerendering is defined by your Suspense boundaries. Here's how it works. Consider the following ecommerce page:

app/page.tsx\`\`\`
export default function Page() {
 return (
 \
 \
 \My Store\
 \}\>
 \
 \
 \
 \
 \}\>
 \
 \
 \
 \
 );
}
\`\`\`
With Partial Prerendering enabled, this page generates a static shell based on your `` boundaries. The `fallback` from React Suspense is prerendered.

Suspense fallbacks in the shell are then replaced with dynamic components, like reading cookies to determine the cart, or showing a banner based on the user.

When a request is made, the static HTML shell is immediately served:

\`\`\`
\
 \
 \My Store\
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
Since `` reads from `cookies` to look at the user session, this component is then streamed in as part of the same HTTP request as the static shell. There are no extra network roundtrips needed.

app/cart.tsx\`\`\`
import { cookies } from 'next/headers'

export default function ShoppingCart() {
 const cookieStore = cookies()
 const session = cookieStore.get('session')
 return ...
}
\`\`\`
To have the most granular static shell, this may require adding additional Suspense boundaries. However, if you're already using `loading.js` today, this is an implicit Suspense boundary, so no changes would be required to generate the static shell.

### [Coming soon](#coming-soon)

Partial prerendering is under active development. We'll be sharing more updates in an upcoming minor release.

## [Metadata Improvements](#metadata-improvements)

Before your page content can be streamed from the server, there's important metadata about the viewport, color scheme, and theme that need to be sent to the browser first.

Ensuring these `meta` tags are sent with the initial page content helps a smooth user experience, preventing the page from flickering by changing the theme color, or shifting layout due to viewport changes.

In Next.js 14, we've decoupled blocking and non\-blocking metadata. Only a small subset of metadata options are blocking, and we want to ensure non\-blocking metadata will not prevent a partially prerendered page from serving the static shell.

The following metadata options are now deprecated and will be removed from `metadata` in a future major version:

* `viewport`: Sets the initial zoom and other properties of the viewport
* `colorScheme`: Sets the support modes (light/dark) for the viewport
* `themeColor`: Sets the color the chrome around the viewport should render with

Starting with Next.js 14, there are new options [`viewport` and `generateViewport`](https://nextjs.org/docs/app/api-reference/functions/generate-viewport) to replace these options. All other `metadata` options remain the same.

You can start adopting these new APIs today. The existing `metadata` options will continue to work.

## [Next.js Learn Course](#nextjs-learn-course)

Today we're releasing a brand new, free course on [Next.js Learn](https://nextjs.org/learn). This course teaches:

* The Next.js App Router
* Styling and Tailwind CSS
* Optimizing Fonts and Images
* Creating Layouts and Pages
* Navigating Between Pages
* Setting Up Your Postgres Database
* Fetching Data with Server Components
* Static and Dynamic Rendering
* Streaming
* Partial Prerendering (Optional)
* Adding Search and Pagination
* Mutating Data
* Handling Errors
* Improving Accessibility
* Adding Authentication
* Adding Metadata

Next.js Learn has taught millions of developers about the foundations of the framework, and we can't wait to hear your feedback on our new addition. Head to [nextjs.org/learn](https://nextjs.org/learn) to take the course.

## [Other Changes](#other-changes)

* **\[Breaking]** Minimum Node.js version is now `18.17`
* **\[Breaking]** Removes WASM target for `next-swc` build ([PR](https://github.com/vercel/next.js/pull/57437))
* **\[Breaking]** Dropped support for `@next/font` in favor of `next/font` ([Codemod](https://nextjs.org/docs/app/building-your-application/upgrading/codemods#built-in-next-font))
* **\[Breaking]** Changed `ImageResponse` import from `next/server` to `next/og` ([Codemod](https://nextjs.org/docs/app/building-your-application/upgrading/codemods#next-og-import))
* **\[Breaking]** `next export` command has been removed in favor of `output: 'export'` config ([Docs](https://nextjs.org/docs/app/building-your-application/deploying/static-exports))
* **\[Deprecation]** `onLoadingComplete` for `next/image` is deprecated in favor of [`onLoad`](https://nextjs.org/docs/app/api-reference/components/image#onload)
* **\[Deprecation]** `domains` for `next/image` is deprecated in favor of [`remotePatterns`](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns)
* **\[Feature]** More verbose logging around `fetch` caching can be enabled ([Docs](https://nextjs.org/docs/app/api-reference/next-config-js/logging))
* **\[Improvement]** 80% smaller function size for a basic `create-next-app` application
* **\[Improvement]** Enhanced memory management when using `edge` runtime in development

## [Contributors](#contributors)

Next.js is the result of the combined work of over 2,900 individual developers, industry partners like Google and Meta, and our core team at Vercel. Join the community on [GitHub Discussions](https://github.com/vercel/next.js/discussions), [Reddit](https://www.reddit.com/r/nextjs/), and [Discord](/discord).

This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Balazs](https://github.com/balazsorban44), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Sebastian](https://github.com/sebmarkbage), [Shu](https://github.com/shuding), [Steven](https://github.com/styfle), [Tim](https://github.com/timneutkens), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Donny](https://github.com/kdy1), [Justin](https://github.com/jridgewell), [Leah](https://github.com/forsakenharmony), [Maia](https://github.com/padmaia), [OJ](https://github.com/kwonoj), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* **Next.js Learn**: [Delba](https://github.com/delbaoliveira), [Steph](https://github.com/StephDietz), [Emil](https://github.com/emilkowalski), [Balazs](https://github.com/balazsorban44), [Hector](https://github.com/dizzyup), and [Amy](https://github.com/timeyoutakeit).

And the contributions of: @05lazy, @0xadada, @2\-NOW, @aarnadlr, @aaronbrown\-vercel, @aaronjy, @abayomi185, @abe1272001, @abhiyandhakal, @abstractvector, @acdlite, @adamjmcgrath, @AdamKatzDev, @adamrhunter, @ademilter, @adictonator, @adilansari, @adtc, @afonsojramos, @agadzik, @agrattan0820, @akd\-io, @AkifumiSato, @akshaynox, @alainkaiser, @alantoa, @albertothedev, @AldeonMoriak, @aleksa\-codes, @alexanderbluhm, @alexkirsz, @alfred\-mountfield, @alpha\-xek, @andarist, @Andarist, @andrii\-bodnar, @andykenward, @angel1254mc, @anonrig, @anthonyshew, @AntoineBourin, @anujssstw, @apeltop, @aralroca, @aretrace, @artdevgame, @artechventure, @arturbien, @Aryan9592, @AviAvinav, @aziyatali, @BaffinLee, @Banbarashik, @bencmbrook, @benjie, @bennettdams, @bertho\-zero, @bigyanse, @Bitbbot, @blue\-devil1134, @bot08, @bottxiang, @Bowens20832, @bre30kra69cs, @BrennanColberg, @brkalow, @BrodaNoel, @Brooooooklyn, @brunoeduardodev, @brvnonascimento, @carlos\-menezes, @cassidoo, @cattmote, @cesarkohl, @chanceaclark, @charkour, @charlesbdudley, @chibicode, @chrisipanaque, @ChristianIvicevic, @chriswdmr, @chunsch, @ciruz, @cjmling, @clive\-h\-townsend, @colinhacks, @colinking, @coreyleelarson, @Cow258, @cprussin, @craigwheeler, @cramforce, @cravend, @cristobaldominguez95, @ctjlewis, @cvolant, @cxa, @danger\-ahead, @daniel\-web\-developer, @danmindru, @dante\-robinson, @darshanjain\-entrepreneur, @darshkpatel, @davecarlson, @David0z, @davidnx, @dciug, @delbaoliveira, @denchance, @DerTimonius, @devagrawal09, @DevEsteves, @devjiwonchoi, @devknoll, @DevLab2425, @devvspaces, @didemkkaslan, @dijonmusters, @dirheimerb, @djreillo, @dlehmhus, @doinki, @dpnolte, @Drblessing, @dtinth, @ducanhgh, @DuCanhGH, @ductnn, @duncanogle, @dunklesToast, @DustinsCode, @dvakatsiienko, @dvoytenko, @dylanjha, @ecklf, @EndangeredMassa, @eps1lon, @ericfennis, @escwxyz, @Ethan\-Arrowood, @ethanmick, @ethomson, @fantaasm, @feikerwu, @ferdingler, @FernandVEYRIER, @feugy, @fgiuliani, @fomichroman, @Fonger, @ForsakenHarmony, @franktronics, @FSaldanha, @fsansalvadore, @furkanmavili, @g12i, @gabschne, @gaojude, @gdborton, @gergelyke, @gfgabrielfranca, @gidgudgod, @Gladowar, @Gnadhi, @gnoff, @goguda, @greatSumini, @gruz0, @Guilleo03, @gustavostz, @hanneslund, @HarshaVardhanReddyDuvvuru, @haschikeks, @Heidar\-An, @heyitsuzair, @hiddenest, @hiro0218, @hotters, @hsrvms, @hu0p, @hughlilly, @HurSungYun, @hustLer2k, @iamarpitpatidar, @ianldgs, @ianmacartney, @iaurg, @ibash, @ibrahemid, @idoob, @iiegor, @ikryvorotenko, @imranbarbhuiya, @ingovals, @inokawa, @insik\-han, @isaackatayev, @ishaqibrahimbot, @ismaelrumzan, @itsmingjie, @ivanhofer, @IvanKiral, @jacobsfletch, @jakemstar, @jamespearson, @JanCizmar, @janicklas\-ralph, @jankaifer, @JanKaifer, @jantimon, @jaredpalmer, @javivelasco, @jayair, @jaykch, @Jeffrey\-Zutt, @jenewland1999, @jeremydouglas, @JesseKoldewijn, @jessewarren\-aa, @jimcresswell, @jiwooIncludeJeong, @jocarrd, @joefreeman, @JohnAdib, @JohnAlbin, @JohnDaly, @johnnyomair, @johnta0, @joliss, @jomeswang, @joostdecock, @Josehower, @josephcsoti, @josh, @joshuabaker, @JoshuaKGoldberg, @joshuaslate, @joulev, @jsteele\-stripe, @JTaylor0196, @JuanM04, @jueungrace, @juliusmarminge, @Juneezee, @Just\-Moh\-it, @juzhiyuan, @jyunhanlin, @kaguya3222, @karlhorky, @kevinmitch14, @keyz, @kijikunnn, @kikobeats, @Kikobeats, @kleintorres, @koba04, @koenpunt, @koltong, @konomae, @kosai106, @krmeda, @kvnang, @kwonoj, @ky1ejs, @kylemcd, @labyrinthitis, @lachlanjc, @lacymorrow, @laityned, @Lantianyou, @leerob, @leodr, @leoortizz, @li\-jia\-nan, @loettz, @lorenzobloedow, @lubakravche, @lucasassisrosa, @lucasconstantino, @lucgagan, @LukeSchlangen, @LuudJanssen, @lycuid, @M3kH, @m7yue, @manovotny, @maranomynet, @marcus\-rise, @MarDi66, @MarkAtOmniux, @martin\-wahlberg, @masnormen, @matepapp, @matthew\-heath, @mattpr, @maxleiter, @MaxLeiter, @maxproske, @meenie, @meesvandongen, @mhmdrioaf, @michaeloliverx, @mike\-plummer, @MiLk, @milovangudelj, @Mingyu\-Song, @mirismaili, @mkcy3, @mknichel, @mltsy, @mmaaaaz, @mnajdova, @moetazaneta, @mohanraj\-r, @molebox, @morganfeeney, @motopods, @mPaella, @mrkldshv, @mrxbox98, @nabsul, @nathanhammond, @nbouvrette, @nekochantaiwan, @nfinished, @Nick\-Mazuk, @nickmccurdy, @niedziolkamichal, @niko20, @nikolovlazar, @nivak\-monarch, @nk980113, @nnnnoel, @nocell, @notrab, @nroland013, @nuta, @nutlope, @obusk, @okcoker, @oliviertassinari, @omarhoumz, @opnay, @orionmiz, @ossan\-engineer, @patrick91, @pauek, @peraltafederico, @Phiction, @pn\-code, @pyjun01, @pythagoras\-yamamoto, @qrohlf, @raisedadead, @reconbot, @reshmi\-sriram, @reyrodrigez, @ricardofiorani, @rightones, @riqwan, @rishabhpoddar, @rjsdnql123, @rodrigofeijao, @runjuu, @Ryan\-Dia, @ryo\-manba, @s0h311, @sagarpreet\-xflowpay, @sairajchouhan, @samdenty, @samsisle, @sanjaiyan\-dev, @saseungmin, @SCG82, @schehata, @Schniz, @sepiropht, @serkanbektas, @sferadev, @ShaunFerris, @shivanshubisht, @shozibabbas, @silvioprog, @simonswiss, @simPod, @sivtu, @SleeplessOne1917, @smaeda\-ks, @sonam\-serchan, @SonMooSans, @soonoo, @sophiebits, @souporserious, @sp00ls, @sqve, @sreetamdas, @stafyniaksacha, @starunaway, @steebchen, @stefanprobst, @steppefox, @steven\-tey, @suhaotian, @sukkaw, @SukkaW, @superbahbi, @SuttonJack, @svarunid, @swaminator, @swarnava, @syedtaqi95, @taep96, @taylorbryant, @teobler, @Terro216, @theevilhead, @thepatrick00, @therealrinku, @thomasballinger, @thorwebdev, @tibi1220, @tim\-hanssen, @timeyoutakeit, @tka5, @tknickman, @tomryanx, @trigaten, @tristndev, @tunamagur0, @tvthatsme, @tyhopp, @tyler\-lutz, @UnknownMonk, @v1k1, @valentincostam, @valentinh, @valentinpolitov, @vamcs, @vasucp1207, @vicsantizo, @vinaykulk621, @vincenthongzy, @visshaljagtap, @vladikoff, @wherehows, @WhoAmIRUS, @WilderDev, @Willem\-Jaap, @williamli, @wiredacorn, @wiscaksono, @wojtekolek, @ws\-jm, @wxh06, @wyattfry, @wyattjoh, @xiaolou86, @y\-tsubuku, @yagogmaisp, @yangshun, @yasath, @Yash\-Singh1, @yigithanyucedag, @ykzts, @Yovach, @yutsuten, @yyuemii, @zek, @zekicaneksi, @zignis, and @zlrlyy



## Next.js 14.2 | Next.js

[Read the full article](https://nextjs.org/blog/next-14-2)

[Back to Blog](/blog)Thursday, April 11th 2024

# Next.js 14\.2

Posted by[Delba de Oliveira@delba\_oliveira](https://twitter.com/delba_oliveira)[Tim Neutkens@timneutkens](https://twitter.com/timneutkens)Next.js 14\.2 includes development, production, and caching improvements.

* [**Turbopack for Development (Release Candidate):**](#turbopack-for-development-release-candidate) 99\.8% tests passing for `next dev --turbo`.
* [**Build and Production Improvements:**](#build-and-production-improvements) Reduced build memory usage and CSS optimizations.
* [**Caching Improvements:**](#caching-improvements) Configurable invalidation periods with `staleTimes`.
* [**Error DX Improvements:**](#errors-dx-improvements) Better hydration mismatch errors and design updates.

Upgrade today or get started with:

Terminal\`\`\`
npx create\-next\-app@latest
\`\`\`
## [Turbopack for Development (Release Candidate)](#turbopack-for-development-release-candidate)

Over the past few months, we’ve been working on improving local development performance with Turbopack. In version 14\.2, the Turbopack **Release Candidate** is now available for local development:

* **99\.8%** of [integrations tests](https://areweturboyet.com/) are now passing.
* We’ve verified the top 300 `npm` packages used in Next.js applications can compile with Turbopack.
* All [Next.js examples](https://github.com/vercel/next.js/tree/canary/examples) work with Turbopack.
* We’ve integrated [Lightning CSS](https://lightningcss.dev/), a fast CSS bundler and minifier, written in Rust.

We’ve been extensively dogfooding Turbopack with Vercel’s applications. For example, with `vercel.com`, a large Next.js app, we've seen:

* Up to **76\.7% faster** local server startup.
* Up to **96\.3% faster** code updates with Fast Refresh.
* Up to **45\.8% faster** initial route compile without caching (Turbopack does not have disk caching yet).

Turbopack continues to be opt\-in and you can try it out with:

Terminal\`\`\`
next dev \-\-turbo
\`\`\`
We will now be focusing on improving memory usage, implementing persistent caching, and `next build --turbo`.

* **Memory Usage** \- We’ve built low\-level tools for investigating memory usage. You can now [generate traces](/docs/architecture/turbopack#generating-trace-files) that include both performance metrics and broad memory usage information. These traces allows us to investigate performance and memory usage without needing access to your application’s source code.
* **Persistent Caching** \- We’re also exploring the best architecture options, and we’re expecting to share more details in a future release.
* **`next build`** \- While Turbopack is not available for builds yet, **74\.7%** of tests are already passing. You can follow the progress at [areweturboyet.com/build](https://areweturboyet.com/build).

To see a list of [supported](/docs/architecture/turbopack#supported-features) and [unsupported features](/docs/architecture/turbopack#unsupported-features) in Turbopack, please refer to our [documentation](/docs/architecture/turbopack).

## [Build and Production Improvements](#build-and-production-improvements)

In addition to bundling improvements with Turbopack, we’ve worked to improve overall build and production performance for all Next.js applications (both Pages and App Router).

### [Tree\-shaking](#tree-shaking)

We identified an optimization for the boundary between Server and Client Components that allows for tree\-shaking unused exports. For example, importing a single `Icon` component from a file that has `"use client"` no longer includes all the other icons from that package. This can largely reduce the production JavaScript bundle size.

Testing this optimization on a popular library like `react-aria-components` reduced the final bundle size by **\-51\.3%**.

> **Note:** This optimization does not currently work with barrel files. In the meantime, you can use the [`optimizePackageImports`](/docs/app/api-reference/next-config-js/optimizePackageImports) config option:
> 
> 
> next.config.ts\`\`\`
> module.exports = {
>  experimental: {
>  optimizePackageImports: \['package\-name'],
>  },
> };
> \`\`\`

### [Build Memory Usage](#build-memory-usage)

For extremely large\-scale Next.js applications, we noticed out\-of\-memory crashes (OOMs) during production builds. After investigating user reports and reproductions, we identified the root issue was over\-bundling and minification (Next.js created fewer, larger JavaScript files with duplication). We’ve refactored the bundling logic and optimized the compiler for these cases.

Our early tests show that on a minimal Next.js app, memory usage and cache file size decreased **from 2\.2GB to under 190MB** on average.

To make it easier to debug memory performance, we’ve introduced a `--experimental-debug-memory-usage` flag to `next build`. Learn more in our [documentation](/docs/app/building-your-application/optimizing/memory-usage).

### [CSS](#css)

We updated how CSS is optimized during production Next.js builds by chunking CSS to avoid conflicting styles when you navigate between pages.

The order and merging of CSS chunks are now defined by the import order. For example, `base-button.module.css` will be ordered before `page.module.css`:

base\-button.tsx\`\`\`
import styles from './base\-button.module.css';

export function BaseButton() {
 return \;
}
\`\`\`
page.tsx\`\`\`
import { BaseButton } from './base\-button';
import styles from './page.module.css';

export function Page() {
 return \;
}
\`\`\`
To maintain the correct CSS order, we recommend:

* Using [CSS Modules](/docs/app/building-your-application/styling/css-modules) over [global styles](/docs/app/building-your-application/styling/css-modules#global-styles).
* Only import a CSS Module in a single JS/TS file.
* If using global class names, import the global styles in the same JS/TS too.

We don’t expect this change to negatively impact the majority of applications. However, if you see any unexpected styles when upgrading, please review your CSS import order as per the recommendations in our [documentation](/docs/app/building-your-application/styling/css#ordering-and-merging).

## [Caching Improvements](#caching-improvements)

Caching is a critical part of building fast and reliable web applications. When performing mutations, both users and developers expect the cache to be updated to reflect the latest changes. We've been exploring how to improve the Next.js caching experience in the App Router.

### [`staleTimes` (Experimental)](#staletimes-experimental)

The [Client\-side Router Cache](/docs/app/building-your-application/caching#data-cache-and-client-side-router-cache) is a caching layer designed to provide a fast navigation experience by caching visited and prefetched routes on the client.

Based on community feedback, we’ve added an experimental `staleTimes` option to allow the [client\-side router cache](/docs/app/building-your-application/caching#router-cache) invalidation period to be configured.

By default, prefetched routes (using the `` component without the `prefetch` prop) will be cached for 30 seconds, and if the `prefetch` prop is set to `true`, 5 minutes. You can overwrite these default values by defining custom [revalidation times](/docs/app/building-your-application/caching#duration-3) in `next.config.js`:

next.config.ts\`\`\`
const nextConfig = {
 experimental: {
 staleTimes: {
 dynamic: 30,
 static: 180,
 },
 },
};

module.exports = nextConfig;
\`\`\`
`staleTimes` aims to improve the current experience of users who want more control over caching heuristics, but it is not intended to be the complete solution. In upcoming releases, we will focus on improving the overall caching semantics and providing more flexible solutions.

Learn more about `staleTimes` in our [documentation](/docs/app/api-reference/next-config-js/staleTimes).

### [Parallel and Intercepting Routes](#parallel-and-intercepting-routes)

We are continuing to iterate on on [Parallel](/docs/app/building-your-application/routing/parallel-routes) and [Intercepting](/docs/app/building-your-application/routing/intercepting-routes) Routes, now improving the integration with the Client\-side Router Cache.

* Parallel and Intercepting routes that invoke Server Actions with [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag) will revalidate the cache and refresh the visible slots while maintaining the user’s current view.
* Similarly, calling [`router.refresh`](/docs/app/building-your-application/caching#routerrefresh) now correctly refreshes visible slots, maintaining the current view.

## [Errors DX Improvements](#errors-dx-improvements)

In version 14\.1, we started working on [improving the readability of error messages and stack traces](/blog/next-14-1#improved-error-messages-and-fast-refresh) when running `next dev`. This work has continued into 14\.2 to now include better error messages, overlay design improvements for both App Router and Pages Router, light and dark mode support, and clearer `dev` and `build` logs.

For example, React Hydration errors are a common source of confusion in our community. While we made improvements to help users pinpoint the source of hydration mismatches (see below), we're working with the React team to improve the underlying error messages and show the file name where the error occurred.

**Before:**



An example of the Next.js error overlay before version 14\.2\.

**After:**



An example of the Next.js error overlay after version 14\.2\.

## [React 19](#react-19)

In February, the React team announced the upcoming release of [React 19](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024#the-next-major-version-of-react). To prepare for React 19, we're working on integrating the latest features and improvements into Next.js, and plan on releasing a major version to orchestrate these changes.

New features like Actions and their related hooks, which have been available within Next.js from the [React canary channel](https://react.dev/blog/2023/05/03/react-canaries), will now all be available for all React applications (including client\-only applications). We're excited to see wider adoption of these features in the React ecosystem.

## [Other Improvements](#other-improvements)

* **\[Docs]** New documentation on Video Optimization ([PR](https://github.com/vercel/next.js/pull/60574)).
* **\[Docs]** New documentation on `instrumentation.ts` ([PR](https://github.com/vercel/next.js/pull/61403))
* **\[Feature]** New `overrideSrc` prop for `next/image` ([PR](https://github.com/vercel/next.js/pull/64221)).
* **\[Feature]** New `revalidateReason` argument to `getStaticProps` ([PR](https://github.com/vercel/next.js/pull/64258)).
* **\[Improvement]** Refactored streaming logic, reducing the time to stream pages in production ([PR](https://github.com/vercel/next.js/pull/63427)).
* **\[Improvement]** Support for nested Server Actions ([PR](https://github.com/vercel/next.js/pull/61001)).
* **\[Improvement]** Support for localization in generated Sitemaps ([PR](https://github.com/vercel/next.js/pull/53765)).
* **\[Improvement]** Visual improvements to dev and build logs ([PR](https://github.com/vercel/next.js/pull/62946))
* **\[Improvement]** Skew protection is stable on Vercel ([Docs](https://vercel.com/docs/deployments/skew-protection)).
* **\[Improvement]** Make `useSelectedLayoutSegment` compatible with the Pages Router ([PR](https://github.com/vercel/next.js/pull/62584)).
* **\[Improvement]** Skip `metadataBase` warnings when absolute URLs don’t need to be resolved ([PR](https://github.com/vercel/next.js/pull/61898)).
* **\[Improvement]** Fix Server Actions not submitting without JavaScript enabled when deployed to Vercel ([PR](https://github.com/vercel/next.js/pull/63978))
* **\[Improvement]** Fix error about a Server Action not being found in the actions manifest if triggered after navigating away from referring page, or if used inside of an inactive parallel route segment ([PR](https://github.com/vercel/next.js/pull/64227))
* **\[Improvement]** Fix CSS imports in components loaded by `next/dynamic` ([PR](https://github.com/vercel/next.js/pull/64294)).
* **\[Improvement]** Warn when animated image is missing `unoptimized` prop ([PR](https://github.com/vercel/next.js/pull/61045)).
* **\[Improvement]** Show an error message if `images.loaderFile` doesn't export a default function ([PR](https://github.com/vercel/next.js/pull/64036))

## [Community](#community)


Next.js now has over 1 million monthly active developers. We're grateful for the community's support and contributions. Join the conversation on [GitHub Discussions](https://github.com/vercel/next.js/discussions), [Reddit](https://www.reddit.com/r/nextjs/), and [Discord](/discord).

## [Contributors](#contributors)

Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel.
This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Balazs](https://github.com/balazsorban44), [Ethan](https://github.com/Ethan-Arrowood), [Janka](https://github.com/lubieowoce), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Sam](https://github.com/samcx), [Sebastian](https://github.com/sebmarkbage), [Sebbie](https://github.com/eps1lon), [Shu](https://github.com/shuding), [Steven](https://github.com/styfle), [Tim](https://github.com/timneutkens), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Donny](https://github.com/kdy1), [Leah](https://github.com/forsakenharmony), [Maia](https://github.com/padmaia), [OJ](https://github.com/kwonoj), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* **Next.js Docs**: [Delba](https://github.com/delbaoliveira), [Steph](https://github.com/StephDietz), [Michael](https://github.com/manovotny), [Anthony](https://github.com/anthonyshew), and [Lee](https://github.com/leerob).

Huge thanks to @taishikato, @JesseKoldewijn, @Evavic44, @feugy, @liamlaverty, @dvoytenko, @SukkaW, @wbinnssmith, @rishabhpoddar, @better\-salmon, @ziyafenn, @A7med3bdulBaset, @jasonuc, @yossydev, @Prachi\-meon, @InfiniteCodeMonkeys, @ForsakenHarmony, @miketimmerman, @kwonoj, @williamli, @gnoff, @jsteele\-stripe, @chungweileong94, @WITS, @sogoagain, @junioryono, @eisafaqiri, @yannbolliger, @aramikuto, @rocketman\-21, @kenji\-webdev, @michaelpeterswa, @Dannymx, @vpaflah, @zeevo, @chrisweb, @stefangeneralao, @tknickman, @Kikobeats, @ubinatus, @code\-haseeb, @hmmChase, @byhow, @DanielRivers, @wojtekmaj, @paramoshkinandrew, @OMikkel, @theitaliandev, @oliviertassinari, @Ishaan2053, @Sandeep\-Mani, @alyahmedaly, @Lezzio, @devjiwonchoi, @juliusmarminge, @szmazhr, @eddiejaoude, @itz\-Me\-Pj, @AndersDJohnson, @gentamura, @tills13, @dijonmusters, @SaiGanesh21, @vordgi, @ryota\-murakami, @tszhong0411, @officialrajdeepsingh, @alexpuertasr, @AkifumiSato, @Jonas\-PFX, @icyJoseph, @florian\-lp, @pbzona, @erfanium, @remcohaszing, @bernardobelchior, @willashe, @kevinmitch14, @smakosh, @mnjongerius, @asobirov, @theoholl, @suu3, @ArianHamdi, @adrianha, @Sina\-Abf, @kuzeykose, @meenie, @nphmuller, @javivelasco, @belgattitude, @Svetoslav99, @johnslemmer, @colbyfayock, @mehranmf31, @m\-nakamura145, @ryo8000, @aryaemami59, @bestlyg, @jinsoul75, @petrovmiroslav, @nattui, @zhuyedev, @dongwonnn, @nhducit, @flotwig, @Schmavery, @abhinaypandey02, @rvetere, @coffeecupjapan, @cjimmy, @Soheiljafarnejad, @jantimon, @zengspr, @wesbos, @neomad1337, @MaxLeiter, and @devr77 for helping!



## Next.js 14.1 | Next.js

[Read the full article](https://nextjs.org/blog/next-14-1)

[Back to Blog](/blog)Thursday, January 18th 2024

# Next.js 14\.1

Posted by[Jiachi Liu@huozhi](https://twitter.com/huozhi)[Jimmy Lai@feedthejim](https://twitter.com/feedthejim)Next.js 14\.1 includes developer experience improvements including:

* [**Improved Self\-Hosting:**](#improved-self-hosting) New documentation and custom cache handler
* [**Turbopack Improvements:**](#turbopack-improvements) 5,600 tests passing for `next dev --turbo`
* [**DX Improvements:**](#developer-experience-improvements) Improved error messages, `pushState` and `replaceState` support
* [**Parallel \& Intercepted Routes:**](#parallel--intercepted-routes) 20 bug fixes based on your feedback
* [**`next/image` Improvements:**](#nextimage-support-for-picture-and-art-direction) ``, art direction, and dark mode support

Upgrade today or get started with:

Terminal\`\`\`
npx create\-next\-app@latest
\`\`\`
## [Improved Self\-Hosting](#improved-self-hosting)

We've heard your feedback for improved clarity on how to self\-host Next.js with a Node.js server, Docker container, or static export. We've overhauled our self\-hosting documentation on:

* [Runtime environment variables](/docs/app/building-your-application/deploying#environment-variables)
* [Custom cache configuration for ISR](/docs/app/building-your-application/deploying#caching-and-isr)
* [Custom image optimization](/docs/app/building-your-application/deploying#image-optimization)
* [Middleware](/docs/app/building-your-application/deploying#middleware)

With Next.js 14\.1, we've also stabilized providing custom cache handlers for Incremental Static Regeneration and the more granular Data Cache for the App Router:

next.config.js\`\`\`
module.exports = {
 cacheHandler: require.resolve('./cache\-handler.js'),
 cacheMaxMemorySize: 0, // disable default in\-memory caching
};
\`\`\`
Using this configuration when self\-hosting is important when using container orchestration platforms like Kubernetes, where each pod will have a copy of the cache. Using a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application.

For instance, you can save the cached values anywhere, like Redis or Memcached. We'd like to thank [`@neshca`](https://github.com/caching-tools/next-shared-cache) for their [Redis cache handler adapter](https://github.com/vercel/next.js/tree/canary/examples/cache-handler-redis) and example.

## [Turbopack Improvements](#turbopack-improvements)

We're continuing to focus on the reliability and performance of local Next.js development:

* **Reliability:** Turbopack passing the entire Next.js development test suite and dogfooding Vercel's applications
* **Performance:** Improving Turbopack initial compile times and Fast Refresh times
* **Memory Usage:** Improving Turbopack memory usage

We plan to stabilize `next dev --turbo` in an upcoming release with it still being opt\-in.

### [Reliability](#reliability)

Next.js with Turbopack now passes **5,600 development tests (94%)**, 600 more since the last update. You can follow the progress on [areweturboyet.com](https://areweturboyet.com/).

We have continued dogfooding `next dev --turbo` on all Vercel's Next.js applications, including [vercel.com](http://vercel.com) and [v0\.dev](http://v0.dev). All engineers working on these applications are using Turbopack daily.

We've found and fixed a number of issues for very large Next.js applications using Turbopack. For these fixes, we've added new tests to the existing development test suites in Next.js.

### [Performance](#performance)

For `vercel.com`, a large Next.js application, we've seen:

* Up to **76\.7% faster** local server startup
* Up to **96\.3% faster** code updates with Fast Refresh
* Up to **45\.8% faster** initial route compile without caching (Turbopack does not have disk caching yet)

In [v0\.dev](http://v0.dev), we identified an opportunity to optimize the way React Client Components are discovered and bundled in Turbopack \- resulting in **up to 61\.5%** faster initial compile time. This performance improvement was also observed in [vercel.com](http://vercel.com).

### [Future Improvements](#future-improvements)

Turbopack currently has in\-memory caching, which improves incremental compilation times for Fast Refresh.

However, the cache is currently not preserved when restarting the Next.js development server. The next big step for Turbopack performance is **disk caching**, which will allow the cache to be preserved when restating the development server.

## [Developer Experience Improvements](#developer-experience-improvements)

### [Improved Error Messages and Fast Refresh](#improved-error-messages-and-fast-refresh)

We know how critical clear error messages are to your local development experience. We've made a number of fixes to improve the quality of stack traces and error messages you see when running `next dev`.

* Errors that previously displayed bundler errors like `webpack-internal` now properly display the source code of the error and the affected file.
* After seeing an error in a client component, and then fixing the error in your editor, the Fast Refresh did not clear the error screen. It required a hard reload. We've fixed a number of these instances. For example, trying to export `metadata` from a Client Component.

For example, this was a previous error message:



An example of an error from a fetch call in Next.js 14\.

Next.js 14\.1 has improved this to:



Errors from fetch calls during rendering now display the source code of the error and the affected file.

### [`window.history.pushState` and `window.history.replaceState`](#windowhistorypushstate-and-windowhistoryreplacestate)

The App Router now allows the usage of the native [`pushState`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) and [`replaceState`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) methods to update the browser's history stack without reloading the page.

`pushState` and `replaceState` calls integrate into the Next.js App Router, allowing you to sync with [`usePathname`](/docs/app/api-reference/functions/use-pathname) and [`useSearchParams`](/docs/app/api-reference/functions/use-search-params).

This is helpful when needing to immediately update the URL when saving state like filters, sort order, or other information desired to persist across reloads.

\`\`\`
'use client';

import { useSearchParams } from 'next/navigation';

export default function SortProducts() {
 const searchParams = useSearchParams();

 function updateSorting(sortOrder: string) {
 const params = new URLSearchParams(searchParams.toString());
 params.set('sort', sortOrder);
 window.history.pushState(null, '', \`?${params.toString()}\`);
 }

 return (
 \
 \ updateSorting('asc')}\>Sort Ascending\
 \ updateSorting('desc')}\>Sort Descending\
 \
 );
}
\`\`\`
Learn more about using the [native History API](/docs/app/building-your-application/routing/linking-and-navigating#using-the-native-history-api) with Next.js.

### [Data Cache Logging](#data-cache-logging)

For improved observability of your cached data in your Next.js application when running `next dev`, we've made a number of improvements to the `logging` [configuration option](/docs/app/api-reference/next-config-js/logging).

You can now display whether there was a cache `HIT` or `SKIP` and the full URL requested:

Terminal\`\`\`
GET / 200 in 48ms
 ✓ Compiled /fetch\-cache in 117ms
 GET /fetch\-cache 200 in 165ms
 │ GET https://api.vercel.app/products/1 200 in 14ms (cache: HIT)
 ✓ Compiled /fetch\-no\-store in 150ms
 GET /fetch\-no\-store 200 in 548ms
 │ GET https://api.vercel.app/products/1 200 in 345ms (cache: SKIP)
 │ │ Cache missed reason: (cache: no\-store)
\`\`\`
This can be enabled through `next.config.js`:

next.config.js\`\`\`
module.exports = {
 logging: {
 fetches: {
 fullUrl: true,
 },
 },
};
\`\`\`
## [`next/image` support for `` and Art Direction](#nextimage-support-for-picture-and-art-direction)

The Next.js Image component now supports more advanced use cases through `getImageProps()` (stable) which don't require using `` directly. This includes:

* Working with [`background-image`](https://developer.mozilla.org/docs/Web/CSS/background-image) or [`image-set`](https://developer.mozilla.org/docs/Web/CSS/image/image-set)
* Working with canvas [`context.drawImage()`](https://developer.mozilla.org/docs/Web/API/Canvas_API/Tutorial/Using_images) or `new Image()`
* Working with [``](https://developer.mozilla.org/docs/Web/HTML/Element/picture) media queries to implement [Art Direction](https://developer.mozilla.org/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction) or Light/Dark Mode images

\`\`\`
import { getImageProps } from 'next/image';

export default function Page() {
 const common = { alt: 'Hero', width: 800, height: 400 };
 const {
 props: { srcSet: dark },
 } = getImageProps({ ...common, src: '/dark.png' });
 const {
 props: { srcSet: light, ...rest },
 } = getImageProps({ ...common, src: '/light.png' });

 return (
 \
 \
 \
 \
 \
 );
}
\`\`\`
Learn more about [`getImageProps()`](/docs/app/api-reference/components/image#getimageprops).

## [Parallel \& Intercepted Routes](#parallel--intercepted-routes)

In Next.js 14\.1, we've made **20 improvements** to Parallel \& Intercepted Routes.

For the past two releases, we've been focused on improving performance and reliability of Next.js. We've now been able to make many improvements to [Parallel](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) \& [Intercepted Routes](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes) based on your feedback. Notably, we've added support for catch\-all routes and Server Actions.

* **Parallel Routes** allow you to simultaneously or conditionally render one or more pages in the same layout. For highly dynamic sections of an app, such as dashboards and feeds on social sites, Parallel Routes can be used to implement complex routing patterns.
* **Intercepted Routes** allow you to load a route from another part of your application within the current layout. For example, when clicking on a photo in a feed, you can display the photo in a modal, overlaying the feed. In this case, Next.js intercepts the `/photo/123` route, masks the URL, and overlays it over `/feed`.

Learn more about [Parallel](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) \& [Intercepted Routes](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes) or [view an example](https://github.com/vercel/nextgram).

## [Other Improvements](#other-improvements)

Since `14.0`, we've fixed a number of highly upvoted bugs from the community.

We've also recently published videos [explaining caching](https://www.youtube.com/watch?v=VBlSe8tvg4U) and some [common mistakes with the App Router](https://www.youtube.com/watch?v=RBM03RihZVs) that you might find helpful.

* **\[Docs]** New documentation on [Redirecting](https://nextjs.org/docs/app/building-your-application/routing/redirecting)
* **\[Docs]** New documentation on [Testing](https://nextjs.org/docs/app/building-your-application/testing)
* **\[Docs]** New documentation with a [Production Checklist](https://nextjs.org/docs/app/building-your-application/deploying/production-checklist)
* **\[Feature]** Add `` component to `next/third-parties` ([Docs](https://nextjs.org/docs/app/building-your-application/optimizing/third-party-libraries#google-analytics))
* **\[Improvement]** `create-next-app` is now smaller and faster to install ([PR](https://github.com/vercel/next.js/pull/58030))
* **\[Improvement]** Nested routes throwing errors can still be caught be `global-error` ([PR](https://github.com/vercel/next.js/pull/60539))
* **\[Improvement]** `redirect` now respects `basePath` when used in a server action ([PR](https://github.com/vercel/next.js/pull/60184))
* **\[Improvement]** Fix `next/script` and `beforeInteractive` usage with App Router ([PR](https://github.com/vercel/next.js/pull/59779))
* **\[Improvement]** Automatically transpile `@aws-sdk` and `lodash` for faster route startup ([PR](https://github.com/vercel/front/pull/27895))
* **\[Improvement]** Fix flash of unstyled content with `next dev` and `next/font` ([PR](https://github.com/vercel/next.js/pull/60175))
* **\[Improvement]** Propagate `notFound` errors past a segment's error boundary ([PR](https://github.com/vercel/next.js/pull/60567))
* **\[Improvement]** Fix serving public files from locale domains with Pages Router i18n ([PR](https://github.com/vercel/next.js/pull/60749))
* **\[Improvement]** Error if an invalidate `revalidate` value is passed ([PR](https://github.com/vercel/next.js/pull/59822))
* **\[Improvement]** Fix path issues on linux machines when build created on windows ([PR](https://github.com/vercel/next.js/pull/60116))
* **\[Improvement]** Fix Fast Refresh / HMR when using a multi\-zone app with `basePath` ([PR](https://github.com/vercel/next.js/pull/59471))
* **\[Improvement]** Improve graceful shutdown from termination signals ([PR](https://github.com/vercel/next.js/pull/60059))
* **\[Improvement]** Modal routes clash when intercepting from different routes ([PR](https://github.com/vercel/next.js/pull/59861))
* **\[Improvement]** Fix intercepting routes when using `basePath` config ([PR](https://github.com/vercel/next.js/issues/52624))
* **\[Improvement]** Show warning when a missing parallel slot results in 404 ([PR](https://github.com/vercel/next.js/pull/60186))
* **\[Improvement]** Improve intercepted routes when used with catch\-all routes ([PR](https://github.com/vercel/next.js/issues/59784))
* **\[Improvement]** Improve intercepted routes when used with `revalidatePath` ([PR](https://github.com/vercel/next.js/issues/54173))
* **\[Improvement]** Fix usage of `@children` slots with parallel routes ([PR](https://github.com/vercel/next.js/pull/60288))
* **\[Improvement]** Fix Fix TypeError when using params with parallel routes ([PR](https://github.com/vercel/next.js/issues/59711))
* **\[Improvement]** Fix catch\-all route normalization for default parallel routes ([PR](https://github.com/vercel/next.js/pull/60240))
* **\[Improvement]** Fix display of parallel routes in the `next build` summary ([PR](https://github.com/vercel/next.js/issues/59775))
* **\[Improvement]** Fix for route parameters when using intercepted routes ([PR](https://github.com/vercel/next.js/issues/59782))
* **\[Improvement]** Improve deeply nested parallel/intercepted routes ([PR](https://github.com/vercel/next.js/issues/58660))
* **\[Improvement]** Fix 404 with intercepted routes paired with route groups ([PR](https://github.com/vercel/next.js/pull/59752))
* **\[Improvement]** Fix parallel routes with server actions / revalidating router cache ([PR](https://github.com/vercel/next.js/pull/59585))
* **\[Improvement]** Fix usage of `rewrites` with an intercepted route ([PR](https://github.com/vercel/next.js/pull/59168))
* **\[Improvement]** Server Actions now work from third\-party libraries ([PR](https://github.com/vercel/next.js/pull/59569))
* **\[Improvement]** Next.js can now be used within an ESM package ([PR](https://github.com/vercel/next.js/pull/59852))
* **\[Improvement]** Barrel file optimizations for libraries like Material UI ([PR](https://github.com/vercel/next.js/issues/59804))
* **\[Improvement]** Builds will now fail on incorrect usage of `useSearchParams` without `Suspense` ([PR](https://github.com/vercel/next.js/pull/60840))

## [Contributors](#contributors)

Next.js is the result of the combined work of over 3,000 individual developers, industry partners like Google and Meta, and our core team at Vercel. Join the community on [GitHub Discussions](https://github.com/vercel/next.js/discussions), [Reddit](https://www.reddit.com/r/nextjs/), and [Discord](https://nextjs.org/discord).

This release was brought to you by:

* The **Next.js** team: [Andrew](https://github.com/acdlite), [Balazs](https://github.com/balazsorban44), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Sebastian](https://github.com/sebmarkbage), [Shu](https://github.com/shuding), [Steven](https://github.com/styfle), [Tim](https://github.com/timneutkens), [Wyatt](https://github.com/wyattjoh), and [Zack](https://github.com/ztanner).
* The **Turbopack** team: [Donny](https://github.com/kdy1), [Leah](https://github.com/forsakenharmony), [Maia](https://github.com/padmaia), [OJ](https://github.com/kwonoj), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
* **Next.js Docs**: [Delba](https://github.com/delbaoliveira), [Steph](https://github.com/StephDietz), [Michael](https://github.com/manovotny), and [Lee](https://github.com/leerob).

And the contributions of: @OlehDutchenko, @eps1lon, @ebidel, @janicklas\-ralph, @JohnPhamous, @chentsulin, @akawalsky, @BlankParticle, @dvoytenko, @smaeda\-ks, @kenji\-webdev, @rv\-david, @icyJoseph, @dijonmusters, @A7med3bdulBaset, @jenewland1999, @mknichel, @kdy1, @housseindjirdeh, @max\-programming, @redbmk, @SSakibHossain10, @jamesmillerburgess, @minaelee, @officialrajdeepsingh, @LorisSigrist, @yesl\-kim, @StevenKamwaza, @manovotny, @mcexit, @remcohaszing, @ryo\-manba, @TranquilMarmot, @vinaykulk621, @haritssr, @divquan, @IgorVaryvoda, @LukeSchlangen, @RiskyMH, @ash2048, @ManuWeb3, @msgadi, @dhayab, @ShahriarKh, @jvandenaardweg, @DestroyerXyz, @SwitchBladeAK, @ianmacartney, @justinh00k, @tiborsaas, @ArianHamdi, @li\-jia\-nan, @aramikuto, @jquinc30, @samcx, @Haosik, @AkifumiSato, @arnabsen, @nfroidure, @clbn, @siddtheone, @zbauman3, @anthonyshew, @alexfradiani, @CalebBarnes, @adk96r, @pacexy, @hichemfantar, @michaldudak, @redonkulus, @k\-taro56, @mhughdo, @tknickman, @shumakmanohar, @vordgi, @hamirmahal, @gaspar09, @JCharante, @sjoerdvanBommel, @mass2527, @N\-Ziermann, @tordans, @davidthorand, @rmathew8\-gh, @chriskrogh, @shogunsea, @auipga, @SukkaW, @agustints, @OXXD, @clarencepenz, @better\-salmon, @808vita, @coltonehrman, @tksst, @hugo\-syn, @JakobJingleheimer, @Willem\-Jaap, @brandonnorsworthy, @jaehunn, @jridgewell, @gtjamesa, @mugi\-uno, @kentobento, @vivianyentran, @empflow, @samennis1, @mkcy3, @suhaotian, @imevanc, @d3lm, @amannn, @hallatore, @Dylan700, @mpsq, @mdio, @christianvuerings, @karlhorky, @simonhaenisch, @olci34, @zce, @LavaToaster, @rishabhpoddar, @jirihofman, @codercor, @devjiwonchoi, @JackieLi565, @thoushif, @pkellner, @jpfifer, @quisido, @tomfa, @raphaelbadia, @j9141997, @hongaar, @MadCcc, @luismulinari, @dumb\-programmer, @nonoakij, @franky47, @robbertstevens, @bryndyment, @marcosmartini, @functino, @Anisi, @AdonisAgelis, @seangray\-dev, @prkagrawal, @heloineto, @kn327, @ihommani, @MrNiceRicee, @falsepopsky, @thomasballinger, @tmilewski, @Vadman97, @dnhn, @RodrigoTomeES, @sadikkuzu, @gffuma, @Schniz, @joulev, @Athrun\-Judah, @rasvanjaya21, @rashidul0405, @nguyenbry, @Mwimwii, @molebox, @mrr11k, @philwolstenholme, @IgorKowalczyk, @Zoe\-Bot, @HanCiHu, @JackHowa, @goncy, @hirotomoyamada, @pveyes, @yeskunall, @ChendayUP, @hmaesta, @ajz003, @its\-kunal, @joelhooks, @blurrah, @tariknh, @Vinlock, @Nayeem\-XTREME, @aziyatali, @aspehler, and @moka\-ayumu.



