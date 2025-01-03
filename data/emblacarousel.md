# https://www.embla-carousel.com/

## Options | Embla Carousel

[Read the full article](https://www.embla-carousel.com/api/options/)

# Options

Embla Carousel takes various **options** in order to customize how the carousel works.

---

## Usage

You can provide **options** in **two different ways**: With the [constructor options](/api/options/#constructor-options) and/or [global options](/api/options/#global-options). If both are provided, they will be merged, and if any options are in conflict, the **constructor option** has precedence and will **override global options**.

### Constructor options

The constructor options is the default way of providing options to Embla Carousel. In the following example, the carousel [loop](/api/options/#loop) option is set to `true`:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode, { loop: true })
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[emblaRef] = useEmblaCarousel({ loop: true })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselVue from 'embla\-carousel\-vue'
 const \[emblaRef] = emblaCarouselVue({ loop: true })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[emblaRef] = createEmblaCarousel(() =\> ({ loop: true }))
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let options = { loop: true }\
\...\
\`\`\`
### Global options

Setting **global options** will be applied to **all carousels** which will override the Embla default options with your own. In the following example [loop](/api/options/#loop) is set to `true`:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'
EmblaCarousel.globalOptions = { loop: true }
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode, { align: 'start' })
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import useEmblaCarousel from 'embla\-carousel\-react'
useEmblaCarousel.globalOptions = { loop: true }
export function EmblaCarousel() { const \[emblaRef] = useEmblaCarousel({ align: 'start' })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselVue from 'embla\-carousel\-vue'
 emblaCarouselVue.globalOptions = { loop: true }
 const \[emblaRef] = emblaCarouselVue({ align: 'start' })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import createEmblaCarousel from 'embla\-carousel\-solid'
createEmblaCarousel.globalOptions = { loop: true }
export function EmblaCarousel() { const \[emblaRef] = createEmblaCarousel(() =\> ({ align: 'start' }))
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 emblaCarouselSvelte.globalOptions = { loop: true }
 let options = { align: 'start' }\
\...\
\`\`\`
Make sure to assign global options **before** initializing any carousel and
**only assign it once**. Re\-assigning global options might lead to confusing
code and unexpected behaviour.

### Changing options

It's possible to **change options** passed to the Embla Carousel constructor **after initialization** with the [reInit](/api/methods/#reinit) method.

In [React](/get-started/react/), [Vue](/get-started/vue/), [Solid](/get-started/solid/) and [Svelte](/get-started/svelte/) wrappers you can pass **reactive options** and the carousel will automatically reinitialize when they change. Here are some examples:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode, { loop: true })
emblaApi.reInit({ loop: false })
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { useState, useCallback } from 'react'import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[options, setOptions] = useState({ loop: true }) const \[emblaRef, emblaApi] = useEmblaCarousel(options)
 const toggleLoop = useCallback(() =\> { setOptions((currentOptions) =\> ({ ...currentOptions, loop: !currentOptions.loop })) }, \[])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselVue from 'embla\-carousel\-vue'
 const options = ref({ loop: true }) const \[emblaRef, emblaApi] = emblaCarouselVue(options)
 function toggleLoop() { options.value = { ...options.value, loop: !options.value.loop } }
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { createSignal } from 'solid\-js'import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[options, setOptions] = createSignal({ loop: true }) const \[emblaRef] = createEmblaCarousel(() =\> options())
 function toggleLoop() { setOptions((currentOptions) =\> ({ ...currentOptions, loop: !currentOptions.loop })) }
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let options = { loop: true }
 function toggleLoop() { options = { ...options, loop: !options.loop } }\
\...\
\`\`\`
### TypeScript

The `EmblaOptionsType` is obtained directly from the **core package** `embla-carousel` and used like so:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`tsx
import EmblaCarousel, { EmblaOptionsType } from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const options: EmblaOptionsType = { loop: true }const emblaApi = EmblaCarousel(emblaNode, options)
\`\`\`Copy code snippet to clipboardCopy\`\`\`tsx
import React from 'react'import { EmblaOptionsType } from 'embla\-carousel'import useEmblaCarousel from 'embla\-carousel\-react'
type PropType = { options?: EmblaOptionsType}
export function EmblaCarousel(props: PropType) { const \[emblaRef, emblaApi] = useEmblaCarousel(props.options)
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-react` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { EmblaOptionsType } from 'embla\-carousel' import emblaCarouselVue from 'embla\-carousel\-vue'
 const options: EmblaOptionsType = { loop: true } const \[emblaRef] = emblaCarouselVue(options)
 // ...\
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-vue` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`tsx
import { EmblaOptionsType } from 'embla\-carousel'import createEmblaCarousel from 'embla\-carousel\-solid'
type PropType = { options?: EmblaOptionsType}
export function EmblaCarousel(props) { const \[emblaRef] = createEmblaCarousel(props.options)
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-solid` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { EmblaOptionsType } from 'embla\-carousel' import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let options: EmblaOptionsType = { loop: true }\
\...\
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-svelte` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

## Reference

Below follows an exhaustive **list of all** Embla Carousel **options** and their default values.

---

### active

Type: `boolean`  

Default: `true`

Setting this to `false` will not activate or deactivate the carousel. Useful when used together with the [breakpoints](/api/options/#breakpoints) option to toggle the carousel active/inactive depending on media queries.

---

### align

Type: `string | (viewSize: number, snapSize: number, index: number) => number`  

Default: `center`

Align the slides relative to the carousel viewport. Use one of the predefined alignments `start`, `center` or `end`. Alternatively, provide your own callback to fully customize the alignment.

---

### axis

Type: `string`  

Default: `x`

Choose scroll axis between `x` and `y`. Remember to stack your slides horizontally or vertically using CSS to match this option.

---

### breakpoints

Type: `EmblaOptionsType`  

Default: `{}`

An object with options that will be applied for a given breakpoint by overriding the options at the root level. Example: `'(min-width: 768px)': { loop: false }`.

**Note:** If multiple queries match, they will be merged. And when breakpoint
options clash, the last one in the list has precedence.

---

### container

Type: `string | HTMLElement | null`  

Default: `null`

Enables choosing a custom container element which holds the slides. By **default**, Embla will choose the **first direct child element** of the **root element**. Provide either a valid `CSS selector string` or a `HTML element`.

---

### containScroll

Type: `false` \| `string`  

Default: `'trimSnaps'`

Clear leading and trailing empty space that causes excessive scrolling. Use `trimSnaps` to only use snap points that trigger scrolling or `keepSnaps` to keep them.

**Note:** When this is active, it will **override alignments** applied by the
[align](/api/options/#align) option for enough slides at the **start** and the **end** of
the carousel, in order to **cover** the **leading** and **trailing space**.

---

### direction

Type: `string`  

Default: `ltr`

Choose content direction between `ltr` and `rtl`.

**Note:** When using `rtl`, the content direction also has to be set to RTL,
either by using the [HTML dir
attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir)
or the [CSS
direction](https://developer.mozilla.org/en-US/docs/Web/CSS/direction)
property.

---

### dragFree

Type: `boolean`  

Default: `false`

Enables momentum scrolling. The duration of the continued scrolling is proportional to how vigorous the drag gesture is.

---

### dragThreshold

Type: `number`  

Default: `10`

Drag threshold in pixels. This only affects **when** clicks are fired and not. In contrast to other carousel libraries, it will **not affect when dragging** of the carousel **starts**.

**Note:** Browsers handle touch events differently than mouse events. Browsers
won't fire the click event when a touch event includes an accidental slight
swipe gesture. This is why this threshold only works for mouse events.

---

### duration

Type: `number`  

Default: `25`

Set scroll duration when triggered by any of the API methods. Higher numbers enables slower scrolling. Drag interactions are not affected because duration is then determined by the drag force.

**Note:** Duration is **not** in milliseconds because Embla uses an attraction
physics simulation when scrolling instead of easings. Only values between
`20`\-`60` are recommended.

---

### inViewThreshold

Type: `IntersectionObserverInit.threshold`  

Default: `0`

This is the Intersection Observer [threshold](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API#creating_an_intersection_observer) option that will be applied to all slides.

---

### loop

Type: `boolean`  

Default: `false`

Enables **infinite looping**. Embla will apply `translateX` or `translateY` to the slides that need to change position in order to create the loop effect.

Embla automatically falls back to `false` if slide content isn't enough to
create the loop effect without visible glitches.

---

### skipSnaps

Type: `boolean`  

Default: `false`

Allow the carousel to skip scroll snaps if it's dragged vigorously. Note that this option will be ignored if the [dragFree](/api/options/#dragfree) option is set to `true`.

---

### slides

Type: `string | HTMLElement[] | NodeListOf | null`  

Default: `null`

Enables using custom slide elements. By **default**, Embla will choose **all direct child elements** of its [container](/api/options/#container). Provide either a valid `CSS selector string` or a `nodeList/array` containing `HTML elements`.

**Note:** Even though it's possible to provide custom slide elements, they
still have to be **direct descendants** of the carousel container.

**Warning:** If you place elements inside the carousel container that aren't
slides, they either shouldn't have any size, or should be detached from the
document flow with `position: absolute` or similar.

---

### slidesToScroll

Type: `string | number`  

Default: `1`

Group slides together. Drag interactions, dot navigation, and previous/next buttons are mapped to group slides into the given number, which has to be an integer. Set it to `auto` if you want Embla to group slides automatically.

---

### startIndex

Type: `number`  

Default: `0`

Set the initial scroll snap to the given number. First snap index starts at `0`. Please note that this is not necessarily equal to the number of slides when used together with the [slidesToScroll](/api/options/#slidestoscroll) option.

---

### watchDrag

Type: `boolean | (emblaApi: EmblaCarouselType, event: MouseEvent | TouchEvent) => boolean | void`  

Default: `true`

Enables for scrolling the carousel with mouse and touch interactions. Set this to `false` to disable drag events or pass a custom callback to add your own drag logic.

**Note:** When passing a custom callback it will run **before** the default
Embla drag behaviour. Return `true` in your callback if you want Embla to run
its default drag behaviour after your callback, or return `false` if you want
to skip it.

---

### watchFocus

Type: `boolean | (emblaApi: EmblaCarouselType, event: FocusEvent) => boolean | void`  

Default: `true`

Embla automatically watches the [slides](api/options/#slides) for focus events. The default callback fires the [slideFocus](/api/events/#slidefocus/) event and [scrolls](/api/methods/#scrollto/) to the focused element. Set this to `false` to disable this behaviour or pass a custom callback to add your own focus logic.

**Note:** When passing a custom callback it will run **before** the default
Embla focus behaviour. Return `true` in your callback if you want Embla to run
its default focus behaviour after your callback, or return `false` if you want
to skip it.

---

### watchResize

Type: `boolean | (emblaApi: EmblaCarouselType, entries: ResizeObserverEntry[]) => boolean | void`  

Default: `true`

Embla automatically watches the [container](/api/methods/#containernode/) and [slides](/api/methods/#slidenodes/) for size changes and runs [reInit](/api/methods/#reinit/) when any size has changed. Set this to `false` to disable this behaviour or pass a custom callback to add your own resize logic.

**Note:** When passing a custom callback it will run **before** the default
Embla resize behaviour. Return `true` in your callback if you want Embla to
run its default resize behaviour after your callback, or return `false` if you
want to skip it.

---

### watchSlides

Type: `boolean | (emblaApi: EmblaCarouselType, mutations: MutationRecord[]) => boolean | void`  

Default: `true`

Embla automatically watches the [container](/api/methods/#containernode/) for **added** and/or **removed** slides and runs [reInit](/api/methods/#reinit/) if needed. Set this to `false` to disable this behaviour or pass a custom callback to add your own slides changed logic.

**Note:** When passing a custom callback it will run **before** the default
Embla mutation behaviour. Return `true` in your callback if you want Embla to
run its default mutation behaviour after your callback, or return `false` if
you want to skip it.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/api/options.mdx)

## Events | Embla Carousel

[Read the full article](https://www.embla-carousel.com/api/events/)

# Events

Embla Carousel exposes **events** that you can listen to in order to **react** to **changes** in the carousel.

---

## Usage

You need an **initialized carousel** in order to **make use of events**. Events will only be fired during the lifecycle of a carousel and added event listeners will persist even when you hard reset the carousel with the [reInit](/api/methods/#reinit) method.

### Adding event listeners

After initializing a carousel, we're going to **subscribe** to the [slidesInView](/api/events/#slidesinview) **event** in the following example:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode)
function logSlidesInView(emblaApi) { console.log(emblaApi.slidesInView())}
emblaApi.on('slidesInView', logSlidesInView)
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { useCallback, useEffect } from 'react'import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel()
 const logSlidesInView = useCallback((emblaApi) =\> { console.log(emblaApi.slidesInView()) }, \[])
 useEffect(() =\> { if (emblaApi) emblaApi.on('slidesInView', logSlidesInView) }, \[emblaApi, logSlidesInView])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import emblaCarouselVue from 'embla\-carousel\-vue'
 const \[emblaRef, emblaApi] = emblaCarouselVue()
 function logSlidesInView(emblaApi) { console.log(emblaApi.slidesInView()) }
 onMounted(() =\> { if (emblaApi.value) emblaApi.value.on('slidesInView', logSlidesInView) })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel()
 function logSlidesInView(emblaApi) { console.log(emblaApi.slidesInView()) }
 onMount(() =\> { const api = emblaApi() if (api) api.on('slidesInView', logSlidesInView) })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let emblaApi
 function logSlidesInView(emblaApi) { console.log(emblaApi.slidesInView()) }
 function onInit(event) { emblaApi = event.detail emblaApi.on('slidesInView', logSlidesInView) }\
\...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

### Removing event listeners

In order to remove an event listener, you'll have to call the [off](/api/methods/#off) method and make sure to pass the **same callback reference** you passed to the [on](/api/methods/#off) method:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode)
function logSlidesInViewOnce(emblaApi) { console.log(emblaApi.slidesInView()) emblaApi.off('slidesInView', logSlidesInViewOnce)}
emblaApi.on('slidesInView', logSlidesInViewOnce)
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { useCallback, useEffect } from 'react'import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel()
 const logSlidesInViewOnce = useCallback((emblaApi) =\> { console.log(emblaApi.slidesInView()) emblaApi.off('slidesInView', logSlidesInViewOnce) }, \[])
 useEffect(() =\> { if (emblaApi) emblaApi.on('slidesInView', logSlidesInViewOnce) }, \[emblaApi, logSlidesInViewOnce])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import emblaCarouselVue from 'embla\-carousel\-vue'
 const \[emblaRef, emblaApi] = emblaCarouselVue()
 function logSlidesInViewOnce(emblaApi) { console.log(emblaApi.slidesInView()) emblaApi.off('slidesInView', logSlidesInViewOnce) }
 onMounted(() =\> { if (emblaApi.value) emblaApi.value.on('slidesInView', logSlidesInViewOnce) })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel()
 function logSlidesInViewOnce(emblaApi) { console.log(emblaApi.slidesInView()) emblaApi.off('slidesInView', logSlidesInViewOnce) }
 onMount(() =\> { const api = emblaApi() if (api) api.on('slidesInView', logSlidesInViewOnce) })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let emblaApi
 function logSlidesInViewOnce(emblaApi) { console.log(emblaApi.slidesInView()) emblaApi.off('slidesInView', logSlidesInViewOnce) }
 function onInit(event) { emblaApi = event.detail emblaApi.on('slidesInView', logSlidesInViewOnce) }\
\...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

### TypeScript

The `EmblaEventType` is obtained directly from the **core package** `embla-carousel` and used like so:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`tsx
import EmblaCarousel, { EmblaCarouselType, EmblaEventType} from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode)
function logEmblaEvent( emblaApi: EmblaCarouselType, eventName: EmblaEventType): void { console.log(\`Embla just triggered ${eventName}!\`)}
emblaApi.on('slidesInView', logEmblaEvent)
\`\`\`Copy code snippet to clipboardCopy\`\`\`tsx
import React, { useCallback } from 'react'import { EmblaCarouselType, EmblaEventType } from 'embla\-carousel'import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel()
 const logEmblaEvent = useCallback( (emblaApi: EmblaCarouselType, eventName: EmblaEventType) =\> { console.log(\`Embla just triggered ${eventName}!\`) }, \[] )
 useEffect(() =\> { if (emblaApi) emblaApi.on('slidesInView', logEmblaEvent) }, \[emblaApi, logEmblaEvent])
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-react` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import { EmblaCarouselType, EmblaEventType } from 'embla\-carousel' import emblaCarouselVue from 'embla\-carousel\-vue'
 const \[emblaRef] = emblaCarouselVue()
 function logEmblaEvent( emblaApi: EmblaCarouselType, eventName: EmblaEventType ): void { console.log(\`Embla just triggered ${eventName}!\`) }
 onMounted(() =\> { if (emblaApi.value) emblaApi.value.on('slidesInView', logEmblaEvent) })
 // ...\
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-vue` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import { EmblaCarouselType, EmblaEventType } from 'embla\-carousel'import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel()
 function logEmblaEvent( emblaApi: EmblaCarouselType, eventName: EmblaEventType ): void { console.log(\`Embla just triggered ${eventName}!\`) }
 onMount(() =\> { const api = emblaApi() if (api) api.on('slidesInView', logEmblaEvent) })
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-solid` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { EmblaCarouselType, EmblaEventType } from 'embla\-carousel' import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let emblaApi: EmblaCarouselType
 function logEmblaEvent( emblaApi: EmblaCarouselType, eventName: EmblaEventType ): void { console.log(\`Embla just triggered ${eventName}!\`) }
 function onInit(event: CustomEvent\): void { emblaApi = event.detail emblaApi.on('slidesInView', logEmblaEvent) }\
\...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-svelte` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

## Reference

Below follows an exhaustive **list of all** Embla Carousel **events** together with information about how they work.

---

### init

Once: `yes`

Runs when the carousel mounts for the first time. This only fires once which means that it won't fire when the carousel is re\-initialized using the [reInit](/api/methods/#reinit) method.

---

### reInit

Once: `no`

Runs when the [reInit](/api/methods/#reinit) method is called. When the window is resized, Embla Carousel automatically calls the [reInit](/api/methods/#reinit) method which will also fire this event.

---

### destroy

Once: `yes`

Runs when the carousel has been destroyed using the [destroy](/api/methods/#destroy) method. This only fires once and will be the last event the carousel fires.

---

### select

Once: `no`

Runs when the selected scroll snap changes. The select event is triggered by drag interactions or the [scrollNext](/api/methods/#scrollnext), [scrollPrev](/api/methods/#scrollPrev) or [scrollTo](/api/methods/#scrollto) methods.

---

### scroll

Once: `no`

Runs when the carousel is scrolling. It might be a good idea to throttle this if you're doing expensive stuff in your callback function.

---

### settle

Once: `no`

Runs when the carousel has settled after scroll has been triggered. Please note that this can take longer than you think when [dragFree](/api/options/#dragfree) is enabled or when using slow [transitions](/api/options/#duration).

---

### resize

Once: `no`

Runs when the carousel container or the slide sizes change. It's using [ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) under the hood.

---

### slidesInView

Once: `no`

Runs when any slide has **entered** or **exited** the viewport. This event is intended to be used together with the [slidesInView](/api/methods/#slidesinview) and/or [slidesNotInView](/api/methods/#slidesnotinview) methods.

---

### slidesChanged

Once: `no`

Runs when slides are added to, or removed from the carousel [container](/api/options/#container). It's using [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver) under the hood.

---

### slideFocus

Once: `no`

Runs when a slide receives focus. For example, when a focusable element like a button, link or input receives focus inside a slide.

---

### pointerDown

Once: `no`

Runs when the user has a pointer down on the carousel. It's triggered by a `touchstart` or a `mousedown` event.

---

### pointerUp

Once: `no`

Runs when the user has released the pointer from the carousel. It's triggered by a `touchend` or a `mouseup` event.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/api/events.mdx)

## Plugins | Embla Carousel

[Read the full article](https://www.embla-carousel.com/api/plugins/)

# Plugins

It's possible to **extend** Embla carousel with additional features using **plugins**. The complete list of official plugins can be found [here](/plugins/).

---

## Installation

All **official plugins** are separate **NPM packages**. They're all **prefixed** with `embla-carousel` followed by its **unique** plugin **name**. For example, the `Autoplay` plugin is installed like so:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-autoplay \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-autoplay
\`\`\`
## Usage

The Embla Carousel **constructor** accepts an **array of plugins**. Each plugin might have its own [options](/api/plugins/#constructor-options), [methods](/api/plugins/#calling-methods) and [events](/api/plugins/#adding-event-listeners).

### Adding a plugin

The constructor plugin array is the default way of providing plugins to Embla Carousel. In the following example, the [Autoplay](/plugins/autoplay/) plugin is added to the carousel:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'import Autoplay from 'embla\-carousel\-autoplay'
const emblaNode = document.querySelector('.embla')const embla = EmblaCarousel(emblaNode, { loop: true }, \[Autoplay()])
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import useEmblaCarousel from 'embla\-carousel\-react'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef] = useEmblaCarousel({ loop: true }, \[Autoplay()])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselVue from 'embla\-carousel\-vue' import Autoplay from 'embla\-carousel\-autoplay'
 const \[emblaRef] = emblaCarouselVue({ loop: true }, \[Autoplay()])
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import createEmblaCarousel from 'embla\-carousel\-solid'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef] = createEmblaCarousel( () =\> ({ loop: true }), () =\> \[AutoPlay()] )
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte' import Autoplay from 'embla\-carousel\-autoplay'
 let plugins = \[Autoplay()]\
\...\
\`\`\`
Note that it's possible to **change plugins** passed to the Embla Carousel
constructor **after initialization** with the [reInit](/api/methods/#reinit)
method.

### Constructor options

Plugins have their own specific **options** which is the first argument of the plugin constructor. This allows for configuring the plugin to your liking:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'import Autoplay from 'embla\-carousel\-autoplay'
const emblaNode = document.querySelector('.embla')const embla = EmblaCarousel(emblaNode, { loop: true }, \[ Autoplay({ delay: 4000 })])
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import useEmblaCarousel from 'embla\-carousel\-react'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef] = useEmblaCarousel({ loop: true }, \[ Autoplay({ delay: 4000 }) ])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselVue from 'embla\-carousel\-vue' import Autoplay from 'embla\-carousel\-autoplay'
 const \[emblaRef] = emblaCarouselVue({ loop: true }, \[ Autoplay({ delay: 4000 }) ])
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import createEmblaCarousel from 'embla\-carousel\-solid'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef] = createEmblaCarousel( () =\> ({ loop: true }), () =\> \[AutoPlay({ delay: 4000 })] )
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte' import Autoplay from 'embla\-carousel\-autoplay'
 let plugins = \[Autoplay({ delay: 4000 })]\
\...\
\`\`\`
### Global options

All [official plugins](/plugins/) allows you to set **global options** that will be applied to all instances. This allows for overriding the default plugin options with your own:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'import Autoplay from 'embla\-carousel\-autoplay'
Autoplay.globalOptions = { delay: 4000 }
const emblaNode = document.querySelector('.embla')const embla = EmblaCarousel(emblaNode, { loop: true }, \[Autoplay()])
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import useEmblaCarousel from 'embla\-carousel\-react'import Autoplay from 'embla\-carousel\-autoplay'
Autoplay.globalOptions = { delay: 4000 }
export function EmblaCarousel() { const \[emblaRef] = useEmblaCarousel({ loop: true }, \[Autoplay()])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselVue from 'embla\-carousel\-vue' import Autoplay from 'embla\-carousel\-autoplay'
 Autoplay.globalOptions = { delay: 4000 }
 const \[emblaRef] = emblaCarouselVue({ loop: true }, \[Autoplay()])
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import createEmblaCarousel from 'embla\-carousel\-solid'import Autoplay from 'embla\-carousel\-autoplay'
Autoplay.globalOptions = { delay: 4000 }
export function EmblaCarousel() { const \[emblaRef] = createEmblaCarousel( () =\> ({ loop: true }), () =\> \[AutoPlay()] )
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte' import Autoplay from 'embla\-carousel\-autoplay'
 Autoplay.globalOptions = { delay: 4000 }
 let plugins = \[Autoplay()]\
\...\
\`\`\`
Make sure to assign global options **before** initializing any carousel and
**only assign it once**. Re\-assigning global options might lead to confusing
code and unexpected behaviour.

### Calling methods

Additionally, some plugins expose their own **API methods**. You can access plugin methods by calling the [plugin](/api/methods/#plugins) method like demonstrated below:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'import Autoplay from 'embla\-carousel\-autoplay'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode, { loop: true }, \[Autoplay()])
emblaApi.plugins().autoplay.stop()
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { useEffect } from 'react'import useEmblaCarousel from 'embla\-carousel\-react'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel({ loop: true }, \[Autoplay()])
 useEffect(() =\> { if (emblaApi) emblaApi.plugins().autoplay.stop() }, \[emblaApi])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import emblaCarouselVue from 'embla\-carousel\-vue' import Autoplay from 'embla\-carousel\-autoplay'
 const \[emblaRef, emblaApi] = emblaCarouselVue({ loop: true }, \[Autoplay()])
 onMounted(() =\> { if (emblaApi.value) emblaApi.value.plugins().autoplay.stop() })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import createEmblaCarousel from 'embla\-carousel\-solid'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel( () =\> ({ loop: true }), () =\> \[AutoPlay()] )
 onMount(() =\> { const api = emblaApi() if (api) api.plugins().autoplay.stop() })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte' import Autoplay from 'embla\-carousel\-autoplay'
 let emblaApi let plugins = \[Autoplay()]
 function onInit(event) { emblaApi = event.detail emblaApi.plugins().autoplay.stop() }\
\ ...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

### Adding event listeners

Some plugins fire their own **events**. Plugin events are structured as follows `:eventname`. [Adding](/api/events/#adding-event-listeners) and [removing](/api/events/#removing-event-listeners) plugin event listeners is done the same way as native Embla events. Here's an example where an event is added to the autoplay plugin:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'import Autoplay from 'embla\-carousel\-autoplay'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode, { loop: true }, \[Autoplay()])
function logPluginEvent(emblaApi, eventName) { console.log(\`Autoplay just triggered ${eventName}!\`)}
emblaApi.on('autoplay:stop', logPluginEvent)
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { useEffect, useCallback } from 'react'import useEmblaCarousel from 'embla\-carousel\-react'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel({ loop: true }, \[Autoplay()])
 const logPluginEvent = useCallback((emblaApi, eventName) =\> { console.log(\`Autoplay just triggered ${eventName}!\`) }, \[])
 useEffect(() =\> { if (emblaApi) emblaApi.on('autoplay:stop', logPluginEvent) }, \[emblaApi, logPluginEvent])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import emblaCarouselVue from 'embla\-carousel\-vue' import Autoplay from 'embla\-carousel\-autoplay'
 const \[emblaRef, emblaApi] = emblaCarouselVue({ loop: true }, \[Autoplay()])
 function logPluginEvent(emblaApi, eventName) { console.log(\`Autoplay just triggered ${eventName}!\`) }
 onMounted(() =\> { if (emblaApi.value) emblaApi.value.on('autoplay:stop', logPluginEvent) })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import createEmblaCarousel from 'embla\-carousel\-solid'import Autoplay from 'embla\-carousel\-autoplay'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel( () =\> ({ loop: true }), () =\> \[AutoPlay()] )
 function logPluginEvent(emblaApi, eventName) { console.log(\`Autoplay just triggered ${eventName}!\`) }
 onMount(() =\> { const api = emblaApi() if (api) api.on('autoplay:stop', logPluginEvent) })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte' import Autoplay from 'embla\-carousel\-autoplay'
 let emblaApi let plugins = \[Autoplay()]
 function logPluginEvent(emblaApi, eventName) { console.log(\`Autoplay just triggered ${eventName}!\`) }
 function onInit(event) { emblaApi = event.detail emblaApi.on('autoplay:stop', logPluginEvent) }\
\ ...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

### TypeScript

The `EmblaPluginType` is obtained directly from the **core package** `embla-carousel` and used like so:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`tsx
import EmblaCarousel, { EmblaPluginType } from 'embla\-carousel'import Autoplay from 'embla\-carousel\-autoplay'
const emblaNode = document.querySelector('.embla')const plugins: EmblaPluginType\[] = \[Autoplay()]const emblaApi = EmblaCarousel(emblaNode, { loop: true }, plugins)
\`\`\`Copy code snippet to clipboardCopy\`\`\`tsx
import React from 'react'import { EmblaPluginType } from 'embla\-carousel'import useEmblaCarousel from 'embla\-carousel\-react'import Autoplay from 'embla\-carousel\-autoplay'
type PropType = { plugins?: EmblaPluginType\[]}
export function EmblaCarousel(props) { const \[emblaRef, emblaApi] = useEmblaCarousel({ loop: true }, props.plugins)
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-react` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { EmblaPluginType } from 'embla\-carousel' import emblaCarouselVue from 'embla\-carousel\-vue' import Autoplay from 'embla\-carousel\-autoplay'
 const plugins: EmblaPluginType\[] = \[Autoplay()] const \[emblaRef] = emblaCarouselVue({ loop: true }, plugins)
 // ...\
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-vue` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`tsx
import { EmblaPluginType } from 'embla\-carousel'import createEmblaCarousel from 'embla\-carousel\-solid'import Autoplay from 'embla\-carousel\-autoplay'
type PropType = { plugins?: EmblaPluginType\[]}
export function EmblaCarousel(props) { const \[emblaRef, emblaApi] = createEmblaCarousel( () =\> ({ loop: true }), props.plugins )
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-solid` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { EmblaPluginType } from 'embla\-carousel' import emblaCarouselSvelte from 'embla\-carousel\-svelte' import Autoplay from 'embla\-carousel\-autoplay'
 let emblaApi let plugins: EmblaPluginType\[] = \[Autoplay()]\
\...\
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-svelte` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/api/plugins.mdx)

## Autoplay | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/autoplay/)

# Autoplay

[View plugin on GitHub](https://github.com/davidjerleke/embla-carousel/tree/master/packages/embla-carousel-autoplay)
This plugin is used to extend Embla Carousel with **autoplay** functionality.

---

## Example

Edit Code
## Installation

Start by installing the **npm package** and save it to your dependencies:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-autoplay \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-autoplay
\`\`\`
## Options

Below follows an exhaustive **list of all** `Autoplay` **options** and their default values.

---

### delay

Type: `number | (scrollSnapList: number[], emblaApi: EmblaCarouselType) => number[]`  

Default: `4000`

Choose a delay between transitions in milliseconds. If you pass a number, the same delay will be **applied to all transitions**. If you pass a function, you can return an array of numbers based on the `scrollSnapList` parameter and set **different delays for each scroll snap**.

---

### jump

Type: `boolean`  

Default: `false`

When set to true `true`, autoplay will do instant slide transitions when advancing.

---

### playOnInit

Type: `boolean`  

Default: `true`

If set to `false`, you'll have to start autoplay manually by calling the [play](/plugins/autoplay/#play) method. It's useful to set this to `false` when you want full control over the timing. For example, when building an autoplay progress bar.

---

### stopOnInteraction

Type: `boolean`  

Default: `true`

If set to `false`, autoplay will not be disabled after drag interactions, and it will restart every time after an interaction.

---

### stopOnMouseEnter

Type: `boolean`  

Default: `false`

When enabled, autoplay will stop when a mouse pointer enters the Embla Carousel container. If [stopOnInteraction](/plugins/autoplay/#stoponinteraction) is also `false`, autoplay will resume when the mouse leaves the carousel container.

---

### stopOnFocusIn

Type: `boolean`  

Default: `true`

When enabled, autoplay will stop when a focusable element inside the carousel recieves focus. If [stopOnInteraction](/plugins/autoplay/#stoponinteraction) is `false`, autoplay will resume when the user leaves focus.

---

### stopOnLastSnap

Type: `boolean`  

Default: `false`

If this parameter is enabled, autoplay will stop when it reaches last slide.

---

### rootNode

Type: `(emblaRoot: HTMLElement) => HTMLElement | null`  

Default: `null`

The **node** that should **respond** to user **interactions** like [stopOnMouseEnter](/plugins/autoplay/#stoponmouseenter) and [stopOnInteraction](/plugins/autoplay/#stoponinteraction). If this is omitted, the node that wraps the Embla Carousel will be used as default.

---

## Methods

Below follows an exhaustive **list of all** `Autoplay` **methods** with their respective parameters and return values.

---

### play

Parameters: `jump?: boolean`  

Returns: `void`

Start autoplay. Set the **jump** parameter to `true` when you want autoplay to do instant slide transitions when advancing. Please note that providing a value to this method vill override the [jump](/plugins/autoplay/#jump) option.

---

### stop

Parameters: `none`  

Returns: `void`

Stop autoplay.

---

### reset

Parameters: `none`  

Returns: `void`

Resets the timer and starts over. This will only take effect if autoplay is already active. If autoplay is stopped, this method won't do anything.

---

### isPlaying

Parameters: `none`  

Returns: `boolean`

Returns a boolean whether autoplay is playing or not.

---

### timeUntilNext

Parameters: `none`  

Returns: `number | null`

If the autoplay timer is active, this will return a number representing the time left until the autoplay scrolls to the next snap. If the timer is not active, this will return `null`. Use this together with the [autoplay:timerset](/plugins/autoplay/#autoplaytimerset) and [autoplay:timerstopped](/plugins/autoplay/#autoplaytimerstopped) events to create a custom progress bar for autoplay.

If you're using a reactive wrapper for Embla Carousel like
`embla-carousel-react` and building an autoplay progress bar, you probably
want to set [playOnInit](/plugins/autoplay/#playoninit) to `false` and call
the `play` method manually to fully control the timing.

This is because the autoplay plugin will start playing as soon as it's
initialized, which might not be what you want in these cases.

---

## Events

Below follows an exhaustive **list of all** `Autoplay` **events** together with information about how they work.

---

### autoplay:play

Once: `no`

Fires when autoplay starts playing. When this event is triggered, the **autoplay timer is active**, and autoplay will select the next scroll snap and start scrolling to it when the [delay](/plugins/autoplay/#delay) has passed.

---

### autoplay:stop

Once: `no`

Fires when autoplay stops playing. When this event is triggered, the **autoplay timer is not active anymore**.

---

### autoplay:select

Once: `no`

Fires directly after autoplay selects the next scroll snap and starts scrolling to it.

---

### autoplay:timerset

Once: `no`

Fires when the autoplay timer is set. As soon as the timer is set, countdown to autoplay to the next scroll snap will begin.

---

### autoplay:timerstopped

Once: `no`

Fires when the autoplay timer is stopped.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/autoplay.mdx)

## No Title

[Read the full article](https://www.embla-carousel.com/api/options/api/options/)

This app only works with JavaScript enabled.# Page not found

Sorry \- We couldn’t find what you were looking for.

[Embla Carousel Homepage](/)



## Wheel Gestures | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/wheel-gestures/)

# Wheel Gestures

[View plugin on GitHub](https://github.com/xiel/embla-carousel-wheel-gestures)
This plugin is used to extend Embla Carousel with the ability to **use the mouse/trackpad wheel** to **navigate** the carousel.

---

## Installation

First you need to install the **npm package** and save it to your dependencies:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-wheel\-gestures \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-wheel\-gestures
\`\`\`
## Usage

This plugin accepts a single **optional** parameter, which is its [options](/plugins/wheel-gestures/#options) object that allows you to configure it.

Copy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'import { WheelGesturesPlugin } from 'embla\-carousel\-wheel\-gestures'
const embla = EmblaCarousel(emblaRoot, { loop: false }, \[WheelGesturesPlugin()]) // Add plugin
\`\`\`
## Options

Below follows an exhaustive **list of all** `Wheel Gestures` **options** and their default values.

---

### wheelDraggingClass

Type: `string`  

Default: `is-wheel-dragging`

Choose a classname that will be applied to the container during a wheel gesture. Pass an empty string to opt\-out.

---

### forceWheelAxis

Type: `string | undefined`  

Default: `undefined`

Force an axis on which to listen for wheel events. Choose scroll axis between `x` and `y`. Useful if you want to slide horizontally when scrolling vertically or vice versa.

---

### target

Type: `Element`  

Default: `undefined`

Specify the element that should be observed for wheel events.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/wheel-gestures.mdx)

## API | Embla Carousel

[Read the full article](https://www.embla-carousel.com/api/)

# API

A lightweight carousel shouldn't be limited to just its core features. That's why the Embla Carousel API is **designed** with **extensibility in mind**, and it exposes a **rich API** that can **easily be extended** to cover most of the use cases for carousels.

---

## Explore the API

* [### Options

Discover how to customize Embla Carousel with its available options.

Read more](/api/options/)
* [### Methods

Explore Embla Carousel methods useful for extending the carousel beyond its native functionality.

Read more](/api/methods/)
* [### Events

Learn how to listen to Embla Carousel events and how to make use of them.

Read more](/api/events/)
* [### Plugins

Learn how to add plugins to Embla Carousel and extend it.

Read more](/api/plugins/)
[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/api/index.mdx)

## Auto Height | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/auto-height/)

# Auto Height

[View plugin on GitHub](https://github.com/davidjerleke/embla-carousel/tree/master/packages/embla-carousel-auto-height)
This plugin is used to extend Embla Carousel with **auto height** functionality. It changes the height of the carousel container to fit the height of the highest slide in view.

---

## Example

Edit Code
## Installation

First you need to install the **npm package** and save it to your dependencies:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-auto\-height \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-auto\-height
\`\`\`
You can make use of CSS transitions to **transition height** changes. But beware: Transitioning height triggers reflow and may cause a performance hit.

Copy code snippet to clipboardCopy\`\`\`css
.embla\_\_container { transition: height 0\.2s;}
\`\`\`
If you've been following along with any of the guides in the [get started](/get-started/) section, you want to make sure that each **slide height** is **determined** by the **content** it holds. Add the following to your CSS to achieve this:

Copy code snippet to clipboardCopy\`\`\`css
.embla\_\_container { display: flex; align\-items: flex\-start; /\* Add this \*/}
\`\`\`[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/auto-height.mdx)

## Class Names | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/class-names/)

# Class Names

[View plugin on GitHub](https://github.com/davidjerleke/embla-carousel/tree/master/packages/embla-carousel-class-names)
Class Names is a **class name toggle** utility plugin for Embla Carousel that enables you to automate the toggling of class names on your carousel.

---

## Example

Edit Code
## Installation

First you need to install the **npm package** and save it to your dependencies:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-class\-names \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-class\-names
\`\`\`
## Usage

Please read the [plugins](/api/plugins/#usage) page to learn **how to work with plugins**.

## Options

Below follows an exhaustive **list of all** `Class Names` **options** and their default values.

---

### snapped

Type: `string | string[]`  

Default: `is-snapped`

Choose a class name that will be applied to the **snapped slides**. It's also possible to pass an array of class names. Pass an empty string to opt\-out.

---

### inView

Type: `string | string[]`  

Default: `is-in-view`

Choose a class name that will be applied to **slides in view**. It's also possible to pass an array of class names. Pass an empty string to opt\-out.

This feature will honor the [inViewThreshold](/api/options/#inviewthreshold)
option.

---

### draggable

Type: `string | string[]`  

Default: `is-draggable`

Choose a class name that will be applied to a **draggable carousel**. It's also possible to pass an array of class names. Pass an empty string to opt\-out.

---

### dragging

Type: `string | string[]`  

Default: `is-dragging`

Choose a class name that will be applied to the container **when dragging**. It's also possible to pass an array of class names. Pass an empty string to opt\-out.

---

### loop

Type: `string | string[]`  

Default: `is-loop`

Choose a class name that will be applied to a carousel with **loop activated**. It's also possible to pass an array of class names. Pass an empty string to opt\-out.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/class-names.mdx)

## Fade | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/fade/)

# Fade

[View plugin on GitHub](https://github.com/davidjerleke/embla-carousel/tree/master/packages/embla-carousel-fade)
This plugin is used to replace the Embla Carousel scroll functionality with **fade transitions**.

---

## Example

Edit Code
## Installation

Start by installing the **npm package** and save it to your dependencies:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-fade \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-fade
\`\`\`
When the Fade plugin is enabled, the
[inViewThreshold](/api/options/#inviewthreshold) option no longer has any
effect. This is because the Fade plugin stacks any slides with an **opacity
higher** than `0` on top of each other, eliminating the concept of scrolling
and gradual appearance of slides.

If your slides are less than 100% of the viewport width, it's recommended to set these options when using the Fade plugin to avoid confusing UX:

Copy code snippet to clipboardCopy\`\`\`ts
const options = { align: 'center', containScroll: false}
\`\`\`  

However, `align: center` is default so you can omit setting the align option and achieve the same thing like so:

Copy code snippet to clipboardCopy\`\`\`ts
const options = { containScroll: false}
\`\`\`[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/fade.mdx)

## Auto Scroll | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/auto-scroll/)

# Auto Scroll

[View plugin on GitHub](https://github.com/davidjerleke/embla-carousel/tree/master/packages/embla-carousel-auto-scroll)
This plugin is used to extend Embla Carousel with **auto scroll** functionality.

---

## Example

Edit Code
## Installation

Start by installing the **npm package** and save it to your dependencies:

CDNCDNnpmnpmyarnyarnCopy code snippet to clipboardCopy\`\`\`html
\\
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
npm install embla\-carousel\-auto\-scroll \-\-save
\`\`\`Copy code snippet to clipboardCopy\`\`\`shell
yarn add embla\-carousel\-auto\-scroll
\`\`\`
## Options

Below follows an exhaustive **list of all** `Auto Scroll` **options** and their default values.

### speed

Type: `number`  

Default: `2`

Number of pixels auto scroll should advance per frame.

---

### startDelay

Type: `number`  

Default: `1000`

Number of milliseconds auto scroll should **wait before it starts**. This also applies when user interactions end and [stopOnInteraction](/plugins/auto-scroll/#stoponinteraction) is `false`.

---

### direction

Type: `string`  

Default: `forward`

This option is used to set the auto scroll direction. Set it to `backward` if you want it to scroll in the opposite direction.

---

### playOnInit

Type: `boolean`  

Default: `true`

If set to `false`, you'll have to start auto scroll yourself by calling the [play](/plugins/auto-scroll/#play) method.

---

### stopOnInteraction

Type: `boolean`  

Default: `true`

If set to `false`, auto scroll will not be disabled after drag interactions, and it will restart every time after an interaction.

---

### stopOnMouseEnter

Type: `boolean`  

Default: `false`

When enabled, auto scroll will stop when a mouse pointer enters the Embla Carousel container. If [stopOnInteraction](/plugins/auto-scroll/#stoponinteraction) is also `false`, auto scroll will resume when the mouse leaves the carousel container.

---

### stopOnFocusIn

Type: `boolean`  

Default: `true`

When enabled, auto scroll will stop when a focusable element inside the carousel recieves focus. If [stopOnInteraction](/plugins/auto-scroll/#stoponinteraction) is `false`, auto scroll will resume when the user leaves focus.

---

### rootNode

Type: `(emblaRoot: HTMLElement) => HTMLElement | null`  

Default: `null`

The **node** that should **respond** to user **interactions** like [stopOnMouseEnter](/plugins/auto-scroll/#stoponmouseenter) and [stopOnInteraction](/plugins/auto-scroll/#stoponinteraction). If this is omitted, the node that wraps the Embla Carousel will be used as default.

---

## Methods

Below follows an exhaustive **list of all** `Auto Scroll` **methods** with their respective parameters and return values.

---

### play

Parameters: `startDelayOverride?: number`  

Returns: `void`

Start auto scroll. Pass a **startDelayOverride** if you want to change the [startDelay](/plugins/auto-scroll/#startdelay) option after the plugin has been initialized.

---

### stop

Parameters: `none`  

Returns: `void`

Stops auto scroll.

---

### reset

Parameters: `none`  

Returns: `void`

Stops auto scroll, and starts the timer again using [startDelay](/plugins/auto-scroll/#startdelay) when the carousel has settled. This will only take effect if auto scroll is playing. If auto scroll is stopped, this method won't trigger anything.

---

### isPlaying

Parameters: `none`  

Returns: `boolean`

Returns a boolean whether the carousel is auto scrolling or not.

---

## Events

Below follows an exhaustive **list of all** `Auto Scroll` **events** together with information about how they work.

---

### autoScroll:play

Once: `no`

Fires when auto scroll starts playing.

---

### autoScroll:stop

Once: `no`

Fires when auto scroll stops scrolling.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/auto-scroll.mdx)

## Methods | Embla Carousel

[Read the full article](https://www.embla-carousel.com/api/methods/)

# Methods

Embla Carousel exposes a set of **useful methods** which makes it very **extensible**.

---

## Usage

You need an **initialized carousel** in order to **make use of methods**. They can be accessed during the lifecycle of a carousel and won't do anything after a carousel instance has been destroyed with the [destroy](/api/methods/#destroy) method.

### Calling methods

In the following example, the [slideNodes](/api/methods/#slidenodes) method is called and logged to the console as soon as the carousel has been initialized:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`js
import EmblaCarousel from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode)
console.log(emblaApi.slideNodes())
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { useEffect } from 'react'import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel()
 useEffect(() =\> { if (emblaApi) console.log(emblaApi.slideNodes()) }, \[emblaApi])
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import emblaCarouselVue from 'embla\-carousel\-vue'
 const \[emblaRef, emblaApi] = emblaCarouselVue()
 onMounted(() =\> { if (emblaApi.value) console.log(emblaApi.value.slideNodes()) })
 // ...\
\`\`\`Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel()
 onMount(() =\> { const api = emblaApi() if (api) console.log(api.slideNodes()) })
 // ...}
\`\`\`Copy code snippet to clipboardCopy\`\`\`html
\ import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let emblaApi
 function onInit(event) { emblaApi = event.detail console.log(emblaApi.slideNodes()) }\
\...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

### TypeScript

The `EmblaCarouselType` is obtained directly from the **core package** `embla-carousel` and used like so:

VanillaVanillaReactReactVueVueSolidSolidSvelteSvelteCopy code snippet to clipboardCopy\`\`\`tsx
import EmblaCarousel, { EmblaCarouselType } from 'embla\-carousel'
const emblaNode = document.querySelector('.embla')const emblaApi = EmblaCarousel(emblaNode)
function logSlidesInView(emblaApi: EmblaCarouselType): void { console.log(emblaApi.slidesInView())}
emblaApi.on('slidesInView', logSlidesInView)
\`\`\`Copy code snippet to clipboardCopy\`\`\`tsx
import React, { useCallback } from 'react'import { EmblaCarouselType } from 'embla\-carousel'import useEmblaCarousel from 'embla\-carousel\-react'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = useEmblaCarousel()
 const logSlidesInView = useCallback((emblaApi: EmblaCarouselType) =\> { console.log(emblaApi.slidesInView()) }, \[])
 useEffect(() =\> { if (emblaApi) emblaApi.on('slidesInView', logSlidesInView) }, \[emblaApi, logSlidesInView])
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-react` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { onMounted } from 'vue' import { EmblaCarouselType } from 'embla\-carousel' import emblaCarouselVue from 'embla\-carousel\-vue'
 const \[emblaRef] = emblaCarouselVue()
 function logSlidesInView(emblaApi: EmblaCarouselType): void { console.log(emblaApi.slidesInView()) }
 onMounted(() =\> { if (emblaApi.value) emblaApi.value.on('slidesInView', logSlidesInView) })
 // ...\
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-vue` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`jsx
import { onMount } from 'solid\-js'import { EmblaCarouselType } from 'embla\-carousel'import createEmblaCarousel from 'embla\-carousel\-solid'
export function EmblaCarousel() { const \[emblaRef, emblaApi] = createEmblaCarousel()
 function logSlidesInView(emblaApi: EmblaCarouselType): void { console.log(emblaApi.slidesInView()) }
 onMount(() =\> { const api = emblaApi() if (api) api.on('slidesInView', logSlidesInView) })
 // ...}
\`\`\`If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-solid` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

Copy code snippet to clipboardCopy\`\`\`html
\ import { EmblaCarouselType } from 'embla\-carousel' import emblaCarouselSvelte from 'embla\-carousel\-svelte'
 let emblaApi: EmblaCarouselType
 function logSlidesInView(emblaApi: EmblaCarouselType): void { console.log(emblaApi.slidesInView()) }
 function onInit(event: CustomEvent\): void { emblaApi = event.detail emblaApi.on('slidesInView', logSlidesInView) }\
\...\
\`\`\`**Note:** Starting with Svelte 5, the `on:` event handlers have been deprecated. However, `on:emblaInit` will remain for backward compatibility.

If you're using `pnpm`, you need to install `embla-carousel` as a
**devDependency** when importing types from it like demonstrated above.

This is because even though `embla-carousel-svelte` has `embla-carousel` as a
dependency, `pnpm` makes nested dependencies inaccessible by design.

## Reference

Below follows an exhaustive **list of all** Embla Carousel **methods** with their respective parameters and return values.

---

### rootNode

Parameters: `none`  

Returns: `HTMLElement`

Get the root node that holds the scroll container with slides inside. This method can be useful when you need to manipulate the root element dynamically or similar.

---

### containerNode

Parameters: `none`  

Returns: `HTMLElement`

Get the container node that holds the slides. This method can be useful when you need to manipulate the container element dynamically or similar.

---

### slideNodes

Parameters: `none`  

Returns: `HTMLElement[]`

Get all the slide nodes inside the container. This method can be useful when you need to manipulate the slide elements dynamically or similar.

---

### scrollNext

Parameters: `jump?: boolean`  

Returns: `void`

Scroll to the next snap point if possible. When [loop](/api/options/#loop) is disabled and the carousel has reached the last snap point, this method won't do anything. Set the **jump** parameter to `true` when you want to go to the next slide instantly.

---

### scrollPrev

Parameters: `jump?: boolean`  

Returns: `void`

Scroll to the previous snap point if possible. When [loop](/api/options/#loop) is disabled and the carousel has reached the first snap point, this method won't do anything. Set the **jump** parameter to `true` when you want to go to the previous slide instantly.

---

### scrollTo

Parameters: `index: number`, `jump?: boolean`  

Returns: `void`

Scroll to a snap point by its unique index. If [loop](/api/options/#loop) is enabled, Embla Carousel will choose the closest way to the target snap point. Set the **jump** parameter to `true` when you want to go to the desired slide instantly.

---

### canScrollNext

Parameters: `none`  

Returns: `boolean`

Check the possiblity to scroll to a next snap point. If [loop](/api/options/#loop) is enabled and the container holds any slides, this will always return `true`.

---

### canScrollPrev

Parameters: `none`  

Returns: `boolean`

Check the possiblity to scroll to a previous snap point. If [loop](/api/options/#loop) is enabled and the container holds any slides, this will always return `true`.

---

### selectedScrollSnap

Parameters: `none`  

Returns: `number`

Get the index of the selected snap point.

---

### previousScrollSnap

Parameters: `none`  

Returns: `number`

Get the index of the previously selected snap point.

---

### scrollSnapList

Parameters: `none`  

Returns: `number[]`

Get an array containing all the snap point positions. Each position represents how far the carousel needs to progress in order to reach this position.

---

### scrollProgress

Parameters: `none`  

Returns: `number`

Check how far the carousel has scrolled of its scrollable length from 0 \- 1\. For example, **0\.5 equals 50%**. For example, this can be useful when creating a scroll progress bar.

---

### slidesInView

Parameters: `none`  

Returns: `number[]`

Get slide indexes **visible** in the carousel viewport. Honors the [inViewThreshold](/api/options/#inviewthreshold) option.

---

### slidesNotInView

Parameters: `none`  

Returns: `number[]`

Get slide indexes **not visible** in the carousel viewport. Honors the [inViewThreshold](/api/options/#inviewthreshold) option.

---

### internalEngine

Parameters: `none`  

Returns: `EmblaEngineType`

Exposes almost all internal functionality used by Embla. Useful when creating plugins or similar.

**Note:** Please **refrain** from creating **bug reports** related to this
method. If you're using this and running into problems, it's a 99\.8% chance
that you don't understand how this works. Use at your own risk.

---

### reInit

Parameters: `options?: EmblaOptionsType`, `plugins?: EmblaPluginType[]`  

Returns: `void`

Hard reset the carousel after it has been initialized. This method allows for changing [options](/api/options/) and [plugins](/api/plugins/) after initializing a carousel.

**Note:** Passed options will be **merged** with current options, but passed
plugins will **replace** current plugins.

---

### plugins

Parameters: `none`  

Returns: `EmblaPluginsType`

Returns an object with key value pairs where the keys are the plugin names, and the plugin API:s are the values.

---

### destroy

Parameters: `none`  

Returns: `void`

Destroy the carousel instance permanently. This is a one way operation and is intended to be used as a cleanup measure when the carousel instance isn't needed anymore.

---

### on

Parameters: `event: EmblaEventType`, `callback: (emblaApi: EmblaCarouselType, eventName: EmblaEventType) => void`  

Returns: `void`

**Subscribe** to an Embla specific [event](/api/events/) with a **callback**. Added event listeners will persist even if [reInit](/api/methods/#reinit) is called, either until the carousel is destroyed or the event is removed with the [off](/api/methods/#off) method.

---

### off

Parameters: `event: EmblaEventType`, `callback: (emblaApi: EmblaCarouselType, eventName: EmblaEventType) => void`  

Returns: `void`

**Unsubscribe** from an Embla specific [event](/api/events/). Make sure to pass the **same callback reference** when the callback was added with the [on](/api/methods/#on) method.

---

### emit

Parameters: `event: EmblaEventType`  

Returns: `void`

Emits an embla [event](/api/events/). This doesn't trigger any internal Embla functionality.

---

[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/api/methods.mdx)

## Plugins | Embla Carousel

[Read the full article](https://www.embla-carousel.com/plugins/)

# Plugins

Here is a list of available Embla Carousel plugins that will **extend your carousels** with additional features, that goes beyond the built\-in Embla Carousel core features.

---

## Choose a plugin

* [### Autoplay

Learn how to use the Autoplay plugin for Embla Carousel

Read more](/plugins/autoplay/)
* [### Auto Scroll

Learn how to use the Auto Scroll plugin for Embla Carousel

Read more](/plugins/auto-scroll/)
* [### Auto Height

Learn how to use the Auto Height plugin for Embla Carousel

Read more](/plugins/auto-height/)
* [### Class Names

Learn how to use the Class Names plugin for Embla Carousel

Read more](/plugins/class-names/)
* [### Fade

Learn how to use the Fade plugin for Embla Carousel

Read more](/plugins/fade/)
* [### Wheel Gestures

Learn how to add this Wheel Gesture plugin to Embla Carousel

Read more](/plugins/wheel-gestures/)
[Edit this page on GitHub](https://github.com/davidjerleke/embla-carousel/blob/master/packages/embla-carousel-docs/src/content/pages/plugins/index.mdx)

