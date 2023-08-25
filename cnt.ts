
// Generic CountDownLatch implementation
export class CountDownLatch {
    private count: number;
    private resolve!: () => void;
    private promise!: Promise<void>;

    constructor(count: number) {
        this.count = count;
        this.promise = new Promise(resolve => {
            this.resolve = resolve;
        });
    }

    public await(): Promise<void> {
        return this.promise;
    }

    public countDown(): void {
        if (--this.count === 0) {
            this.resolve();
        }
    }
}

cancel_ts.js

if (t) {
    clearTimeout(t);
    return;
}

$.ts

import { CountDownLatch } from "cnt";

export function asyncDelay(cnt: number, towait: number): JQueryPromise<any> {
    return Promise.resolve({}).then(() => {
        const p = new CountDownLatch(cnt);
        return new Promise((resolve, reject) => {
            doAsync(p, towait, reject);
            p.await().then(resolve, reject);
        });
    });
}

example_ts.js

export function example(): number {
    return 5;
}

import { example } from "example";
import { asyncDelay } from "$";

export function main(): void {
    asyncDelay(example(), 300);
}
