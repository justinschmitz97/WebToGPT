# https://blog.vuejs.org/

## Announcing Vue 3.3 | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-3)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)
Today we're excited to announce the release of Vue 3\.3 "Rurouni Kenshin"!

This release is focused on developer experience improvements \- in particular, SFC `` usage with TypeScript. Together with the 1\.6 release of [Vue Language Tools](https://github.com/vuejs/language-tools/) (previously known as Volar), we have resolved many long\-standing pain points when using Vue with TypeScript.

This post provides an overview of the highlighted features in 3\.3\. For the full list of changes, please consult [the full changelog on GitHub](https://github.com/vuejs/core/blob/main/CHANGELOG.md#330-2023-05-08).

---

Dependency Updates

When upgrading to 3\.3, it is recommended to also update the following dependencies:

* volar / vue\-tsc@^1\.6\.4
* vite@^4\.3\.5
* @vitejs/plugin\-vue@^4\.2\.0
* vue\-loader@^17\.1\.0 (if using webpack or vue\-cli)
## `` \+ TypeScript DX Improvements [​](#script-setup-typescript-dx-improvements)

### Imported and Complex Types Support in Macros [​](#imported-and-complex-types-support-in-macros)

Previously, types used in the type parameter position of `defineProps` and `defineEmits` were limited to local types, and only supported type literals and interfaces. This is because Vue needs to be able to analyze the properties on the props interface in order to generate corresponding runtime options.

This limitation is now resolved in 3\.3\. The compiler can now resolve imported types, and supports a limited set of complex types:

vue\`\`\`
\
import type { Props } from './foo'

// imported \+ intersection type
defineProps\()
\
\`\`\`Do note that complex types support is AST\-based and therefore not 100% comprehensive. Some complex types that require actual type analysis, e.g. conditional types, are not supported. You can use conditional types for the type of a single prop, but not the entire props object.

* Details: [PR\#8083](https://github.com/vuejs/core/pull/8083)

### Generic Components [​](#generic-components)

Components using `` can now accept generic type parameters via the `generic` attribute:

vue\`\`\`
\
defineProps\()
\
\`\`\`The value of `generic` works exactly the same as the parameter list between `` in TypeScript. For example, you can use multiple parameters, `extends` constraints, default types, and reference imported types:

vue\`\`\`
\
import type { Item } from './types'
defineProps\()
\
\`\`\`This feature previously required explicit opt\-in, but is now enabled by default in the latest version of volar / vue\-tsc.

* Discussion: [RFC\#436](https://github.com/vuejs/rfcs/discussions/436)
* Related: [generic `defineComponent()` \- PR\#7963](https://github.com/vuejs/core/pull/7963)

### More Ergonomic `defineEmits` [​](#more-ergonomic-defineemits)

Previously, the type parameter for `defineEmits` only supports the call signature syntax:

ts\`\`\`
// BEFORE
const emit = defineEmits\()
\`\`\`The type matches the return type for `emit`, but is a bit verbose and awkward to write. 3\.3 introduces a more ergonomic way of declaring emits with types:

ts\`\`\`
// AFTER
const emit = defineEmits\()
\`\`\`In the type literal, the key is the event name and the value is an array type specifying the additional arguments. Although not required, you can use the [labeled tuple elements](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-0.html#labeled-tuple-elements) for explicitness, like in the example above.

The call signature syntax is still supported.

### Typed Slots with `defineSlots` [​](#typed-slots-with-defineslots)

The new `defineSlots` macro can be used to declare expected slots and their respective expected slot props:

vue\`\`\`
\
defineSlots\ any
 item?: (props: { id: number }) =\> any
}\>()
\
\`\`\``defineSlots()` only accepts a type parameter and no runtime arguments. The type parameter should be a type literal where the property key is the slot name, and the value is a slot function. The first argument of the function is the props the slot expects to receive, and its type will be used for slot props in the template. The returning value of `defineSlots` is the same slots object returned from `useSlots`.

Some current limitations:

* Required slots checking is not yet implemented in volar / vue\-tsc.
* Slot function return type is currently ignored and can be `any`, but we may leverage it for slot content checking in the future.

There is also a corresponding `slots` option for `defineComponent` usage. Both APIs have no runtime implications and serve purely as type hints for IDEs and `vue-tsc`.

* Details: [PR\#7982](https://github.com/vuejs/core/issues/7982)

## Experimental Features [​](#experimental-features)

### Reactive Props Destructure [​](#reactive-props-destructure)

Previously part of the now\-dropped Reactivity Transform, reactive props destructure has been split into a separate feature.

The feature allows destructured props to retain reactivity, and provides a more ergonomic way to declare props default values:

vue\`\`\`
\
import { watchEffect } from 'vue'

const { msg = 'hello' } = defineProps(\['msg'])

watchEffect(() =\> {
 // accessing \`msg\` in watchers and computed getters
 // tracks it as a dependency, just like accessing \`props.msg\`
 console.log(\`msg is: ${msg}\`)
})
\

\{{ msg }}\
\`\`\`This feature is experimental and requires explicit opt\-in.

* Details: [RFC\#502](https://github.com/vuejs/rfcs/discussions/502)

### `defineModel` [​](#definemodel)

Previously, for a component to support two\-way binding with `v-model`, it needs to (1\) declare a prop and (2\) emit a corresponding `update:propName` event when it intends to update the prop:

vue\`\`\`
\
\
const props = defineProps(\['modelValue'])
const emit = defineEmits(\['update:modelValue'])
console.log(props.modelValue)

function onInput(e) {
 emit('update:modelValue', e.target.value)
}
\

\
 \
\
\`\`\`3\.3 simplifies the usage with the new `defineModel` macro. The macro automatically registers a prop, and returns a ref that can be directly mutated:

vue\`\`\`
\
\
const modelValue = defineModel()
console.log(modelValue.value)
\

\
 \
\
\`\`\`This feature is experimental and requires explicit opt\-in.

* Details: [RFC\#503](https://github.com/vuejs/rfcs/discussions/503)

## Other Notable Features [​](#other-notable-features)

### `defineOptions` [​](#defineoptions)

The new `defineOptions` macro allows declaring component options directly in ``, without requiring a separate `` block:

vue\`\`\`
\
defineOptions({ inheritAttrs: false })
\
\`\`\`### Better Getter Support with `toRef` and `toValue` [​](#better-getter-support-with-toref-and-tovalue)

`toRef` has been enhanced to support normalizing values / getters / existing refs into refs:

js\`\`\`
// equivalent to ref(1\)
toRef(1\)
// creates a readonly ref that calls the getter on .value access
toRef(() =\> props.foo)
// returns existing refs as\-is
toRef(existingRef)
\`\`\`Calling `toRef` with a getter is similar to `computed`, but can be more efficient when the getter is just performing property access with no expensive computations.

The new `toValue` utility method provides the opposite, normalizing values / getters / refs into values:

js\`\`\`
toValue(1\) // \-\-\> 1
toValue(ref(1\)) // \-\-\> 1
toValue(() =\> 1\) // \-\-\> 1
\`\`\``toValue` can be used in composables in place of `unref` so that your composable can accept getters as reactive data sources:

js\`\`\`
// before: allocating unnecessary intermediate refs
useFeature(computed(() =\> props.foo))
useFeature(toRef(props, 'foo'))

// after: more efficient and succinct
useFeature(() =\> props.foo)
\`\`\`The relationship between `toRef` and `toValue` is similar to that between `ref` and `unref`, with the main difference being the special handling of getter functions.

* Details: [PR\#7997](https://github.com/vuejs/core/pull/7997)

### JSX Import Source Support [​](#jsx-import-source-support)

Currently, Vue's types automatically registers global JSX typing. This may cause conflict with used together with other libraries that needs JSX type inference, in particular React.

Starting in 3\.3, Vue supports specifying JSX namespace via TypeScript's [jsxImportSource](https://www.typescriptlang.org/tsconfig#jsxImportSource) option. This allows the users to choose global or per\-file opt\-in based on their use case.

For backwards compatibility, 3\.3 still registers JSX namespace globally. **We plan to remove the default global registration in 3\.4\.** If you are using TSX with Vue, you should add explicit `jsxImportSource` to your `tsconfig.json` after upgrading to 3\.3 to avoid breakage in 3\.4\.

## Maintenance Infrastructure Improvements [​](#maintenance-infrastructure-improvements)

This release builds upon many maintenance infrastructure improvements that allow us to move faster with more confidence:

* 10x faster builds by separating type checking from the rollup build and moving from `rollup-plugin-typescript2` to `rollup-plugin-esbuild`.
* Faster tests by moving from Jest to [Vitest](https://vitest.dev).
* Faster types generation by moving from `@microsoft/api-extractor` to `rollup-plugin-dts`.
* Comprehensive regression tests via [ecosystem\-ci](https://github.com/vuejs/ecosystem-ci) \- catches regressions in major ecosystem dependents before releases!

As planned, we aim to start making smaller and more frequent feature releases in 2023\. Stay tuned!



## Announcing Vue 3.0 "One Piece" | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-one-piece)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)


Today we are proud to announce the official release of Vue.js 3\.0 "One Piece". This new major version of the framework provides improved performance, smaller bundle sizes, better TypeScript integration, new APIs for tackling large scale use cases, and a solid foundation for long\-term future iterations of the framework.

---

The 3\.0 release represents over 2 years of development efforts, featuring [30\+ RFCs](https://github.com/vuejs/rfcs/tree/master/active-rfcs), 2,600\+ commits, [628 pull requests](https://github.com/vuejs/vue-next/pulls?q=is%3Apr+is%3Amerged+-author%3Aapp%2Fdependabot-preview+) from [99 contributors](https://github.com/vuejs/vue-next/graphs/contributors), plus tremendous amount of development and documentation work outside of the core repo. We would like to express our deepest gratitude towards our team members for taking on this challenge, our contributors for the pull requests, our [sponsors and backers](https://github.com/vuejs/vue/blob/dev/BACKERS.md) for the financial support, and the wider community for participating in our design discussions and providing feedback for the pre\-release versions. Vue is an independent project created for the community and sustained by the community, and Vue 3\.0 wouldn't have been possible without your consistent support.

## Taking the "Progressive Framework" Concept Further [​](#taking-the-progressive-framework-concept-further)

Vue had a simple mission from its humble beginning: to be an approachable framework that anyone can quickly learn. As our user base grew, the framework also grew in scope to adapt to the increasing demands. Over time, it evolved into what we call a "Progressive Framework": a framework that can be learned and adopted incrementally, while providing continued support as the user tackles more and more demanding scenarios.

Today, with over 1\.3 million users worldwide\*, we are seeing Vue being used in a wildly diverse range of scenarios, from sprinkling interactivity on traditional server\-rendered pages, to full\-blown single page applications with hundreds of components. Vue 3 takes this flexibility even further.

### Layered internal modules [​](#layered-internal-modules)

Vue 3\.0 core can still be used via a simple `` tag, but its internals has been re\-written from the ground up into [a collection of decoupled modules](https://github.com/vuejs/vue-next/tree/master/packages). The new architecture provides better maintainability, and allows end users to shave off up to half of the runtime size via tree\-shaking.

These modules also exposes lower\-level APIs that unlocks many advanced use cases:

* The compiler supports custom AST transforms for build\-time customizations (e.g. [build\-time i18n](https://github.com/intlify/vue-i18n-extensions))
* The core runtime provides first\-class API for creating custom renderers targeting different render targets (e.g. [native mobile](https://github.com/rigor789/nativescript-vue-next), [WebGL](https://github.com/Planning-nl/vugel) or [terminals](https://github.com/ycmjason/vuminal)). The default DOM renderer is built using the same API.
* The [`@vue/reactivity` module](https://github.com/vuejs/vue-next/tree/master/packages/reactivity) exports functions that provide direct access to Vue's reactivity system, and can be used as a standalone package. It can be used to pair with other templating solutions (e.g. [lit\-html](https://github.com/yyx990803/vue-lit)) or even in non\-UI scenarios.

### New APIs for tackling scale [​](#new-apis-for-tackling-scale)

The 2\.x Object\-based API is largely intact in Vue 3\. However, 3\.0 also introduces the [Composition API](https://v3.vuejs.org/guide/composition-api-introduction.html) \- a new set of APIs aimed at addressing the pain points of Vue usage in large scale applications. The Composition API builds on top of the reactivity API and enables logic composition and reuse similar to React hooks, more flexible code organization patterns, and more reliable type inference than the 2\.x Object\-based API.

Composition API can also be used with Vue 2\.x via the [@vue/composition\-api](https://github.com/vuejs/composition-api) plugin, and there are already Composition API utility libraries that work for both Vue 2 and 3 (e.g. [vueuse](https://github.com/antfu/vueuse), [vue\-composable](https://github.com/pikax/vue-composable)).

### Performance Improvements [​](#performance-improvements)

Vue 3 has demonstrated [significant performance improvements](https://docs.google.com/spreadsheets/d/1VJFx-kQ4KjJmnpDXIEaig-cVAAJtpIGLZNbv3Lr4CR0/edit?usp=sharing) over Vue 2 in terms of bundle size (up to 41% lighter with tree\-shaking), initial render (up to 55% faster), updates (up to 133% faster), and memory usage (up to 54% less).

In Vue 3, we have taken the approach of "compiler\-informed Virtual DOM": the template compiler performs aggressive optimizations and generates render function code that hoists static content, leaves runtime hints for binding types, and most importantly, flattens the dynamic nodes inside a template to reduce the cost of runtime traversal. The user therefore gets the best of both worlds: compiler\-optimized performance from templates, or direct control via manual render functions when the use case demands.

### Improved TypeScript integration [​](#improved-typescript-integration)

Vue 3's codebase is written in TypeScript, with automatically generated, tested, and bundled type definitions so they are always up\-to\-date. Composition API works great with type inference. Vetur, our official VSCode extension, now supports template expression and props type checking leveraging Vue 3's improved internal typing. Oh, and Vue 3's typing [fully supports TSX](https://github.com/vuejs/vue-next/blob/master/test-dts/defineComponent.test-d.tsx) if that's your preference.

### Experimental Features [​](#experimental-features)

We have proposed [two new features](https://github.com/vuejs/rfcs/pull/182) for Singe\-File Components (SFC, aka `.vue` files):

* [``: syntactic sugar for using Composition API inside SFCs](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-script-setup.md)
* [``: state\-driven CSS variables inside SFCs](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-style-variables.md)

These features are already implemented and available in Vue 3\.0, but are provided only for the purpose of gathering feedback. They will remain experimental until the RFCs are merged.

We have also implemented a currently undocumented `` component, which allows waiting on nested async dependencies (async components or component with `async setup()`) on initial render or branch switch. We are testing and iterating on this feature with the Nuxt.js team ([Nuxt 3 is on the way](https://nuxtjs.slides.com/atinux/state-of-nuxt-2020)) and will likely solidify it in 3\.1\.

## Phased Release Process [​](#phased-release-process)

The release of Vue 3\.0 marks the general readiness of the framework. While some of the frameworks sub projects may still need further work to reach stable status (specifically router and Vuex integration in the devtools), we believe it's suitable to start new, green\-field projects with Vue 3 today. We also encourage library authors to start upgrading your projects to support Vue 3\.

Check out the [Vue 3 Libraries Guide](https://v3-migration.vuejs.org/recommendations.html) for details on all framework sub projects.

### Migration and IE11 Support [​](#migration-and-ie11-support)

We have pushed back the migration build (v3 build with v2 compatible behavior \+ migration warnings) and the IE11 build due to time constraints, and are aiming to focus on them in Q4 2020\. Therefore, users planning to migrate an existing v2 app or require IE11 support should be aware of these limitations at this time.

### Next Steps [​](#next-steps)

For the near term after release, we will focus on:

* Migration build
* IE11 support
* Router and Vuex integration in new devtools
* Further improvements to template type inference in Vetur

For the time being, the documentation websites, GitHub branches, and npm dist tags for Vue 3 and v3\-targeting projects will remain under `next`\-denoted status. This means `npm install vue` will still install Vue 2\.x and `npm install vue@next` will install Vue 3\. **We are planning to switch all doc links, branches and dist tags to default to 3\.0 in early 2021\.**

At the same time, we have started planning for 2\.7, which will be the last planned minor release of the 2\.x release line. 2\.7 will be backporting compatible improvements from v3, and emit warnings on usage of APIs that are removed/changed in v3 to help with potential migration. We are planning to work on 2\.7 in Q1 2021, which will directly become LTS upon release with an 18 months maintenance lifespan.

## Trying It Out [​](#trying-it-out)

To learn more about Vue 3\.0, check out our [new documentation website](https://v3.vuejs.org/). If you are an existing Vue 2\.x user, go directly to the [Migration Guide](https://v3.vuejs.org/guide/migration/introduction.html).

---

* \*based on [Vue Devtools Chrome extension](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) weekly active users as reported by Google.


## Announcing Vue 3.4 | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-4)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)
Today we're excited to announce the release of Vue 3\.4 "🏀 Slam Dunk"!

This release includes some substantial internal improvements \- most notably a rewritten template parser that is 2x faster, and a refactored reactivity system that makes effect triggering more accurate and efficient. It also packs a number of quality\-of\-life API improvements, including the stabilization of `defineModel` and a new same\-name shorthand when binding props.

This post provides an overview of the highlighted features in 3\.4\. For the full list of changes, please consult [the full changelog on GitHub](https://github.com/vuejs/core/blob/main/CHANGELOG.md#340-2023-12-28).

---

## Potential Actions Needed [​](#potential-actions-needed)

1. To fully leverage new features in 3\.4, it is recommended to also update the following dependencies when upgrading to 3\.4:

	* Volar / vue\-tsc@^1\.8\.27 (**required**)
	* @vitejs/plugin\-vue@^5\.0\.0 (if using Vite)
	* nuxt@^3\.9\.0 (if using Nuxt)
	* vue\-loader@^17\.4\.0 (if using webpack or vue\-cli)
2. If using TSX with Vue, check actions needed in [Removed: Global JSX Namespace](#removed-global-jsx-namespace).
3. Make sure you are no longer using any deprecated features (if you are, you should have warnings in the console telling you so). They may have been [removed in 3\.4](#other-removed-features).

## Feature Highlights [​](#feature-highlights)

### 2X Faster Parser and Improved SFC Build Performance [​](#_2x-faster-parser-and-improved-sfc-build-performance)

* Context: [PR\#9674](https://github.com/vuejs/core/pull/9674)

In 3\.4, we completely rewrote the template parser. Previously, Vue used a recursive descent parser that relied on many regular expressions and look\-ahead searches. The new parser uses a state\-machine tokenizer based on the tokenizer in [htmlparser2](https://github.com/fb55/htmlparser2), which iterates through the entire template string only once. The result is a parser that is consistently twice as fast for templates of all sizes. Thanks to our extensive test cases and [ecosystem\-ci](https://github.com/vuejs/ecosystem-ci), it is also 100% backwards compatible for Vue end users.

While integrating the new parser with other parts of the system, we also discovered a few opportunities to further improve the overall SFC compilation performance. The benchmarks show a \~44% improvement when compiling the script and template parts of a Vue SFC while generating source maps, so 3\.4 should result in faster builds for most projects using Vue SFCs. However, do note that Vue SFC compilation is only one part of the entire build process in real world projects. The final gain in end\-to\-end build time will likely be much smaller compared to the isolated benchmarks.

Outside of Vue core, the new parser will also benefit the performance of Volar / vue\-tsc, and community plugins that need to parse Vue SFCs or templates, e.g. Vue Macros.

### More Efficient Reactivity System [​](#more-efficient-reactivity-system)

**Context: [PR\#5912](https://github.com/vuejs/core/pull/5912)**

3\.4 also ships a substantial refactor of the reactivity system, with the goal of improving re\-compute efficiency of computed properties.

To illustrate what is being improved, let's consider the following scenario:

js\`\`\`
const count = ref(0\)
const isEven = computed(() =\> count.value % 2 === 0\)

watchEffect(() =\> console.log(isEven.value)) // logs true

count.value = 2 // logs true again
\`\`\`Before 3\.4, the callback of `watchEffect` will fire every time `count.value` is changed, even if the computed result remains the same. With the post\-3\.4 optimizations, the callback now only fires if the computed result has actually changed.

In addition, in 3\.4:

* Multiple computed dep changes only trigger sync effects once.
* Array `shift`, `unshift`, `splice` methods only trigger sync effects once.

In addition to the gains shown in the [benchmarks](https://github.com/vuejs/core/pull/5912#issuecomment-1748985641), this should reduce unnecessary component re\-renders in many scenarios while retaining full backwards compatibility.

### `defineModel` is Now Stable [​](#definemodel-is-now-stable)

**Context: [RFC\#503](https://github.com/vuejs/rfcs/discussions/503)**

`defineModel` is a new `` macro that aims to simplify the implementation of components that support `v-model`. It was previously shipped in 3\.3 as an experimental feature, and has graduated to stable status in 3\.4\. It now also provides better support for usage with `v-model` modifiers.

Relevant Documentation:

* [Revised Component v\-model section](https://vuejs.org/guide/components/v-model.html)
* [defineModel API reference](https://vuejs.org/api/sfc-script-setup.html#definemodel)

### `v-bind` Same\-name Shorthand [​](#v-bind-same-name-shorthand)

**Context: [PR\#9451](https://github.com/vuejs/core/pull/9451)**

You can now shorten this:

template\`\`\`
\
\`\`\`To this:

template\`\`\`
\
\`\`\`This feature has been frequently requested in the past. Originally, we had concerns about its usage being confused with boolean attributes. However, after revisiting the feature, we now think it makes sense for `v-bind` to behave a bit more like JavaScript than native attributes, considering its dynamic nature.

### Improved Hydration Mismatch Errors [​](#improved-hydration-mismatch-errors)

**Context: [PR\#5953](https://github.com/vuejs/core/pull/5953)**

3\.4 ships a number of improvements to hydration mismatch error messages:

1. Improved clarity of the wording (rendered by server vs. expected on client).
2. The message now includes the DOM node in question so you can quickly locate it on the page or in the elements panel.
3. Hydration mismatch checks now also apply to class, style, and other dynamically bound attributes.

In addition, 3\.4 also adds a new compile\-time flag, [`__VUE_PROD_HYDRATION_MISMATCH_DETAILS__`](https://vuejs.org/api/compile-time-flags.html#vue-prod-hydration-mismatch-details), which can be used to force hydration mismatch errors to include full details even in production.

### Error Code and Compile\-time Flag Reference [​](#error-code-and-compile-time-flag-reference)

To reduce bundle size, Vue drops long error message strings in production builds. However, this means errors caught by error handlers in production will receive short error codes that are difficult to decipher without diving into Vue's source code.

To improve this, we have added a [Production Error Reference Page](https://vuejs.org/error-reference/) to the documentation. The error codes are automatically generated from the latest version of Vue stable release.

We have also added a [Compile\-Time Flags Reference](https://vuejs.org/api/compile-time-flags.html) with instructions on how to configure these flags for different build tools.

## Removed Deprecated Features [​](#removed-deprecated-features)

### Global JSX Namespace [​](#global-jsx-namespace)

Starting in 3\.4, Vue no longer registers the global `JSX` namespace by default. This is necessary to avoid global namespace collision with React so that TSX of both libs can co\-exist in the same project. This should not affect SFC\-only users with latest version of Volar.

If you are using TSX, there are two options:

1. Explicitly set [jsxImportSource](https://www.typescriptlang.org/tsconfig#jsxImportSource) to `'vue'` in `tsconfig.json` before upgrading to 3\.4\. You can also opt\-in per file by adding a `/* @jsxImportSource vue */` comment at the top of the file.
2. If you have code that depends on the presence of the global `JSX` namespace, e.g. usage of types like `JSX.Element` etc., you can retain the exact pre\-3\.4 global behavior by explicitly referencing `vue/jsx`, which registers the global `JSX` namespace.

Note that this is a type\-only breaking change in a minor release, which adheres to our [release policy](https://vuejs.org/about/releases.html#semantic-versioning-edge-cases).

### Other Removed Features [​](#other-removed-features)

* [Reactivity Transform](https://vuejs.org/guide/extras/reactivity-transform.html) was marked deprecated in 3\.3 and is now removed in 3\.4\. This change does not require a major due to the feature being experimental. Users who wish to continue using the feature can do so via the [Vue Macros plugin](https://vue-macros.dev/features/reactivity-transform.html).
* `app.config.unwrapInjectedRef` has been removed. It was deprecated and enabled by default in 3\.3\. In 3\.4 it is no longer possible to disable this behavior.
* `@vnodeXXX` event listeners in templates are now a compiler error instead of a deprecation warning. Use `@vue:XXX` listeners instead.
* `v-is` directive has been removed. It was deprecated in 3\.3\. Use the [`is` attribute with `vue:` prefix](https://vuejs.org/api/built-in-special-attributes.html#is) instead.


## Announcing Vue 3.5 | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-5)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)
Today we are excited to announce the release of Vue 3\.5 "Tengen Toppa Gurren Lagann"!

This minor release contains no breaking changes and includes both internal improvements and useful new features. We will cover some highlights in this blog post \- for a full list of changes and new features, please consult [the full changelog on GitHub](https://github.com/vuejs/core/blob/main/CHANGELOG.md).

---

## Reactivity System Optimizations [​](#reactivity-system-optimizations)

In 3\.5, Vue's reactivity system has undergone another major refactor that achieves better performance and significantly improved memory usage (**\-56%**) with no behavior changes. The refactor also resolves stale computed values and memory issues caused by hanging computeds during SSR.

In addition, 3\.5 also optimizes reactivity tracking for large, deeply reactive arrays, making such operations up to 10x faster in some cases.

**Details: [PR\#10397](https://github.com/vuejs/core/pull/10397), [PR\#9511](https://github.com/vuejs/core/pull/9511)**

## Reactive Props Destructure [​](#reactive-props-destructure)

**Reactive Props Destructure** has been stabilized in 3\.5\. With the feature now enabled by default, variables destructured from a `defineProps` call in `` are now reactive. Notably, this feature significantly simplifies declaring props with default values by leveraging JavaScript's native default value syntax:

**Before**

ts\`\`\`
const props = withDefaults(
 defineProps\(),
 {
 count: 0,
 msg: 'hello'
 }
)
\`\`\`**After**

ts\`\`\`
const { count = 0, msg = 'hello' } = defineProps\()
\`\`\`Access to a destructured variable, e.g. `count`, is automatically compiled into `props.count` by the compiler, so they are tracked on access. Similar to `props.count`, watching the destructured prop variable or passing it into a composable while retaining reactivity requires wrapping it in a getter:

js\`\`\`
watch(count /\* ... \*/)
// ^ results in compile\-time error

watch(() =\> count /\* ... \*/)
// ^ wrap in a getter, works as expected

// composables should normalize the input with \`toValue()\`
useDynamicCount(() =\> count)
\`\`\`For those who prefer to better distinguish destructured props from normal variables, `@vue/language-tools` 2\.1 has shipped an opt\-in setting to enable inlay hints for them:

Details:

* See [docs](https://vuejs.org/guide/components/props.html#reactive-props-destructure) for usage and caveats.
* See [RFC\#502](https://github.com/vuejs/rfcs/discussions/502) for the history and design rationale behind this feature.

## SSR Improvements [​](#ssr-improvements)

3\.5 brings a few long\-requested improvements to server\-side rendering (SSR).

### Lazy Hydration [​](#lazy-hydration)

Async components can now control when they should be hydrated by specifying a strategy via the `hydrate` option of the `defineAsyncComponent()` API. For example, to only hydrate a component when it becomes visible:

js\`\`\`
import { defineAsyncComponent, hydrateOnVisible } from 'vue'

const AsyncComp = defineAsyncComponent({
 loader: () =\> import('./Comp.vue'),
 hydrate: hydrateOnVisible()
})
\`\`\`The core API is intentionally lower level and the Nuxt team is already building higher\-level syntax sugar on top of this feature.

**Details: [PR\#11458](https://github.com/vuejs/core/pull/11458)**

### `useId()` [​](#useid)

`useId()` is an API that can be used to generate unique\-per\-application IDs that are guaranteed to be stable across the server and client renders. They can be used to generate IDs for form elements and accessibility attributes, and can be used in SSR applications without leading to hydration mismatches:

vue\`\`\`
\
import { useId } from 'vue'

const id = useId()
\

\
 \
 \Name:\
 \
 \
\
\`\`\`**Details: [PR\#11404](https://github.com/vuejs/core/pull/11404)**

### `data-allow-mismatch` [​](#data-allow-mismatch)

In cases where a client value will be inevitably different from its server counterpart (e.g. dates), we can now suppress the resulting hydration mismatch warnings with `data-allow-mismatch` attributes:

vue\`\`\`
\{{ data.toLocaleString() }}\
\`\`\`You can also limit what types of mismatches are allowed by providing a value to the attribute, where the possible values are `text`, `children`, `class`, `style`, and `attribute`.

## Custom Elements Improvements [​](#custom-elements-improvements)

3\.5 fixes many long\-standing issues related to the `defineCustomElement()` API, and adds a number of new capabilities for authoring custom elements with Vue:

* Support app configurations for custom elements via the `configureApp` option.
* Add `useHost()`, `useShadowRoot()`, and `this.$host` APIs for accessing the host element and shadow root of a custom element.
* Support mounting custom elements without Shadow DOM by passing `shadowRoot: false`.
* Support providing a `nonce` option, which will be attached to `` tags injected by custom elements.

These new custom\-element\-only options can be passed to `defineCustomElement` via a second argument:

js\`\`\`
import MyElement from './MyElement.ce.vue'

defineCustomElements(MyElement, {
 shadowRoot: false,
 nonce: 'xxx',
 configureApp(app) {
 app.config.errorHandler = ...
 }
})
\`\`\`## Other Notable Features [​](#other-notable-features)

### `useTemplateRef()` [​](#usetemplateref)

3\.5 introduces a new way of obtaining [Template Refs](https://vuejs.org/guide/essentials/template-refs.html) via the `useTemplateRef()` API:

vue\`\`\`
\
import { useTemplateRef } from 'vue'

const inputRef = useTemplateRef('input')
\

\
 \
\
\`\`\`Prior to 3\.5, we recommended using plain refs with variable names matching static `ref` attributes. The old approach required the `ref` attributes to be analyzable by the compiler and thus was limited to static `ref` attributes. In comparison, `useTemplateRef()` matches the refs via runtime string IDs, therefore supporting dynamic ref bindings to changing IDs.

`@vue/language-tools` 2\.1 has also implemented [special support for the new syntax](https://github.com/vuejs/language-tools/pull/4644), so you will get auto\-completion and warnings when using `useTemplateRef()` based on presence of `ref` attributes in your template:

### Deferred Teleport [​](#deferred-teleport)

A known constraint of the built\-in `` component is that its target element must exist at the time the teleport component is mounted. This prevented users from teleporting content to other elements rendered by Vue after the teleport.

In 3\.5, we have introduced a `defer` prop for `` which mounts it after the current render cycle, so this will now work:

html\`\`\`
\...\
\\
\`\`\`This behavior requires the `defer` prop because the default behavior needs to be backwards compatible.

**Details: [PR\#11387](https://github.com/vuejs/core/issues/11387)**

### `onWatcherCleanup()` [​](#onwatchercleanup)

3\.5 introduces a globally imported API, [`onWatcherCleanup()`](https://vuejs.org/api/reactivity-core#onwatchercleanup), for registering cleanup callbacks in watchers:

js\`\`\`
import { watch, onWatcherCleanup } from 'vue'

watch(id, (newId) =\> {
 const controller = new AbortController()

 fetch(\`/api/${newId}\`, { signal: controller.signal }).then(() =\> {
 // callback logic
 })

 onWatcherCleanup(() =\> {
 // abort stale request
 controller.abort()
 })
})
\`\`\`* Related: new docs section on [Side Effect Cleanup](https://vuejs.org/guide/essentials/watchers.html#side-effect-cleanup)

---

For a comprehensive list of changes and features in 3\.5, check out of the [the full changelog on GitHub](https://github.com/vuejs/core/blob/main/CHANGELOG.md). Happy hacking!



## Vue 3 as the New Default | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-as-the-new-default.html)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)
TL;DR: Vue 3 is now the new default version as of **Monday, February 7, 2022**!

Make sure to read the [Potential Required Actions](/posts/vue-3-as-the-new-default.html#potential-required-actions) section to see if you need to make certain changes before the switch to avoid breakage.

---

## From a Library to a Framework [​](#from-a-library-to-a-framework)

When Vue first started, it was just a runtime library. Over the years, it has evolved into a framework that encompasses many sub projects:

* The core library, i.e. the `vue` npm package
* The documentation, with enough content to be considered a book
* The build toolchain, i.e. Vue CLI, vue\-loader and other supporting packages
* Vue Router for building SPA
* Vuex for state management
* Browser devtools extension for debugging and profiling
* Vetur, the VSCode extension for Single\-File Component IDE support
* ESLint plugin for static style / error checking
* Vue Test Utils for component testing
* Custom JSX transforms that leverages Vue's runtime features
* VuePress for Vue\-based static site generation

This is only possible because Vue is a community\-driven project. Many of these projects were started by community members who later became Vue team members. The rest were originally started by me, but are now almost entirely maintained by the team (with the exception of the core library).

## Soft Launch of Vue 3 [​](#soft-launch-of-vue-3)

With the core releasing a new major version, all the other parts of the framework needed to move forward together. We also needed to provide a migration path for Vue 2 users. This was a massive undertaking for a community\-drive team like Vue. When Vue 3 core was ready, most other parts of the framework were either in beta or still awaiting update. We decided to go ahead and release the core so that the early adopters, library authors and higher\-level frameworks can start building with it while we worked on the rest of the framework.

At the same time, we kept Vue 2 as the default for documentation and npm installs. This is because we knew that for many users, Vue 2 still provided a more coherent and comprehensive experience until other parts of Vue 3 are refined.

## The New Vue [​](#the-new-vue)

This soft launch process took longer than we hoped, but we are finally here: we are excited to announce that Vue 3 will become the new default version on **Monday, February 7, 2022**.

Outside of Vue core, we have improved almost every aspect of the framework:

* Blazing fast, [Vite](https://vitejs.dev/)\-powered build toolchain
* More ergonomic Composition API syntax via ``
* Improved TypeScript IDE support for Single File Components via [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar)
* Command line type checking for SFCs via [vue\-tsc](https://github.com/johnsoncodehk/volar/tree/master/packages/vue-tsc)
* Simpler state management via [Pinia](https://pinia.vuejs.org/)
* New devtools extension with simultaneous Vue 2 / Vue 3 support and a [plugin system](https://devtools.vuejs.org/plugin/plugins-guide.html) that allows community libraries to hook into the devtools panels

We also completely reworked the main documentation. [The new vuejs.org](https://staging.vuejs.org) (currently in staging) will provide updated framework overview and recommendations, flexible learning paths for users from different backgrounds, the ability to toggle between Options API and Composition API throughout the guide and examples, and many new deep dive sections. It's also *very* fast \- which we will discuss in more details in a separate blog post soon.

## Version Switch Details [​](#version-switch-details)

Here are the details on what we mean by "the new default". In addition, please read the [Potential Required Actions](#potential-required-actions) section to see if you need to make certain changes before the switch to avoid breakage.

### npm dist tags [​](#npm-dist-tags)

* `npm install vue` now installs Vue 3 by default.
* The `latest` dist tag of all other official npm packages now point to Vue 3 compatible versions, including `vue-router`, `vuex`, `vue-loader`, and `@vue/test-utils`.

### Official docs and sites [​](#official-docs-and-sites)

All documentation and official sites now default to Vue 3 versions. These include:

* vuejs.org
* router.vuejs.org
* vuex.vuejs.org
* vue\-test\-utils.vuejs.org (moved to test\-utils.vuejs.org)
* template\-explorer.vuejs.org

The current Vue 2 versions of these sites have been moved to new addresses (the version prefixes indicate the libraries' respective versions, not Vue core's):

* vuejs.org \-\> v2\.vuejs.org (old v2 URLs will auto redirect to the new address)
* router.vuejs.org \-\> v3\.router.vuejs.org
* vuex.vuejs.org \-\> v3\.vuex.vuejs.org
* vue\-test\-utils.vuejs.org \-\> v1\.test\-utils.vuejs.org
* template\-explorer.vuejs.org \-\> v2\.template\-explorer.vuejs.org

### GitHub repos [​](#github-repos)

All GitHub repos under the `vuejs` organization have switched to Vue 3 versions in the default branch. In addition, we have renamed the following repos to remove `next` in their names:

* `vuejs/vue-next` \-\> [`vuejs/core`](https://github.com/vuejs/core)
* `vuejs/vue-router-next` \-\> [`vuejs/router`](https://github.com/vuejs/router)
* `vuejs/docs-next` \-\> [`vuejs/docs`](https://github.com/vuejs/docs)
* `vuejs/vue-test-utils-next` \-\> [`vuejs/test-utils`](https://github.com/vuejs/test-utils)
* `vuejs/jsx-next` \-\> [`vuejs/babel-plugin-jsx`](https://github.com/vuejs/babel-plugin-jsx)

Translation repos for the main documentation are moved to the [`vuejs-translations` organization](https://github.com/vuejs-translations).

GitHub handles repo directs automatically, so previous links to source code and issues should still work.

### Devtools extension [​](#devtools-extension)

Devtools v6, which was previously published under the [beta channel](https://chrome.google.com/webstore/detail/vuejs-devtools/ljjemllljcmogpfapbkkighbhhppjdbg) on Chrome Web Store, is now published under the [stable channel](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd).

The previous version of the devtools extension is still be available and has been moved to the [legacy channel](https://chrome.google.com/webstore/detail/vuejs-devtools/iaajmlceplecbljialhhkmedjlpdblhp).

## Potential Required Actions [​](#potential-required-actions)

### Unversioned CDN Usage [​](#unversioned-cdn-usage)

If you are using Vue 2 via a CDN link without specifying a version, make sure to specify a version range via `@2`:

diff\`\`\`
\- \\
\+ \\

\- \\
\+ \\
\`\`\`Note: even if using Vue 3, you should also always specify a version range in production to avoid accidentally loading future major versions.

### NPM `latest` Tag [​](#npm-latest-tag)

If you are installing Vue or other official libraries from npm using the `latest` tag or `*`, please update to explicitly use Vue 2 compatible versions:

diff\`\`\`
{
 "dependencies": {
\- "vue": "latest",
\+ "vue": "^2\.6\.14",
\- "vue\-router": "latest",
\+ "vue\-router": "^3\.5\.3",
\- "vuex": "latest"
\+ "vuex": "^3\.6\.2"
 },
 "devDependencies": {
\- "vue\-loader": "latest",
\+ "vue\-loader": "^15\.9\.8",
\- "@vue/test\-utils": "latest"
\+ "@vue/test\-utils": "^1\.3\.0"
 }
}
\`\`\`

## Vue 3 as the New Default | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-as-the-new-default)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)
TL;DR: Vue 3 is now the new default version as of **Monday, February 7, 2022**!

Make sure to read the [Potential Required Actions](/posts/vue-3-as-the-new-default.html#potential-required-actions) section to see if you need to make certain changes before the switch to avoid breakage.

---

## From a Library to a Framework [​](#from-a-library-to-a-framework)

When Vue first started, it was just a runtime library. Over the years, it has evolved into a framework that encompasses many sub projects:

* The core library, i.e. the `vue` npm package
* The documentation, with enough content to be considered a book
* The build toolchain, i.e. Vue CLI, vue\-loader and other supporting packages
* Vue Router for building SPA
* Vuex for state management
* Browser devtools extension for debugging and profiling
* Vetur, the VSCode extension for Single\-File Component IDE support
* ESLint plugin for static style / error checking
* Vue Test Utils for component testing
* Custom JSX transforms that leverages Vue's runtime features
* VuePress for Vue\-based static site generation

This is only possible because Vue is a community\-driven project. Many of these projects were started by community members who later became Vue team members. The rest were originally started by me, but are now almost entirely maintained by the team (with the exception of the core library).

## Soft Launch of Vue 3 [​](#soft-launch-of-vue-3)

With the core releasing a new major version, all the other parts of the framework needed to move forward together. We also needed to provide a migration path for Vue 2 users. This was a massive undertaking for a community\-drive team like Vue. When Vue 3 core was ready, most other parts of the framework were either in beta or still awaiting update. We decided to go ahead and release the core so that the early adopters, library authors and higher\-level frameworks can start building with it while we worked on the rest of the framework.

At the same time, we kept Vue 2 as the default for documentation and npm installs. This is because we knew that for many users, Vue 2 still provided a more coherent and comprehensive experience until other parts of Vue 3 are refined.

## The New Vue [​](#the-new-vue)

This soft launch process took longer than we hoped, but we are finally here: we are excited to announce that Vue 3 will become the new default version on **Monday, February 7, 2022**.

Outside of Vue core, we have improved almost every aspect of the framework:

* Blazing fast, [Vite](https://vitejs.dev/)\-powered build toolchain
* More ergonomic Composition API syntax via ``
* Improved TypeScript IDE support for Single File Components via [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar)
* Command line type checking for SFCs via [vue\-tsc](https://github.com/johnsoncodehk/volar/tree/master/packages/vue-tsc)
* Simpler state management via [Pinia](https://pinia.vuejs.org/)
* New devtools extension with simultaneous Vue 2 / Vue 3 support and a [plugin system](https://devtools.vuejs.org/plugin/plugins-guide.html) that allows community libraries to hook into the devtools panels

We also completely reworked the main documentation. [The new vuejs.org](https://staging.vuejs.org) (currently in staging) will provide updated framework overview and recommendations, flexible learning paths for users from different backgrounds, the ability to toggle between Options API and Composition API throughout the guide and examples, and many new deep dive sections. It's also *very* fast \- which we will discuss in more details in a separate blog post soon.

## Version Switch Details [​](#version-switch-details)

Here are the details on what we mean by "the new default". In addition, please read the [Potential Required Actions](#potential-required-actions) section to see if you need to make certain changes before the switch to avoid breakage.

### npm dist tags [​](#npm-dist-tags)

* `npm install vue` now installs Vue 3 by default.
* The `latest` dist tag of all other official npm packages now point to Vue 3 compatible versions, including `vue-router`, `vuex`, `vue-loader`, and `@vue/test-utils`.

### Official docs and sites [​](#official-docs-and-sites)

All documentation and official sites now default to Vue 3 versions. These include:

* vuejs.org
* router.vuejs.org
* vuex.vuejs.org
* vue\-test\-utils.vuejs.org (moved to test\-utils.vuejs.org)
* template\-explorer.vuejs.org

The current Vue 2 versions of these sites have been moved to new addresses (the version prefixes indicate the libraries' respective versions, not Vue core's):

* vuejs.org \-\> v2\.vuejs.org (old v2 URLs will auto redirect to the new address)
* router.vuejs.org \-\> v3\.router.vuejs.org
* vuex.vuejs.org \-\> v3\.vuex.vuejs.org
* vue\-test\-utils.vuejs.org \-\> v1\.test\-utils.vuejs.org
* template\-explorer.vuejs.org \-\> v2\.template\-explorer.vuejs.org

### GitHub repos [​](#github-repos)

All GitHub repos under the `vuejs` organization have switched to Vue 3 versions in the default branch. In addition, we have renamed the following repos to remove `next` in their names:

* `vuejs/vue-next` \-\> [`vuejs/core`](https://github.com/vuejs/core)
* `vuejs/vue-router-next` \-\> [`vuejs/router`](https://github.com/vuejs/router)
* `vuejs/docs-next` \-\> [`vuejs/docs`](https://github.com/vuejs/docs)
* `vuejs/vue-test-utils-next` \-\> [`vuejs/test-utils`](https://github.com/vuejs/test-utils)
* `vuejs/jsx-next` \-\> [`vuejs/babel-plugin-jsx`](https://github.com/vuejs/babel-plugin-jsx)

Translation repos for the main documentation are moved to the [`vuejs-translations` organization](https://github.com/vuejs-translations).

GitHub handles repo directs automatically, so previous links to source code and issues should still work.

### Devtools extension [​](#devtools-extension)

Devtools v6, which was previously published under the [beta channel](https://chrome.google.com/webstore/detail/vuejs-devtools/ljjemllljcmogpfapbkkighbhhppjdbg) on Chrome Web Store, is now published under the [stable channel](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd).

The previous version of the devtools extension is still be available and has been moved to the [legacy channel](https://chrome.google.com/webstore/detail/vuejs-devtools/iaajmlceplecbljialhhkmedjlpdblhp).

## Potential Required Actions [​](#potential-required-actions)

### Unversioned CDN Usage [​](#unversioned-cdn-usage)

If you are using Vue 2 via a CDN link without specifying a version, make sure to specify a version range via `@2`:

diff\`\`\`
\- \\
\+ \\

\- \\
\+ \\
\`\`\`Note: even if using Vue 3, you should also always specify a version range in production to avoid accidentally loading future major versions.

### NPM `latest` Tag [​](#npm-latest-tag)

If you are installing Vue or other official libraries from npm using the `latest` tag or `*`, please update to explicitly use Vue 2 compatible versions:

diff\`\`\`
{
 "dependencies": {
\- "vue": "latest",
\+ "vue": "^2\.6\.14",
\- "vue\-router": "latest",
\+ "vue\-router": "^3\.5\.3",
\- "vuex": "latest"
\+ "vuex": "^3\.6\.2"
 },
 "devDependencies": {
\- "vue\-loader": "latest",
\+ "vue\-loader": "^15\.9\.8",
\- "@vue/test\-utils": "latest"
\+ "@vue/test\-utils": "^1\.3\.0"
 }
}
\`\`\`

## Vue 3.2 Released! | The Vue Point

[Read the full article](https://blog.vuejs.org/posts/vue-3-2)

Authors* NameEvan YouTwitter[@youyuxi](https://twitter.com/@youyuxi)
We are excited to announce the release of Vue.js 3\.2 "Quintessential Quintuplets"! This release includes many significant new features and performance improvements, and contains no breaking changes.

---

## New SFC Features [​](#new-sfc-features)

Two new features for Single File Components (SFCs, aka `.vue` files) have graduated from experimental status and are now considered stable:

* `` is a compile\-time syntactic sugar that greatly improves the ergonomics when using Composition API inside SFCs.
* ` v-bind` enables component state\-driven dynamic CSS values in SFC `` tags.

Here is an example component using these two new features together:

vue\`\`\`
\
import { ref } from 'vue'

const color = ref('red')
\

\
 \
 Color is: {{ color }}
 \
\

\
button {
 color: v\-bind(color);
}
\
\`\`\`Try it out in the [SFC Playground](https://sfc.vuejs.org/#eyJBcHAudnVlIjoiPHNjcmlwdCBzZXR1cD5cbmltcG9ydCB7IHJlZiB9IGZyb20gJ3Z1ZSdcblxuY29uc3QgY29sb3IgPSByZWYoJ3JlZCcpXG48L3NjcmlwdD5cblxuPHRlbXBsYXRlPlxuICA8YnV0dG9uIEBjbGljaz1cImNvbG9yID0gY29sb3IgPT09ICdyZWQnID8gJ2dyZWVuJyA6ICdyZWQnXCI+XG4gICAgQ29sb3IgaXM6IHt7IGNvbG9yIH19XG4gIDwvYnV0dG9uPlxuPC90ZW1wbGF0ZT5cblxuPHN0eWxlIHNjb3BlZD5cbmJ1dHRvbiB7XG4gIGNvbG9yOiB2LWJpbmQoY29sb3IpO1xufVxuPC9zdHlsZT4ifQ==), or read their respective documentations:

* [``](https://v3.vuejs.org/api/sfc-script-setup.html)
* [` v-bind`](https://v3.vuejs.org/api/sfc-style.html#state-driven-dynamic-css)

Building on top of ``, we also have a new RFC for improving the ergonomics of ref usage with compiler\-enabled sugar \- please share your feedback [here](https://github.com/vuejs/rfcs/discussions/369).

## Web Components [​](#web-components)

Vue 3\.2 introduces a new `defineCustomElement` method for easily creating native [custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) using Vue component APIs:

js\`\`\`
import { defineCustomElement } from 'vue'

const MyVueElement = defineCustomElement({
 // normal Vue component options here
})

// Register the custom element.
// After registration, all \`\\` tags
// on the page will be upgraded.
customElements.define('my\-vue\-element', MyVueElement)
\`\`\`This API allows developers to create Vue\-powered UI component libraries that can be used with any framework, or no framework at all. We have also added a new section in our docs on [consuming and creating Web Components in Vue](https://v3.vuejs.org/guide/web-components.html).

## Performance Improvements [​](#performance-improvements)

3\.2 includes some significant performance improvements to Vue's reactivity system, thanks to the great work by [@basvanmeurs](https://github.com/basvanmeurs). Specifically:

* [More efficient ref implementation (\~260% faster read / \~50% faster write)](https://github.com/vuejs/vue-next/pull/3995)
* [\~40% faster dependency tracking](https://github.com/vuejs/vue-next/pull/4017)
* [\~17% less memory usage](https://github.com/vuejs/vue-next/pull/4001)

The template compiler also received a number of improvements:

* [\~200% faster creation of plain element VNodes](https://github.com/vuejs/vue-next/pull/3334)
* More aggressive constant hoisting \[[1](https://github.com/vuejs/vue-next/commit/b7ea7c148552874e8bce399eec9fbe565efa2f4d)] \[[2](https://github.com/vuejs/vue-next/commit/02339b67d8c6fab6ee701a7c4f2773139ed007f5)]

Finally, there is a new [`v-memo` directive](https://v3.vuejs.org/api/directives.html#v-memo) that provides the ability to memoize part of the template tree. A `v-memo` hit allows Vue to skip not only the Virtual DOM diffing, but the creation of new VNodes altogether. Although rarely needed, it provides an escape hatch to squeeze out maximum performance in certain scenarios, for example large `v-for` lists.

The usage of `v-memo`, which is a one\-line addition, places Vue among the fastest mainstream frameworks in [js\-framework\-benchmark](https://github.com/krausest/js-framework-benchmark):



## Server\-side Rendering [​](#server-side-rendering)

The `@vue/server-renderer` package in 3\.2 now ships an ES module build which is also decoupled from Node.js built\-ins. This makes it possible to bundle and leverage `@vue/server-renderer` for use inside non\-Node.js runtimes such as [CloudFlare Workers](https://developers.cloudflare.com/workers/) or Service Workers.

We also improved the streaming render APIs, with new methods for rendering to the [Web Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API). Check out the [documentation of `@vue/server-renderer`](https://github.com/vuejs/vue-next/tree/master/packages/server-renderer#streaming-api) for more details.

## Effect Scope API [​](#effect-scope-api)

3\.2 introduces a new [Effect Scope API](https://v3.vuejs.org/api/effect-scope.html) for directly controlling the disposal timing of reactive effects (computed and watchers). It makes it easier to leverage Vue's reactivity API out of a component context, and also unlocks some advanced use cases inside components.

This is low\-level API largely intended for library authors, so it's recommended to read the feature's [RFC](https://github.com/vuejs/rfcs/blob/master/active-rfcs/0041-reactivity-effect-scope.md) for the motivation and use cases of this feature.

---

For a detailed list of all changes in 3\.2, please refer to the [full changelog](https://github.com/vuejs/vue-next/blob/master/CHANGELOG.md).



